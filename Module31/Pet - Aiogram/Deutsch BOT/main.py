from config import API_KEY
from aiogram import Bot, executor, types, Dispatcher
from aiogram.utils.exceptions import InvalidHTTPUrlContent
from keyboards import inline_kb, regular_kb
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import CallbackQuery
import requests


noun_link = "https://www.verbformen.de/deklination/substantive/"
verb_link = "https://www.verbformen.de/konjugation/steckbrief/"
preteritum_link = "https://www.verbformen.de/konjugation/indikativ/praeteritum/"
presens_link = "https://www.verbformen.de/konjugation/indikativ/praesens/"

letters_pars = {"A": "Ä", "a": "ä", "U": "Ü", "u": "ü", "O": "Ö", "o": "ö"}
my_memory = MemoryStorage()
my_bot = Bot(API_KEY)
my_disp = Dispatcher(bot=my_bot,
                     storage=my_memory)


async def on_startup(_):
    print("Бот успешно запущен")


class MyStatesGroup(StatesGroup):
    verb = State()
    noun = State()


@my_disp.message_handler(commands=["start"], state="*")
async def cmd_start(message: types.Message) -> None:
    await message.delete()
    await message.answer(text="Добро пожаловать!  🥳\nЭто не простой бот, а очень грамотный  🤓\n"
                              "Чтобы убедиться в этом, выберите режим работы с ботом –– глаголы или существительные  ✍️\n"
                              "После выбора отправьте мне любое существительное или глагол на немецком языке  🇩🇪",
                         reply_markup=regular_kb())


@my_disp.message_handler(Text(equals="Хочу узнать больше о глаголах  🧠", ignore_case=True), state="*")
async def verb_chang_state(message: types.Message, state: FSMContext):
    if state == MyStatesGroup.verb:
        await message.reply("Бот уже работает в этом режиме!  🛑")
    else:
        await MyStatesGroup.verb.set()
        await message.reply("Теперь отправь мне любой глагол на немецком языке  🇩🇪")


@my_disp.message_handler(Text(equals="Хочу узнать больше о существительных  💪", ignore_case=True), state="*")
async def noun_chang_state(message: types.Message, state: FSMContext):

    if state == MyStatesGroup.noun:
        await message.reply("Бот уже работает в этом режиме!  🛑")
    else:
        await MyStatesGroup.noun.set()
        await message.reply("Теперь отправь мне любое существительное на немецком языке  🇩🇪")


@my_disp.message_handler(state=MyStatesGroup.noun)
async def noun_answer(message: types.Message) -> None:
    wort = message.text.capitalize()
    for letter, umlaut in letters_pars.items():
        if umlaut in wort:
            wort = wort.replace(umlaut, letter + "3")

    wort_link = noun_link + wort + ".png"
    try:
        await my_bot.send_photo(chat_id=message.chat.id,
                                photo=wort_link,
                                caption="Вот ваше существительное  👨🏻‍🏫")
    except InvalidHTTPUrlContent:
        await message.reply(text="Такое существительно не найдено  👮‍♂️")


@my_disp.message_handler(state=MyStatesGroup.verb)
async def verb_answer(message: types.Message, state: FSMContext) -> None:
    wort = message.text.lower()
    for letter, umlaut in letters_pars.items():
        if umlaut in wort:
            wort = wort.replace(umlaut, letter + "3")

    wort_link = verb_link + wort + ".png"

    response = requests.get(url=wort_link)
    if response.status_code == 404:
        wort_link = wort_link.replace(".png", "_ist.png")
        response = requests.get(url=wort_link)
        if response.status_code == 404:
            wort_link = wort_link.replace("_ist.png", "_haben.png")
            response = requests.get(url=wort_link)
            if response.status_code == 404:
                await message.reply(text="Такой глагол не найден  👮‍♂️")

    async with state.proxy() as data:
        data["wort"] = wort
        data["message"] = message
        data["wort_link"] = wort_link
    try:
        await my_bot.send_photo(chat_id=message.chat.id,
                                photo=wort_link,
                                caption="Вот ваш глагол  👨🏻‍🏫",
                                reply_markup=inline_kb())

    except InvalidHTTPUrlContent:
        await message.reply(text="Такой глагол не найден  👮‍♂️")


@my_disp.callback_query_handler(text="preteritum", state=MyStatesGroup.verb)
async def callback_preteritum(callback_data: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        message = data["message"]
        wort_link = data["wort_link"].replace(verb_link, "")
        wort_link = preteritum_link + wort_link
    print(wort_link)

    await callback_data.answer(text="Будет выполнено  🫡")
    try:
        await my_bot.send_photo(chat_id=message.chat.id,
                                photo=wort_link,
                                caption="Этот глагол в Präteritum  👨🏻‍🏫")
    except InvalidHTTPUrlContent:
        await message.reply(text="Для этого глагола данные не найдены  👮‍♂️")


@my_disp.callback_query_handler(text="presens", state=MyStatesGroup.verb)
async def callback_presens(callback_data: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        message = data["message"]
        wort_link = data["wort_link"].replace(verb_link, "")
        wort_link = presens_link + wort_link
    print(wort_link)

    await callback_data.answer(text="Будет выполнено  🫡")

    try:
        await my_bot.send_photo(chat_id=message.chat.id,
                                photo=wort_link,
                                caption="Этот глагол в Präsens  👨🏻‍🏫")
    except InvalidHTTPUrlContent:
        await message.reply(text="Для этого глагола данные не найдены  👮‍♂️")


if __name__ == "__main__":
    executor.start_polling(dispatcher=my_disp,
                           on_startup=on_startup,
                           skip_updates=True)
