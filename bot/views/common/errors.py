from aiogram import F
from aiogram.filters.exception import ExceptionTypeFilter
from aiogram.types import CallbackQuery, Message
from aiogram.types.error_event import ErrorEvent

from bot.customs.bot import CustomBot
from bot.customs.dispatcher import CustomDispatcher
from bot.views.common.inform import hide_message_kb
from transport.exceptions import APIError, NotFoundError


def init_error_handlers(dp: CustomDispatcher):

    @dp.error(ExceptionTypeFilter(NotFoundError), F.update.message.as_("message"))
    async def handle_not_found_msg(error_event: ErrorEvent, message: Message, bot: CustomBot):
        await message.answer(
            "❗️Помилка. Об'єкт не знайдено. Оновіть сторінку та спробуйте ще раз",
            reply_markup=hide_message_kb()
        )
        await bot.safe_delete_message(message.from_user.id, message.message_id)

    @dp.error(ExceptionTypeFilter(NotFoundError), F.update.callback_query.as_("callback_query"))
    async def handle_not_found_cb(error_event: ErrorEvent, callback_query: CallbackQuery, bot: CustomBot):
        await bot.safe_answer_callback_query(
            callback_query.id,
            "❗️Помилка. Об'єкт не знайдено. Оновіть сторінку та спробуйте ще раз",
            show_alert=True
        )

    @dp.error(ExceptionTypeFilter(APIError), F.update.message.as_("message"))
    async def handle_api_error_msg(error_event: ErrorEvent, message: Message, bot: CustomBot):
        await message.answer(
            f"❗️Невідома помилка. Оновіть сторінку та спробуйте ще раз\n<pre>{error_event.exception.json}</pre>",
            reply_markup=hide_message_kb()
        )
        await bot.safe_delete_message(message.from_user.id, message.message_id)

    @dp.error(ExceptionTypeFilter(APIError), F.update.callback_query.as_("callback_query"))
    async def handle_api_error_cb(error_event: ErrorEvent, callback_query: CallbackQuery, bot: CustomBot):
        await bot.safe_answer_callback_query(
            callback_query.id,
            f"❗️Невідома помилка. Оновіть сторінку та спробуйте ще раз\n{error_event.exception.json}",
            show_alert=True
        )
