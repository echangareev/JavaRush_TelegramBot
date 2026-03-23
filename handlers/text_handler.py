from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

router = Router()


@router.message(F.text.lower() == 'привет')
async def cmd_text(message: Message):
    help_text = 'И тебе привет'
    await message.answer(help_text)


@router.message(F.text.lower() == 'как дела')
async def cmd_text(message: Message):
    await message.answer('Всё отлично, а у тебя как?')


@router.message(F.text.lower().contains('помощь'))
async def handle_help_word(message: Message):
    await message.answer()