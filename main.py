import asyncio
import logging

from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers.commands_handler import router as command_router
from handlers.text_handler import router as text_router
from handlers.voice_handler import router as voice_router


async def main():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - %(levelname)s %(message)s")

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(command_router)
    dp.include_router(text_router)
    dp.include_router(voice_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())