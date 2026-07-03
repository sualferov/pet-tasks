from enum import Enum


class UserRegistrationStatus(Enum):
    """Статус регистрации."""

    in_progress = 'in_progress'
    registered = 'registered'
    already_exists = 'already_exists'
    error = 'error'
