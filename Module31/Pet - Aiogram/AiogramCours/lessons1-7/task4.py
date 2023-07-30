from aiogram import types, Bot, executor, Dispatcher
from config import API_KEY

my_bot = Bot(API_KEY)
my_disp = Dispatcher(my_bot)


@my_disp.message_handler(commands="give")
async def command_give(message: types.Message):
    await message.answer("Смотри какой смешной кот ❤️")
    await my_bot.send_sticker(message.from_user.id,
                              sticker="CAACAgIAAxkBAAEJjphkoTmK3Rc6VTkBzlGrRI3LIKbF2QACwwIAAtqkIzCz5lU7VJruEi8E")
    await message.delete()


@my_disp.message_handler()
async def answer(message: types.Message):
    if message.text == "❤️":
        await message.delete()
        await message.answer("🖤")


if __name__ == "__main__":
    executor.start_polling(my_disp)
