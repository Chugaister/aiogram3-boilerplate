from aiogram import Router

from .agency import agency_router
from .start import start_router
from .support import support_router

menu_router = Router(name="menu")
menu_router.include_router(start_router)
menu_router.include_router(agency_router)
menu_router.include_router(support_router)
