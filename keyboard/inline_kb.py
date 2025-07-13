from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

list = ["Кола","Фанта","Спрайт"]

inline_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Напитки", callback_data='drinks'),InlineKeyboardButton(text="Пиццы", callback_data='pizza')],
    [InlineKeyboardButton(text="Салаты", callback_data='salat')]
])

async def drinks_list():
    keyboard = InlineKeyboardBuilder()
    for drinks in list:
        keyboard.add(InlineKeyboardButton(text=drinks, callback_data=drinks))

    return keyboard.as_markup()