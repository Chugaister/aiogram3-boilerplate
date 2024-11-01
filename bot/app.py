from contextlib import asynccontextmanager

from aiogram.types import BotCommand, Update
from fastapi import FastAPI, Response

from bot.bot import bot, dp
from utils.getenv import config
from utils.tunneling import create_tunnel


async def on_startup():
    await bot.delete_webhook()
    await bot.save_get_me()
    await bot.set_my_commands([
        BotCommand(command="start", description="перезавантажити бота"),
        BotCommand(command="help", description="список команд")
    ])
    if config.LOCAL:
        config.WEBHOOK_HOST = create_tunnel(config.APP_PORT)
    await bot.set_webhook(
        f"{config.WEBHOOK_HOST}/{config.BOT_TOKEN}",
        allowed_updates=["message", "chat_join_request", "callback_query"]
    )


async def on_shutdown():
    await bot.delete_webhook()
    await bot.session.close()


@asynccontextmanager
async def lifespan(app_: FastAPI):
    await on_startup()
    yield
    await on_shutdown()


app = FastAPI(lifespan=lifespan)


@app.post("/{request_token}")
async def handle_update(update: Update, request_token: str):
    if request_token == config.BOT_TOKEN:
        await dp.feed_update(bot=bot, update=update)
        return Response(status_code=200)
    else:
        return Response(status_code=404)
