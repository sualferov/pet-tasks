import os

import redis.asyncio as redis
from dotenv import dotenv_values


config = dotenv_values(os.environ.get('ENV_FILE'))
print(f'\n\n{config.get("REDIS_CONNECTION")}\n\n')
redis_db = redis.Redis.from_pool(connection_pool=redis.ConnectionPool.from_url(url=config.get('REDIS_CONNECTION')))
