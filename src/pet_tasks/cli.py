import click


@click.group()
def cli() -> None:
    """Создание группы команд."""


@cli.command('run')
def run_task() -> None:
    """Выполняет задачу."""
    print('Executing task ...')
