from aiogram import Router

from .status import status_router

admin_router = Router(name="admin")
admin_router.include_router(status_router)
