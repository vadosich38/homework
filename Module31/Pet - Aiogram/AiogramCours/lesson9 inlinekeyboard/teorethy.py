from aiogram import types, executor, Bot, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import API_KEY

my_bot = Bot(API_KEY)
my_disp = Dispatcher(my_bot)
my_inline_kb = InlineKeyboardMarkup(row_width=2)

button_ok = InlineKeyboardButton(text="OK", url="https://www.google.com/search?q=%D1%81%D0%B0%D0%B9%D1%82%D1%8B+%D0%B"
                                                "4%D0%BB%D1%8F+%D0%BC%D0%BE%D0%BB%D0%BE%D0%B4%D1%86%D0%BE%D0%B2&oq=%D1"
                                                "%81%D0%B0%D0%B9%D1%82%D1%8B+%D0%B4%D0%BB%D1%8F+%D0%BC%D0%BE%D0%BB%D0%B"
                                                "E%D0%B4%D1%86%D0%BE%D0%B2&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIJCAEQIRgKGKA"
                                                "BMgkIAhAhGAoYoAEyCQgDECEYChigAdIBCDM0ODdqMGo3qAIAsAIA&sourceid=chrome"
                                                "&ie=UTF-8")
button_not_ok = InlineKeyboardButton(text="Not OK", url="https://www.google.com/search?sxsrf=AB5stBg3mtmpuYvCf98Fmjcd3"
                                                        "kVq62-sZw:1688652265087&q=%D1%81%D0%B0%D0%B9%D1%82%D1%8B+%D0"
                                                        "%B4%D0%BB%D1%8F+%D0%B4%D1%83%D1%80%D0%B0%D0%BA%D0%BE%D0%B2&"
                                                        "spell=1&sa=X&ved=2ahUKEwjMjaPzn_r_AhUchv0HHZnIB30QBSgAegQIFh"
                                                        "AB&biw=1440&bih=789&dpr=2")

my_inline_kb.add(button_ok, button_not_ok)


@my_disp.message_handler(commands="start")
async def start_answer(message: types.Message):
    await message.delete()
    await message.answer(text="Добро пожаловать в нашего бота", reply_markup=my_inline_kb)


async def on_startup(_):
    print("Бот успешно запущен!")


if __name__ == "__main__":
    executor.start_polling(my_disp, skip_updates=True, on_startup=on_startup)
