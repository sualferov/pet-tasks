from langgraph.graph import END, START, StateGraph

from pet_tasks.exceptions.server_error import ServerError
from pet_tasks.langgraph.entities.user_registration import UserRegistrationState
from pet_tasks.langgraph.enums.user_registration import UserRegistrationStatus
from pet_tasks.langgraph.handlers.entities.user_register import UserRegisterRequest, UserRegisterResponse
from pet_tasks.langgraph.repositories.pg_users import UsersRepo


class UserRegistrationService:
    """Класс бизнес-логики регистрации пользователя."""

    @classmethod
    async def register(cls, request: UserRegisterRequest) -> UserRegisterResponse:
        """Регистрирует пользователя."""
        try:
            graph = StateGraph(UserRegistrationState)

            graph.add_node('start_node', lambda state: state)
            graph.add_node('raise_user_exists_error', cls.raise_user_exists_error_)
            graph.add_node('create_user', cls.create_user_)

            graph.add_edge(START, 'start_node')
            graph.add_conditional_edges(
                'start_node',
                cls.check_user_exist_,
                {
                    True: 'raise_user_exists_error',
                    False: 'create_user',
                },
            )
            graph.add_edge('raise_user_exists_error', END)
            graph.add_edge('create_user', END)

            app = graph.compile()

            result = await app.ainvoke(
                UserRegistrationState(
                    email=request.email,
                    name=request.name,
                    status=UserRegistrationStatus.in_progress,
                ),  # type: ignore
            )
        except Exception as err:
            raise ServerError from err

        return UserRegisterResponse.model_validate(result)

    @classmethod
    async def check_user_exist_(cls, state: UserRegistrationState) -> bool:
        """Проверяет, существует ли пользователь с таким email."""
        return await UsersRepo.check_user_exist_by_email(email=state.email)

    @classmethod
    def raise_user_exists_error_(cls, state: UserRegistrationState) -> dict[str, UserRegistrationStatus]:
        """Возвращает статус - пользователь уже зарегистрирован."""
        return {'status': UserRegistrationStatus.already_exists}

    @classmethod
    async def create_user_(cls, state: UserRegistrationState) -> dict[str, object]:
        """Создает нового пользователя."""
        user_id = await UsersRepo.create_user(email=state.email, name=state.name)
        return {'status': UserRegistrationStatus.registered, 'user_id': user_id}
