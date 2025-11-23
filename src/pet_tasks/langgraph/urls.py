from pet_tasks.langgraph.handlers.hello import api_hello_handler


urls = [
    ('/api/langgraph/hello/', api_hello_handler, ['GET'], 'lg_hello'),
]
