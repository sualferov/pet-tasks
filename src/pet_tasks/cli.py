import click
import uvicorn
from fastapi import FastAPI, Request, Response, status
from fastapi.responses import JSONResponse
from pydantic import ValidationError

from pet_tasks.exceptions.server_error import ServerError
from pet_tasks.langgraph.urls import urls as lg_urls


fast_api_app = FastAPI(title='Pet tasks web server')
for url in lg_urls:
    fast_api_app.add_api_route(path=url[0], endpoint=url[1], methods=url[2], name=url[3])


@fast_api_app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc: ValidationError) -> Response:
    """Возвращает информацию об ошибке, если переданы некорректные данные."""
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={'message': 'Invalid data provided', 'errors': exc.errors()},
    )


@fast_api_app.exception_handler(ServerError)
async def server_exception_handler(request: Request, exc: ServerError) -> Response:
    """Возвращает информацию об ошибке, если переданы некорректные данные."""
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={'message': 'API Server error'},
    )


@click.group()
def cli() -> None:
    """Создание группы команд."""


@cli.command('web-serve')
@click.option('--host', type=str, default='127.0.0.1')
@click.option('--port', type=int, default=8000)
@click.option('--debug', type=bool, default=False)
def run_web_server(*, host: str, port: int, debug: bool) -> None:
    """Run Web-server."""
    uvicorn.run('pet_tasks.cli:fast_api_app', host=host, port=port, reload=debug)
