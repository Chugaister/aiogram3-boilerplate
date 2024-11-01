from aiogram import Router
from aiogram.filters.command import Command
from aiogram.types import Message

from bot.customs.bot import CustomBot
from bot.filters.regexp import Regexp
from bot.views.common.inform import hide_message_kb

support_router = Router(name="support")


@support_router.message(Regexp("Підтримка"))
@support_router.message(Command("support"))
async def send_agency_menu(msg: Message, bot: CustomBot):
    await msg.delete()
    await msg.answer(
        "Тебе ніхто не підтримає",
        reply_markup=hide_message_kb(text="🔽")
    )
