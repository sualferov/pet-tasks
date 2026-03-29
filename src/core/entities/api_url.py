from collections.abc import Callable
from dataclasses import dataclass
from typing import Any

from starlette.responses import Response


@dataclass
class APIUrl:
    """Класс объекта APIUrl."""

    path: str
    handler: Callable[..., Any]
    methods: list[str]
    name: str
    response_class: type[Response] | None = None
