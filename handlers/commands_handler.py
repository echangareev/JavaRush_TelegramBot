from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    help_text = '''
    Список достпных команд:
    /start - Начать
    /help - Показать это сообщение
    /whoami - User info
    /about - Информация о боте
    '''
    await message.answer(help_text)


@router.message(Command("about"))
async def cmd_about(message: Message):
    about_answer = "Этот бот написан в процессе обучения"
    await message.answer(about_answer)


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