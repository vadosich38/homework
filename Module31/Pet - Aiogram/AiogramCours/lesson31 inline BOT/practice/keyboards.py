from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

my_pattern = CallbackData("ikb1", "action")


def get_ikb() -> types.InlineKeyboardMarkup:
    my_ikb = InlineKeyboardMarkup(row_width=2)

    button1 = InlineKeyboardButton(text="Button1",
                                   callback_data=my_pattern.new("button1"))
    button2 = InlineKeyboardButton(text="Button2",
                                   callback_data=my_pattern.new("button2"))

    my_ikb.add(button1, button2)
    return my_ikb
