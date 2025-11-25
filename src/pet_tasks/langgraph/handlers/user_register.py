from starlette.requests import Request


def user_register_handler(request: Request) -> dict[str, object]:
    """Обрабатывает АПИ вызов."""
    return {'some': 'val2'}
