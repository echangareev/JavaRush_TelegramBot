from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(F.voice)
async def voice_func_handler(message: Message):
    await message.answer('Ты отправил голосовое сообщение')

