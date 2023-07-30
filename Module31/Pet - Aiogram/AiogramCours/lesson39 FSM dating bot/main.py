import aiogram.types
from aiogram.types import ContentTypes
from config import API_KEY
from keyboards import get_kb, get_cancel_kb
from aiogram.dispatcher.filters import Text
from aiogram import Bot, executor, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext

my_bot = Bot(API_KEY)
my_storage = MemoryStorage()
my_disp = Dispatcher(bot=my_bot,
                     storage=my_storage)


async def on_startup(_):
    print("Бот успешно запущен")


class MyStatesGroup(StatesGroup):
    photo = State()
    name = State()
    age = State()
    description = State()


@my_disp.message_handler(Text(equals="cancel", ignore_case=True), state="*")
async def cmd_start(message: types.Message, state: FSMContext):
    await message.reply(text="Вы отменили создание профиля",
                        reply_markup=get_kb())
    await state.finish()


@my_disp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    await message.delete()
    await message.answer("Добро пожаловать в бота, где вы можете познакомиться с новыми людьми! ❤️‍🔥\n\n"
                         "Для создния профиля нажмите кнопку CREATE PROFILE 👇 внизу или напишите "
                         "такое сообщение боту  ✍️",
                         reply_markup=get_kb())


@my_disp.message_handler(Text(equals="create profile", ignore_case=True), state="*")
async def cmd_create_profile(message: types.Message):
    await message.delete()
    await MyStatesGroup.photo.set()
    await message.answer(text="Пришлите ваше фото  📸",
                         reply_markup=get_cancel_kb())


@my_disp.message_handler(lambda message: not message.photo, state=MyStatesGroup.photo)
async def check_photo(message: types.Message):
    await message.reply("⛔️ Это не фото! Пришлите ваше фото")


@my_disp.message_handler(lambda message: message.photo, content_types="photo", state=MyStatesGroup.photo)
async def fill_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["photo"] = message.photo[0].file_id

    await MyStatesGroup.next()
    await message.answer(text="Теперь пришлите ваше имя 🗣")


@my_disp.message_handler(lambda message: message.text, content_types="text", state=MyStatesGroup.name)
async def fill_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["name"] = message.text

    await MyStatesGroup.next()
    await message.answer(text="Теперь пришлите ваш возраст 🔞\nВы должны быть старне 18 и младше 90 ⛔️")


@my_disp.message_handler(content_types=ContentTypes.ANY, state=MyStatesGroup.name)
async def check_name(message: types.Message):
    await message.reply(text="⛔️ Это не имя! Пришлите ваше имя в текстовом формате")


@my_disp.message_handler(lambda message: not message.text.isdigit() or not (18 <= float(message.text) <= 90),
                         state=MyStatesGroup.age)
async def check_age(message: types.Message):
    await message.reply(text="⛔️ Это не корректный возраст! Пришлите корректный возраст")


@my_disp.message_handler(lambda message: message.text.isdigit, content_types="text", state=MyStatesGroup.age)
async def fill_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["age"] = int(message.text)

    await MyStatesGroup.next()
    await message.answer(text="Теперь пришлите информацию о себе 🔞\nИнформация о себе должна быть не менее 50 знаков, "
                              "но не более 1000 ⛔️")


@my_disp.message_handler(lambda message: 50 <= len(message.text) <= 1000,
                         content_types=ContentTypes.TEXT,
                         state=MyStatesGroup.description)
async def fill_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["description"] = message.text

    await state.finish()
    await message.answer(text="Ваш профиль успешно создан!\n")
    await my_bot.send_photo(chat_id=message.chat.id,
                            photo=data["photo"],
                            caption=f"Имя: {data['name']}\nВозраст: {data['age']}\nО себе: {data['description']}")


@my_disp.message_handler(content_types=ContentTypes.ANY,
                         state=MyStatesGroup.description)
async def check_description(message: types.Message):
    await message.reply(text="⛔️ Описание не соответствует требованиям! Пришлите корректное описание")


if __name__ == "__main__":
    executor.start_polling(dispatcher=my_disp,
                           skip_updates=True,
                           on_startup=on_startup)
