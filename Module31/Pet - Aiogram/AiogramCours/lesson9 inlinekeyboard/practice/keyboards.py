from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup


links_inline_kb = InlineKeyboardMarkup(row_width=3)
my_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

button_links = KeyboardButton(text="/links")
my_kb.add(button_links)

in_b1 = InlineKeyboardButton(text="Google", url="google.com")
in_b2 = InlineKeyboardButton(text="Bing", url="bing.com")
in_b3 = InlineKeyboardButton(text="Yandex", url="yandex.com")
in_b4 = InlineKeyboardButton(text="Yahoo", url="yahoo.com")

links_inline_kb.add(in_b1, in_b2, in_b3, in_b4)
