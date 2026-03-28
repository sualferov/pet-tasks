from fastapi.sse import EventSourceResponse

from core.entities.api_url import APIUrl
from pet_tasks.fastapi_sse.handlers.stream import sse_stream_handler
from pet_tasks.fastapi_sse.handlers.stream_publish import sse_stream_publish_handler

urls = [
    APIUrl(
        path='/api/sse/stream/',
        handler=sse_stream_handler,
        methods=['POST'],
        name='api_sse_stream',
        response_class=EventSourceResponse,
    ),
    APIUrl(
        path='/api/sse/stream/publish/',
        handler=sse_stream_publish_handler,
        methods=['POST'],
        name='api_sse_stream_publish',
    ),
]
