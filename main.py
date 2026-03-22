import asyncio
import logging

from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import start, about, whoami #random_fact, gpt_chat, talk, quiz


async def main():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - %(levelname)s %(message)s")

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(start.router)
    dp.include_router(about.router)
    dp.include_router(whoami.router)
    #dp.include_router(random_fact.router)
    #dp.include_router(gpt_chat.router)
    #dp.include_router(talk.router)
    #dp.include_router(quiz.router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())