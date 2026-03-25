from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from texts.messages import MESSAGES
from aiogram.fsm.context import FSMContext
from states.states import RegistrationProfile
from utils.file_handler import write_to_file, get_user_from_file


router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    # await message.answer(MESSAGES["start"])
    user = get_user_from_file('data/users.json', message.from_user.id)
    if user:
        await message.answer(f'Hello {user["name"]}')
    else:
        await message.answer("Hello! What is your name? To cancel /cancel")
        await state.set_state(RegistrationProfile.waiting_name)
    # start_text = '''
    # Список достпных команд:
    # /start - Начать
    # /help - Показать это сообщение
    # /whoami - User info
    # /about - Информация о боте
    # '''
    # await message.answer(start_text)


@router.message(Command('cancel'))
async def cmd_cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Last move canceled")


@router.message(RegistrationProfile.waiting_name)
async def cmd_waiting_name(message: Message, state: FSMContext):
    await message.answer(f'Nice to meat you, {message.text}')
    await state.update_data(id = message.from_user.id)
    await state.update_data(name = message.text)
    await message.answer('How old are you? To cancel /cancel')
    await state.set_state(RegistrationProfile.waiting_age)


@router.message(RegistrationProfile.waiting_age)
async def cmd_waiting_age(message: Message, state: FSMContext):
    await message.answer(f'Wow! Nice. You are {message.text} years old')
    await state.update_data(age = message.text)
    await message.answer('Where are you from? To cancel /cancel')
    await state.set_state(RegistrationProfile.waiting_city)


@router.message(RegistrationProfile.waiting_city)
async def cmd_waiting_city(message: Message, state: FSMContext):
    await message.answer(f'You are from {message.text}! Awesome!')
    await state.update_data(city = message.text)
    data = await state.get_data()
    await message.answer(f'Info about you: {data}')
    write_to_file('data/users.json', data)
    await state.clear()


@router.message(Command("about"))
async def cmd_about(message: Message):
    await message.answer(MESSAGES["about"])
    # about_answer = "Этот бот написан в процессе обучения"
    # await message.answer(about_answer)


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

@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(MESSAGES["help"])
    # help_text = '''
    #     Список достпных команд:
    #     /start - Начать
    #     /help - Показать это сообщение
    #     /whoami - User info
    #     /about - Информация о боте
    #     '''
    # await message.answer(help_text)