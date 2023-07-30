from aiogram import types, executor, Dispatcher, Bot
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from config import API_KEY

my_bot = Bot(API_KEY)
my_disp = Dispatcher(my_bot)

my_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton("/help")
button2 = KeyboardButton("/description")
button3 = KeyboardButton("/photo")
button4 = KeyboardButton("/location")

my_keyboard.add(button1, button2, button3, button4)

my_keyboard2 = ReplyKeyboardMarkup(resize_keyboard=True)
back_button = KeyboardButton("/back")
my_keyboard2.add(back_button)

HELP_COMMAND = """
<b>/help</b> - <em>список команд</em>
<b>/start</b> - <em>старт бота</em>
<b>/description</b> - <em>описание бота</em>
<b>/photo</b> - <em>отрпавка фото</em>
<b>/location</b> - <em>отправить геолокацию</em>
"""


async def on_startup(_):
    print("Бот успешно запущен!")


@my_disp.message_handler(commands=["back"])
async def back(message: types.Message):
    await message.delete()
    await my_bot.send_message(chat_id=message.from_user.id, text="выполняю команду!", reply_markup=ReplyKeyboardRemove())
    await my_bot.send_message(chat_id=message.from_user.id, text="выполняю команду!", reply_markup=my_keyboard)


@my_disp.message_handler(commands=["help"])
async def help_answer(message: types.Message):
    await message.delete()
    await my_bot.send_message(chat_id=message.from_user.id, text=HELP_COMMAND, parse_mode="HTML",
                              reply_markup=ReplyKeyboardRemove())
    await my_bot.send_message(chat_id=message.from_user.id, text="выполняю команду!", reply_markup=my_keyboard2)


@my_disp.message_handler(commands=["start"])
async def start_answer(message: types.Message):
    await message.delete()
    await my_bot.send_message(chat_id=message.from_user.id, text="Добро пожаловать в BOT", reply_markup=my_keyboard)


@my_disp.message_handler(commands=["description"])
async def description_answer(message: types.Message):
    await message.delete()
    await my_bot.send_message(chat_id=message.from_user.id, text="Наш бот умеет отправлять фотографии",
                              reply_markup=ReplyKeyboardRemove())
    await my_bot.send_message(chat_id=message.from_user.id, text="выполняю команду!", reply_markup=my_keyboard2)


@my_disp.message_handler(commands=["photo"])
async def photo_answer(message: types.Message):
    await message.delete()
    await my_bot.send_photo(photo="https://t1.gstatic.com/licensed-image?q=tbn:ANd9GcRRv9ICxXjK-LVFv-lKRId6gB45BFoNCLsZ"
                                  "4dk7bZpYGblPLPG-9aYss0Z0wt2PmWDb",
                            chat_id=message.from_user.id, reply_markup=ReplyKeyboardRemove())
    await my_bot.send_message(chat_id=message.from_user.id, text="выполняю команду!", reply_markup=my_keyboard2)


@my_disp.message_handler(commands=["location"])
async def location_answer(message: types.Message):
    await message.delete()
    await my_bot.send_location(chat_id=message.from_user.id, latitude=5.422, longitude=1.3211,
                               reply_markup=ReplyKeyboardRemove())
    await my_bot.send_message(chat_id=message.from_user.id, text="выполняю команду!", reply_markup=my_keyboard2)


if __name__ == "__main__":
    executor.start_polling(my_disp, on_startup=on_startup, skip_updates=True)
