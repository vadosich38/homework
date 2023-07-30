from aiogram import types, executor, Bot, Dispatcher
from config import API_KEY
from keyboards import my_inline_kb
my_bot = Bot(API_KEY)
my_disp = Dispatcher(my_bot)
flag = None


async def on_startup(_):
    print("Бот успешно запущен!")


@my_disp.message_handler(commands="start")
async def start_cmd(message: types.Message):
    await my_bot.send_photo(chat_id=message.from_user.id,
                            photo="https://img.freepik.com/free-photo/a-heart-shaped-cloud-is-in-the-sky-with-the-word-love-on-it_1340-34492.jpg",
                            reply_markup=my_inline_kb,
                            caption="Вам нравится это фото?")
    await message.delete()


@my_disp.callback_query_handler(text="clear")
async def clear_cmd(callback: types.CallbackQuery):
    await callback.answer("Удалить сообщение!")
    await callback.message.delete()


@my_disp.callback_query_handler()
async def clb_handler(callback: types.CallbackQuery):
    global flag
    if callback.data == "like":
        if flag:
            await callback.answer(show_alert=True,
                                  text="Вы уже лайкнули это фото!")
        else:
            flag = True
            await callback.answer("Вам понравилось фото!")
    elif callback.data == "dislike":
        if not flag:
            await callback.answer(show_alert=True,
                                  text="Вы уже дизлайкнули это фото")
        else:
            flag = False
            await callback.answer("Вам не понравилось фото!")


if __name__ == "__main__":
    executor.start_polling(my_disp,
                           skip_updates=True,
                           on_startup=on_startup)
