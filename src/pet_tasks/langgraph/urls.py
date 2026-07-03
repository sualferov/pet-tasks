from core.entities.api_url import APIUrl
from pet_tasks.langgraph.handlers.user_register import user_register_handler


urls = [
    APIUrl(
        path='/api/langgraph/user-register/',
        handler=user_register_handler,
        methods=['POST'],
        name='api_langgrapth_user_register',
    ),
]
