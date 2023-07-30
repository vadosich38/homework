from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def get_kb() -> ReplyKeyboardMarkup:
    my_kb = ReplyKeyboardMarkup(resize_keyboard=True)

    create_btn = KeyboardButton(text="CREATE PROFILE")

    my_kb.add(create_btn)
    return my_kb


def get_cancel_kb() -> ReplyKeyboardMarkup:
    my_kb = ReplyKeyboardMarkup(resize_keyboard=True)

    create_btn = KeyboardButton(text="CANCEL")

    my_kb.add(create_btn)
    return my_kb

