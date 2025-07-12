from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

inline_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Напитки", callback_data='drinks'),InlineKeyboardButton(text="Пиццы", callback_data='pizza')],
    [InlineKeyboardButton(text="Салаты", callback_data='salat')]
])