import json

import requests
from aiogram import Bot, executor, types, Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from config_data.config import API_TOKEN, API_MARKER, TG_KEY
my_bot = Bot(TG_KEY)
my_disp = Dispatcher(my_bot)
HELP = """
<b>Список команд бота</b>

<b>/low</b><i> –– показать самые дешевые перелеты</i>
<b>/high</b><i> –– показать самые дорогие перелеты</i>
<b>/custom</b><i> –– показать перелеты в вашем диапазоне цен</i>
<b>/history</b><i> –– показать историю запросов</i>
"""
HELLO_TEXT = """
<b>Добро пожаловать в Travel Bot</b>
<i>В этом боте вы сможете найти некоторую информацию о перелетах</i>

<b>Воспользуйтесь командой /help для просмотра возможностей бота</b>
"""

my_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
button_help = KeyboardButton("/help")
button_low = KeyboardButton("/low")
button_high = KeyboardButton("/high")
button_custom = KeyboardButton("/custom")
my_keyboard.add(button_help, button_low, button_high, button_custom)


async def on_startup(_):
    print("Бот успешно запустился!")


def low(origin: str, destination: str, date_departure: str, date_return: str) -> str:
    """
    Функция выполняющая запрос к API и получает данные о самом дешевом перелете по заданым параметрам
    :origin -- город вылета
    :destination -- город назначения
    :date_departure -- дата вылета
    :date_return -- дата возвращения
    :return: текст результата запроса или текст ошибки
    """
    url = "https://api.travelpayouts.com/v1/prices/cheap"
    querystring = {"origin": "MOW", "destination": "HKT", "depart_date": "2023-11", "return_date": "2023-12",
                   "currency": "EUR"} #пример запроса
    headers = {'x-access-token': API_TOKEN}
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.text


@my_disp.message_handler(commands=["start"])
async def start_answer(message: types.Message):
    await message.delete()
    await message.answer(HELLO_TEXT, parse_mode="HTML", reply_markup=my_keyboard)


@my_disp.message_handler(commands=["help"])
async def help_answer(message: types.Message):
    await message.answer(HELP, parse_mode="HTML")
    await message.delete()


@my_disp.message_handler(commands=["low"])
async def low_answer(message: types.Message):
    pass
    #нужно запросить ввод у пользователя
    # res_dict = json.loads(low(origin=origin, destination=destination, date_departure=date_departure, date_return=date_return)) #десериализуем джейсон
    # await message.reply("<b>Данные вашего перелета:</b>\n\nМаршрут: x - x \nДата вылета: x \nДата обратного вылета: x \n"
    #                     "Стоимость: {} EUR".format(res_dict["data"]["HKT"]["2"]["price"]), parse_mode="HTML")


@my_disp.message_handler(commands=["high"])
async def high_answer(message: types.Message):
    pass


@my_disp.message_handler(commands=["custom"])
async def custom_answer(message: types.Message):
    pass


@my_disp.message_handler(commands=["history"])
async def history_answer(message: types.Message):
    pass


if __name__ == "__main__":
    executor.start_polling(my_disp, on_startup=on_startup, skip_updates=True)
