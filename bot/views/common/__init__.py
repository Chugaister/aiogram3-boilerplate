from aiogram import Router

from .plugs import plugs_router

common_router = Router(name="common")
common_router.include_router(plugs_router)
