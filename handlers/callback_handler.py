from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

router = Router()

@router.callback_query(F.data == 'btn:hello')
async def cmd_hello(callback: CallbackQuery):
    await callback.message.answer('you pushed the button') # answer as message
    await callback.answer('you pushed the button')  # answer as pop-up message from above