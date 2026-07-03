from pydantic import BaseModel


class StreamRequest(BaseModel):
    """Класс запроса."""

    last_id: int | None = None


class StreamPublishRequest(BaseModel):
    """Класс запроса при публикации в стрим."""

    channel_id: int
    message: str


class StreamPublishResponse(BaseModel):
    """Класс ответа при публикации в стрим."""

    status: str
