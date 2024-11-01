from redis.asyncio.client import Redis

from utils.getenv import config

rds = Redis.from_url(url=config.REDIS_URL)

