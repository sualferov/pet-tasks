from collections.abc import AsyncIterable

from fastapi.sse import ServerSentEvent
from pydantic import BaseModel

from core.db.redis import redis_db
from pet_tasks.fastapi_sse.handlers.entities.stream import StreamPublishRequest, StreamPublishResponse, StreamRequest


class Item(BaseModel):
    """Класс элемента."""

    name: str
    price: float


items = [
    Item(name='Plumbus', price=32.99),
    Item(name='Portal Gun', price=999.99),
    Item(name='Meeseeks Box', price=49.99),
]
items.extend(items * 100)


class StreamService:
    """Сервис для работы с потоком данных."""

    @classmethod
    async def stream(cls, request: StreamRequest) -> AsyncIterable[ServerSentEvent]:
        """Стримит поток данных."""
        yield ServerSentEvent(comment='SSE Stream')

        async with redis_db.pubsub() as pubsub:
            await pubsub.subscribe('channel:1')
            while True:
                message = await pubsub.get_message(ignore_subscribe_messages=True)
                if message:
                    if message['data'].decode() == 'STOP':
                        break
                    yield ServerSentEvent(data=message, event='Item_update', id='1')
            await pubsub.unsubscribe('channel:1')

    @classmethod
    async def publish(cls, request: StreamPublishRequest) -> StreamPublishResponse:
        """Публикует сообщение."""
        await redis_db.publish(channel=f'channel:{request.channel_id}', message=request.message)

        return StreamPublishResponse(status='ok')
