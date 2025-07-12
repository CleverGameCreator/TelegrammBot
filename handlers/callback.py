from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

call_router = Router()

@call_router.message(F.text == "Меню")
async def menu(message: Message):
    await message.answer("Выберите пункт меню:")

@call_router.message(F.text == "Поддержка")
async def menu(message: Message):
    await message.answer("Поддержка от создателей :)")

@call_router.message(F.text == "Информация")
async def menu(message: Message):
    await message.answer("Информация о боте тут")

@call_router.message(F.text == "Назад")
async def menu(message: Message):
    await message.answer("Выберите пункт меню:")