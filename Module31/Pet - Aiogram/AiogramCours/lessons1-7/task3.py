import random
import string

from aiogram import Bot, executor, types, Dispatcher
from config import API_KEY
call_counter = 0

my_bot = Bot(API_KEY)
my_disp = Dispatcher(my_bot)

description = """
Этот бот создан для практики

Его функцион меняется каждую минуту
"""


async def on_startup(_):
    print("Бот был успешно запущен!")


@my_disp.message_handler(commands="give")
async def give(message: types.Message):
    await my_bot.send_sticker(chat_id=message.from_user.id,
                              sticker="CAACAgIAAxkBAAEJjbxkoHV9Cpb1EgWoL6f08_4GeLTCMAACzwADy_l-NuAzlLoWpDEZLwQ")
    await message.delete()


@my_disp.message_handler(commands="description")
async def descr(message: types.message):
    await message.reply(description)


@my_disp.message_handler(commands="count")
async def counter(message: types.message):
    global call_counter

    await message.reply("Эта команда была вызвана {} раз".format(call_counter))
    call_counter += 1


@my_disp.message_handler(commands="start")
async def start(message: types.message):
    await message.answer("<em><b>Добро</b> пожаловать в моего бота!</em>", parse_mode="HTML")
    await message.delete()


@my_disp.message_handler()
async def answer(message: types.message):
    if "0" in message.text:
        await message.reply("NO 🌚")
    elif "1" in message.text:
        await message.reply("YES 😱")
    else:
        await message.reply(random.choice(string.ascii_letters))


if __name__ == "__main__":
    executor.start_polling(my_disp, on_startup=on_startup)
