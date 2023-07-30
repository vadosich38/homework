from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def work_kb() -> ReplyKeyboardMarkup:
    my_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button_working = KeyboardButton(text="Start working")

    my_kb.add(button_working)
    return my_kb


def cancel_kb() -> ReplyKeyboardMarkup:
    my_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button_cancel = KeyboardButton(text="Cancel")

    my_kb.add(button_cancel)
    return my_kb
