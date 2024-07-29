from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton   )

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Жанры")],[KeyboardButton(text="Hello")],
    [KeyboardButton(text="Goodmorning")], [KeyboardButton(text="Goodbye")]
], 
                                    resize_keyboard=True,
                                    input_field_placeholder="Выбери пункт в меню")

settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='YouTube', url='https://animego.org/anime')]
])