from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

def menu_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="🌤 Weather"),
                KeyboardButton(text="📰 News")
            ],
            [
                KeyboardButton(text="⚙ Settings")
            ],
            [
                KeyboardButton(text="❌ Close menu")
            ]
        ], resize_keyboard=True)

    return keyboard


def inline_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="🌤 Weather", callback_data="weather")
        ],
        [
            InlineKeyboardButton(text="📰 News", callback_data="news")
        ],
        [
            InlineKeyboardButton(text="⚙ Settings", callback_data="settings")
        ],
        [
            InlineKeyboardButton(text="❌ Close menu", callback_data="close")
        ],
        [InlineKeyboardButton(text = "Push me", callback_data='btn:hello', style = 'danger')],
        [InlineKeyboardButton(text="Google", url = 'https://www.google.com', style = 'success')] #style = 'primary'
    ])

    return keyboard

def special_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text = "Send my phone number", request_contact = True)],
            [KeyboardButton(text = "Send my geolocation", request_location=True)]
        ],
        resize_keyboard = True
    )
    return keyboard