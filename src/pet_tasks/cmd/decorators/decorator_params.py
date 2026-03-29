from collections.abc import Callable
from functools import wraps
from typing import ParamSpec, TypeVar, Concatenate

TParam = ParamSpec('TParam')
TReturn = TypeVar('TReturn')

def multi_calls(count: int) -> Callable[[Callable[TParam, TReturn]], Callable[TParam, None]]:
    """Вызывает метод указанное кол-во раз."""
    def decorator(func: Callable[TParam, TReturn]) -> Callable[TParam, None]:
        @wraps(func)
        def wrapper(*args: TParam.args, **kwargs: TParam.kwargs) -> None:
            for i in range(count):
                print(f'Calling: {i}')
                func(*args, **kwargs)
        return wrapper
    return decorator
