from aiogram import types, executor, Bot, Dispatcher
from config import API_KEY
from keyboard import get_inline_kb
import random

my_bot = Bot(API_KEY)
my_disp = Dispatcher(my_bot)
number = 0


async def on_startup(_):
    print("Бот успешно запущен!")


@my_disp.message_handler(commands="start")
async def start_cmd(message: types.Message) -> None:
    await message.delete()
    await my_bot.send_message(chat_id=message.chat.id,
                              text="Текущее число {}".format(number),
                              reply_markup=get_inline_kb())


@my_disp.callback_query_handler(lambda callback: callback.data == "+" or callback.data == "-")
async def calc_handler(callback_obj: types.CallbackQuery) -> None:
    global number
    if callback_obj.data == "+":
        number += 1
        await callback_obj.message.edit_text(text="Текущее число {}".format(number),
                                             reply_markup=get_inline_kb())
    elif callback_obj.data == "-":
        number -= 1
        await callback_obj.message.edit_text(text="Текущее число {}".format(number),
                                             reply_markup=get_inline_kb())
    else:
        raise Exception("Получена неизвестная callback data")


@my_disp.callback_query_handler()
async def all_callbacks_handler(callback_obj: types.CallbackQuery):
    global number
    if callback_obj.data == "random":
        number = random.randint(-100, 100)
        await callback_obj.message.edit_text(text="Текущее число {}".format(number),
                                             reply_markup=get_inline_kb())

if __name__ == "__main__":
    executor.start_polling(my_disp,
                           skip_updates=True,
                           on_startup=on_startup)
