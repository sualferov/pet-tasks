from pet_tasks.cmd.decorators.decorator_params import multi_calls


@multi_calls(count=3)
def some_function() -> None:
    """Тестируемый метод."""
    print('Some function')


def run_cmd() -> None:
    """Запускает код для проверки в консоле."""
    some_function()
