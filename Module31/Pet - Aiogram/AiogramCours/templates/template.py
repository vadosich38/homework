from aiogram import types, executor, Bot, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import API_KEY

my_bot = Bot(API_KEY)
my_disp = Dispatcher(my_bot)


async def on_startup(_):
    print("Бот успешно запущен!")


if __name__ == "__main__":
    executor.start_polling(my_disp, skip_updates=True, on_startup=on_startup)
