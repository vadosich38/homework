from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_inline_kb() -> InlineKeyboardMarkup:
    my_ikb = InlineKeyboardMarkup()
    button_plus = InlineKeyboardButton(text="+",
                                       callback_data="+")
    button_minus = InlineKeyboardButton(text="-",
                                        callback_data="-")
    button_random = InlineKeyboardButton(text="random",
                                         callback_data="random")
    my_ikb.add(button_plus, button_minus, button_random)
    return my_ikb
