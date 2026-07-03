from pydantic import BaseModel

from pet_tasks.langgraph.enums.user_registration import UserRegistrationStatus


class UserRegisterRequest(BaseModel):
    """Класс запроса - регистрация пользователя."""

    email: str
    name: str | None = None


class UserRegisterResponse(BaseModel):
    """Класс ответа - регистрация пользователя."""

    status: UserRegistrationStatus
    user_id: int | None = None
