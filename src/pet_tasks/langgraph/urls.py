from pet_tasks.langgraph.handlers.user_register import user_register_handler


urls = [
    ('/api/langgraph/user-register/', user_register_handler, ['POST'], 'api_langgrapth_user_register_handler'),
]
