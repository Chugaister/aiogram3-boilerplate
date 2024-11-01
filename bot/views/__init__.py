from aiogram import Router

from .admin import admin_router
from .menu import menu_router

main_router = Router(name="main")
main_router.include_router(admin_router)
main_router.include_router(menu_router)
