from starlette.requests import Request

from pet_tasks.langgraph.handlers.entities.user_register import UserRegisterRequest, UserRegisterResponse
from pet_tasks.langgraph.services.user_register import UserRegistrationService


async def user_register_handler(request: Request) -> UserRegisterResponse:
    """Обрабатывает АПИ вызов."""
    return await UserRegistrationService.register(
        request=UserRegisterRequest.model_validate(obj=await request.json()),
    )
