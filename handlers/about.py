from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("about"))
async def cmd_about(message: Message):
    about_answer = "Этот бот написан в процессе обучения"
    await message.answer(about_answer)