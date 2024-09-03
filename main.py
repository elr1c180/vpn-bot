import asyncio
from aiogram import Dispatcher, Bot

from handlers import start, support


async def main():
    bot = Bot(token='7045835036:AAFXA_3w7-qkyfJ52bW9fKBWip6PRmAFewM')
    dp = Dispatcher()

    dp.include_routers(start.router, support.router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())