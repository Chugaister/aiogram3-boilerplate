from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot.customs.bot import CustomBot

from .cbdata import GeneralActionCB


def hide_message_kb(text: str = "OK", callback_data="general_action:hide_message") -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[
            InlineKeyboardButton(text=text, callback_data=callback_data)
        ]]
    )
    return keyboard


def cancel_kb(callback_data: str, text="Відміна") -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[
            InlineKeyboardButton(text=text, callback_data=callback_data)
        ]]
    )
    return keyboard

