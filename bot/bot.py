from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.redis import RedisStorage

from bot.customs.bot import CustomBot
from bot.customs.dispatcher import CustomDispatcher
from bot.views import main_router
from bot.views.common.errors import init_error_handlers
from utils.getenv import config
from utils.rds import rds

# basicConfig(level=DEBUG)
storage = RedisStorage(rds)
bot = CustomBot(config.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = CustomDispatcher()
dp.include_router(main_router)
init_error_handlers(dp)

