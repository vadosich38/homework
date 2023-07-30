import aiogram.utils.callback_data
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

my_cb_data_pattern = CallbackData("ikb", "action")
# паттерн колбека, выглядит как словарь {action: "здесь значение доьавленное после .new"}


def kb_return(my_pattern: aiogram.utils.callback_data.CallbackData) -> types.InlineKeyboardMarkup:
    my_ikb = InlineKeyboardMarkup(row_width=3)

    button_1 = InlineKeyboardButton(text="Button_1", callback_data=my_pattern.new("button1"))
    button_2 = InlineKeyboardButton(text="Button_2", callback_data=my_pattern.new("button2"))

    my_ikb.add(button_1).add(button_2)

    return my_ikb
