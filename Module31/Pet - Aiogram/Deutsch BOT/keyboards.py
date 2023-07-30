from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup


def regular_kb() -> ReplyKeyboardMarkup:
    my_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    verb_button = KeyboardButton(text="Хочу узнать больше о глаголах  🧠")
    noun_button = KeyboardButton(text="Хочу узнать больше о существительных  💪")

    my_kb.add(verb_button, noun_button)
    return my_kb


def inline_kb() -> InlineKeyboardMarkup:
    my_ikb = InlineKeyboardMarkup(row_width=3)
    pr_button = InlineKeyboardButton(text="Präteritum  👀",
                                     callback_data="preteritum")
    presens_button = InlineKeyboardButton(text="Präsens  👀",
                                          callback_data="presens")
    my_ikb.add(pr_button, presens_button)

    return my_ikb