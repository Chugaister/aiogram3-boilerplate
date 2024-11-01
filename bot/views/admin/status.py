from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

status_router = Router(name="status")


@status_router.message(Command("status"))
async def send_status(msg: Message):
    await msg.answer("Bot is running")
