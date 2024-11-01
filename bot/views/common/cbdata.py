from aiogram.filters.callback_data import CallbackData


class GeneralActionCB(CallbackData, prefix="general_action"):
    action: str
