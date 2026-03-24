from aiogram import Router
from handlers.commands_handler import router as command_router
from handlers.text_handler import router as text_router
from handlers.voice_handler import router as voice_router


router = Router()
router.include_router(command_router)
router.include_router(text_router)
router.include_router(voice_router)