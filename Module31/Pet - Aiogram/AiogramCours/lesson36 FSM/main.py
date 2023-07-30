from aiogram import types, executor, Bot, Dispatcher
from config import API_KEY
from aiogram.dispatcher.filters import Text
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext

from keyboard import work_kb, cancel_kb

storage = MemoryStorage()
my_bot = Bot(API_KEY)
my_disp = Dispatcher(my_bot,
                     storage=storage)


async def on_startup(_):
    print("Бот успешно запущен!")


class MyStatesGroup(StatesGroup):
    photo = State()
    description = State()


@my_disp.message_handler(commands="start")
async def start_command(message: types.Message) -> None:
    await message.delete()
    await message.answer(text="Welcome in my BOT",
                         reply_markup=work_kb())


@my_disp.message_handler(Text(equals="Cancel", ignore_case=True), state="*")
async def cancel_command(message: types.Message, state: FSMContext) -> None:
    await message.reply(text="Canceled",
                        reply_markup=work_kb())
    await state.finish()


@my_disp.message_handler(Text(equals="Start working", ignore_case=True))
async def start_working_command(message: types.Message) -> None:
    await message.reply(text="Send me a photo!",
                        reply_markup=cancel_kb())
    await MyStatesGroup.photo.set()


@my_disp.message_handler(lambda message: not message.photo, state=MyStatesGroup.photo)
async def error_type_send(message: types.Message):
    return await message.reply(text="This is not a photo!")


@my_disp.message_handler(lambda message: message.photo, content_types=["photo"], state=MyStatesGroup.photo)
async def fill_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["photo"] = message.photo[0].file_id

    await MyStatesGroup.next()
    await message.answer(text="Now send me a description!",
                         reply_markup=cancel_kb())


@my_disp.message_handler(lambda message: message.text, content_types=["text"], state=MyStatesGroup.description)
async def fill_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["description"] = message.text

    await message.answer("Your photo was saved")
    await my_bot.send_photo(chat_id=message.from_user.id,
                            photo=data["photo"],
                            caption=data["description"])

    await state.finish()


if __name__ == "__main__":
    executor.start_polling(my_disp, skip_updates=True, on_startup=on_startup)
