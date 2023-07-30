from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_inline_kb() -> InlineKeyboardMarkup:
    my_ikb = InlineKeyboardMarkup()
    button_plus = InlineKeyboardButton(text="+",
                                       callback_data="+")
    button_minus = InlineKeyboardButton(text="-",
                                        callback_data="-")
    my_ikb.add(button_plus, button_minus)
    return my_ikb
