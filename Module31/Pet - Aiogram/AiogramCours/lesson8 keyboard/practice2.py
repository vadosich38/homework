from aiogram import types, executor, Bot, Dispatcher
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from config import API_KEY

HELP_TEXT = "HELP_TEXT"
DESCRIPTION_TEXT = "DESCRIPTION_TEXT"

my_bot = Bot(API_KEY)
my_disp = Dispatcher(my_bot)

my_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

help_button = KeyboardButton("/help")
orange_button = KeyboardButton("/orange")
description_button = KeyboardButton("/description")
location_button = KeyboardButton("/location")

my_keyboard.add(help_button, description_button, location_button, orange_button)


async def on_startup(_):
    print("Бот успешно запущен!")


@my_disp.message_handler(commands="start")
async def start_answer(message: types.Message):
    await message.delete()
    await my_bot.send_message(chat_id=message.chat.id, text="Добро пожаловать в БОТ!", reply_markup=my_keyboard)


@my_disp.message_handler(commands="orange")
async def start_answer(message: types.Message):
    await message.delete()
    await my_bot.send_photo(chat_id=message.from_user.id,
                            photo="https://www.gastronom.ru/binfiles/images/20220127/ba944b65.jpg")


@my_disp.message_handler(commands="description")
async def description_answer(message: types.Message):
    await message.delete()
    await message.answer(text=DESCRIPTION_TEXT)


@my_disp.message_handler(commands="help")
async def help_answer(message: types.Message):
    await message.delete()
    await message.answer(text=HELP_TEXT)


@my_disp.message_handler(commands="location")
async def help_answer(message: types.Message):
    await message.delete()
    await my_bot.send_location(chat_id=message.chat.id, longitude=1.432, latitude=53.321)


@my_disp.message_handler()
async def help_answer(message: types.Message):
    pass

if __name__ == "__main__":
    executor.start_polling(my_disp, skip_updates=True, on_startup=on_startup)
