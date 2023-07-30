from aiogram import types, executor, Bot, Dispatcher
from config import API_KEY
from keyboards import links_inline_kb, my_kb

my_bot = Bot(API_KEY)
my_disp = Dispatcher(my_bot)


async def on_startup(_):
    print("Бот успешно запущен!")


@my_disp.message_handler(commands="links")
async def links_command(message: types.Message):
    await message.delete()
    await my_bot.send_message(text="Выберите поисковик:", chat_id=message.chat.id, reply_markup=links_inline_kb)


@my_disp.message_handler(commands="start")
async def start_command(message: types.Message):
    await message.delete()
    await my_bot.send_message(text="Добро пожаловать в Бота!",
                              chat_id=message.chat.id, reply_markup=my_kb)

if __name__ == "__main__":
    executor.start_polling(my_disp, skip_updates=True, on_startup=on_startup)
