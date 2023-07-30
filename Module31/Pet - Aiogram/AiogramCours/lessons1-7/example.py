import aiogram
from aiogram import Bot, Dispatcher, executor, types

api_key = "6126620863:AAG8OxQQhtNnT0tsDoEMg6yDY1R8NcgenwI"

my_bot = Bot(api_key)
my_dp = Dispatcher(my_bot)


@my_dp.message_handler()
async def echo(message: types.Message):
    await message.answer(text="Все говорят '{}', а ты купи слона!".format(message.text))

if __name__ == "__main__":
    executor.start_polling(my_dp)
