from os import getenv
from typing import Any


class EnvVariableNotFound(Exception):
    pass


class Config:

    def __init__(self):
        self.BOT_TOKEN = self.get_var("BOT_TOKEN")
        self.WEBHOOK_HOST = self.get_var("WEBHOOK_HOST")
        self.API_URL = self.get_var("API_URL")
        self.REDIS_URL = self.get_var("REDIS_URL")
        self.APP_PORT = int(self.get_var("APP_PORT", default=8000))
        self.NGROK_AUTH_TOKEN = self.get_var("NGROK_AUTH_TOKEN", optional=True)
        self.LOCAL = self.get_var("LOCAL", optional=True, default=False) == "true"

    @staticmethod
    def get_var(item: str, optional: bool = False, default: Any = None):
        var = getenv(item)
        if not var and not optional and not default:
            raise EnvVariableNotFound(f"Environment variable {item} not found")
        if not var and default:
            return default
        return var


config = Config()
