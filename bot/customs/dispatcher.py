from typing import Any

from aiogram import Bot, Dispatcher
from aiogram.types import Update


class CustomDispatcher(Dispatcher):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.last_update_id = None

    async def feed_update(self, bot: Bot, update: Update, **kwargs: Any) -> Any:
        if not self.last_update_id or self.last_update_id < update.update_id:
            self.last_update_id = update.update_id
            await super().feed_update(bot, update, **kwargs)
