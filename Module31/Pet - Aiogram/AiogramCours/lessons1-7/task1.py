from aiogram import Bot, Dispatcher, types, executor

API_KEY = "6126620863:AAG8OxQQhtNnT0tsDoEMg6yDY1R8NcgenwI"

my_bot = Bot(API_KEY)
my_disp = Dispatcher(my_bot)


@my_disp.message_handler()
async def answer(message: types.Message):
    await message.answer(message.text.upper())

if __name__ == "__main__":
    executor.start_polling(my_disp)
