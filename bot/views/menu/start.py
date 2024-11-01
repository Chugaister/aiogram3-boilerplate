from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.customs.bot import CustomBot

start_router = Router(name="start")


async def send_greeting(bot: CustomBot, user_id: int, username: str, first_name: str, last_name: str):
    text = (
        "Skymarket – це надійна платформа для проведення ефективної рекламної кампанії.\n\n"
        "У нас ви зможете легко придбати та продати рекламу у Telegram, захистивши себе від скаму."
    )
    await bot.send_message(
        user_id,
        text
    )


@start_router.message(CommandStart())
async def start(msg: Message, bot: CustomBot):
    await send_greeting(
        bot,
        msg.from_user.id,
        msg.from_user.username,
        msg.from_user.first_name,
        msg.from_user.last_name
    )
    return
