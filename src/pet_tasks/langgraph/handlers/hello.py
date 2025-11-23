from starlette.requests import Request


def api_hello_handler(request: Request) -> dict[str, object]:
    """Обрабатывает АПИ вызов."""
    return {'some': 'val2'}
