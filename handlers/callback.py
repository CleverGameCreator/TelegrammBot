from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

call_router = Router()

import keyboard.inline_kb as ikb

@call_router.message(F.text == "Меню")
async def menu(message: Message):
    await message.answer("Выберите пункт меню:", reply_markup=ikb.inline_kb)

@call_router.message(F.text == "Поддержка")
async def menu(message: Message):
    await message.answer("Поддержка от создателей :)")

@call_router.message(F.text == "Информация")
async def menu(message: Message):
    await message.answer("Информация о боте тут")

@call_router.message(F.text == "Назад")
async def menu(message: Message):
    await message.answer("Выберите пункт меню:")



@call_router.callback_query(F.data == 'drinks')
async def drinks(callback: CallbackQuery):
    await callback.message.answer("Напитки:\nКола\nФанта\nСпрайт")

@call_router.callback_query(F.data == 'pizza')
async def drinks(callback: CallbackQuery):
    await callback.message.answer("Пиццы:\nМаргарита\nПиперони\nСырная")

@call_router.callback_query(F.data == 'salat')
async def drinks(callback: CallbackQuery):
    await callback.message.answer("Салаты:\nЦезарь\nОливье\nДомашний")