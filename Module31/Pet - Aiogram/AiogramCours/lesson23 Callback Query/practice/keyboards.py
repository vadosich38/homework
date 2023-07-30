from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

my_inline_kb = InlineKeyboardMarkup(row_width=3)
like_button = InlineKeyboardButton(text="❤️",
                                   callback_data="like")
dislike_button = InlineKeyboardButton(text="👎",
                                      callback_data="dislike")
clear_button = InlineKeyboardButton(text="❌",
                                    callback_data="clear")
my_inline_kb.add(like_button, dislike_button, clear_button)
