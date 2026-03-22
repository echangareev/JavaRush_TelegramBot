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

