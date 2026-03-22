from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("whoami"))
async def cmd_whoami(message: Message):
    user = message.from_user

    info = (
        f"Your telegram ID: {user.id}",
        f"Your full name: {user.full_name or 'empty'}",
        f"Your language: {user.language_code or 'empty'}",
        f"Your username: {user.username or 'empty'}"
    )
    await message.answer(str(info))