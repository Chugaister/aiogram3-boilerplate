from aiogram import F, Router
from aiogram.types import CallbackQuery

from .cbdata import GeneralActionCB

plugs_router = Router(name="plugs")


@plugs_router.callback_query(GeneralActionCB.filter(F.action == "hide_message"))
async def hide_message(cb: CallbackQuery, callback_data: GeneralActionCB):
    await cb.message.delete()


@plugs_router.callback_query(lambda cb: cb.data == "not_implemented")
async def not_implemented(cb: CallbackQuery):
    await cb.answer("In development, coming soon...", show_alert=True)
