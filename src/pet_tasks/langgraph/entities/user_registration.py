from pydantic import BaseModel

from pet_tasks.langgraph.enums.user_registration import UserRegistrationStatus


class UserRegistrationState(BaseModel):
    """Класс состояния регистрации."""

    email: str
    user_id: int | None = None
    name: str | None = None
    status: str | UserRegistrationStatus = UserRegistrationStatus.in_progress
