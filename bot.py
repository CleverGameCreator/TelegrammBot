import asyncio
import os
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from config import API_BOT
from handlers.commands import router




async def main():
    try:
        bot = Bot(API_BOT)
        dp = Dispatcher()
        print('Бот запущен')
        dp.include_router(router)
        await dp.start_polling(bot)
    except Exception as ex:
        print(f"There is an Exception {ex}")


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот отключен')
