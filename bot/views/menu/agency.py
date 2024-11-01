from aiogram import Router
from aiogram.filters.command import Command
from aiogram.types import Message

from bot.customs.bot import CustomBot
from bot.filters.regexp import Regexp
from bot.views.common.inform import hide_message_kb

agency_router = Router(name="agency")


@agency_router.message(Regexp("Агентство"))
@agency_router.message(Command("agency"))
async def send_agency_menu(msg: Message, bot: CustomBot):
    await msg.delete()
    text = (
        "Рекламна агенція <a href='https://t.me/CloudUA_agency'>Cloud</a> ☁️ "
        "надає усі необхідні послуги для гарантованого заробітку у TG:\n"
        "\t• розробка рекламних кампаній\n"
        "\t• IT-послуги будь-якої складності\n"
        "\t• ведення каналів під ключ\n"
        "\t• створення рекламних креативів\n"
        "\t• наповнення каналу контентом\n"
        "\t• продаж та закуп реклами\n"
        "\t• послуги дизайнерів\n"
        "\t• створення рекламних креативів\n\n"
        "Детальніше: <a href='https://t.me/CloudUA_agency'>Cloud Agency</a>"
    )
    await msg.answer(
        text,
        reply_markup=hide_message_kb(text="🔽")
    )
