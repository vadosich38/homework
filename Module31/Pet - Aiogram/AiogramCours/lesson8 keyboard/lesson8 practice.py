from aiogram import types, executor, Bot, Dispatcher
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from config import API_KEY

HELP_TEXT = "HELP_TEXT"
DESCRIPTION_TEXT = "DESCRIPTION_TEXT"

my_bot = Bot(API_KEY)
my_disp = Dispatcher(my_bot)

my_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

help_button = KeyboardButton("/help")
description_button = KeyboardButton("/description")

my_keyboard.add(help_button, description_button, KeyboardButton("❤️"))


async def on_startup(_):
    print("Бот успешно запущен!")


@my_disp.message_handler(commands="start")
async def start_answer(message: types.Message):
    await message.delete()
    await message.answer(text="Добро пожаловать в БОТ!", reply_markup=my_keyboard)


@my_disp.message_handler(commands="description")
async def description_answer(message: types.Message):
    await message.delete()
    await message.answer(text=DESCRIPTION_TEXT)


@my_disp.message_handler(commands="help")
async def help_answer(message: types.Message):
    await message.delete()
    await message.answer(text=HELP_TEXT)


@my_disp.message_handler()
async def help_answer(message: types.Message):
    if message.text == "❤️":
        await my_bot.send_sticker(sticker="CAACAgIAAxkBAAEJjphkoTmK3Rc6VTkBzlGrRI3LIKbF2QACwwIAAtqkIzCz5lU7VJruEi8E",
                                  chat_id=message.from_user.id)

if __name__ == "__main__":
    executor.start_polling(my_disp, skip_updates=True, on_startup=on_startup)
