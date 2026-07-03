import os

import redis.asyncio as redis
from dotenv import dotenv_values


config = dotenv_values(os.environ.get('ENV_FILE'))
redis_db = redis.Redis.from_pool(
    connection_pool=redis.ConnectionPool.from_url(url=config.get('REDIS_CONNECTION') or ''),
)
