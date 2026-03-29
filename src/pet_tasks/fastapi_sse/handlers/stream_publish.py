from pet_tasks.fastapi_sse.handlers.entities.stream import StreamPublishRequest, StreamPublishResponse
from pet_tasks.fastapi_sse.services.stream import StreamService


async def sse_stream_publish_handler(request: StreamPublishRequest) -> StreamPublishResponse:
    """Обработчик АПИ /stream."""
    return await StreamService.publish(request=request)
