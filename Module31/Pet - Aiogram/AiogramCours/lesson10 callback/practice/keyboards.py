from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

my_kb = ReplyKeyboardMarkup(resize_keyboard=True)
my_inline_kb = InlineKeyboardMarkup(row_width=2)
like_button = InlineKeyboardButton(text="👍", callback_data="like")
dislike_button = InlineKeyboardButton(text="👎", callback_data="dislike")
random_photo_location = InlineKeyboardButton(text="Отправить рандомную локацию", callback_data="location")
next_photo_button = InlineKeyboardButton(text="Следующее фото", callback_data="next_photo")
my_inline_kb.add(like_button, dislike_button, random_photo_location, next_photo_button)


description_button = KeyboardButton(text="/description")
photo_button = KeyboardButton(text="/send_photo")
help_button = KeyboardButton(text="/help")
favorite_button = KeyboardButton(text="/favorite")
not_favorite_button = KeyboardButton(text="/not_favorite")
location_button = KeyboardButton(text="/location")
emoji_button = KeyboardButton(text="/funny_emoji")
sticker_button = KeyboardButton(text="/funny_sticker")

my_kb.add(description_button, photo_button, help_button, favorite_button, not_favorite_button, location_button,
          emoji_button, sticker_button)
