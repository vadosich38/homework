from aiogram import Bot, executor, types, Dispatcher

API_KEY = "6126620863:AAG8OxQQhtNnT0tsDoEMg6yDY1R8NcgenwI"

my_bot = Bot(API_KEY)
my_disp = Dispatcher(my_bot)


@my_disp.message_handler()
async def answer(message: types.Message):
    if len(message.text.split()) > 1:
        await message.answer(message.text)


if __name__ == "__main__":
    executor.start_polling(my_disp)
