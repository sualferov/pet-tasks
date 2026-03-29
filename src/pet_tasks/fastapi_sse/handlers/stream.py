from collections.abc import AsyncIterable

from fastapi.sse import ServerSentEvent

from pet_tasks.fastapi_sse.handlers.entities.stream import StreamRequest
from pet_tasks.fastapi_sse.services.stream import StreamService


async def sse_stream_handler(request: StreamRequest) -> AsyncIterable[ServerSentEvent]:
    """Обработчик АПИ /stream."""
    async for item in StreamService.stream(request=request):
        yield item
