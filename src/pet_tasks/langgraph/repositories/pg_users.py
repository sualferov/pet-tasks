from pet_tasks.langgraph.db.postgres import postgres_db


class UsersRepo:
    """Класс репозитория к таблице users."""

    @classmethod
    async def check_user_exist_by_email(cls, email: str) -> bool:
        """Проверяет наличие пользователя в таблице по email."""
        row = await postgres_db.fetchrow(
            query='select 1 from users where email=$1 limit 1',
            args=[email],
        )
        return bool(row)

    @classmethod
    async def create_user(cls, email: str, name: str | None = None) -> int | None:
        """Создание записи в таблице users."""
        user_id = await postgres_db.fetchval(
            query='insert into users(name, email) values($1, $2) returning id',
            args=(name, email),
        )

        return int(user_id) if user_id else None
