from aiogram import types, executor, Bot, Dispatcher
from config import API_KEY
from keyboard import kb_return, my_cb_data_pattern
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent
import hashlib


my_bot = Bot(API_KEY)
my_disp = Dispatcher(my_bot)


async def on_startup(_):
    print("Бот успешно запущен!")


@my_disp.message_handler(commands="start")
async def start_answer(message: types.Message):
    await message.delete()
    await my_bot.send_message(text="Welcome to my Aiogram YouTube Bot! Dont forget to subscribe to my chanel!",
                              chat_id=message.from_user.id,
                              reply_markup=kb_return(my_pattern=my_cb_data_pattern))


@my_disp.callback_query_handler(my_cb_data_pattern.filter(action="button1")) #фильтруем по значению ключа словаря "action"
async def button1_handler(callback: types.CallbackQuery):
    await callback.answer(text="Hello")


@my_disp.callback_query_handler(my_cb_data_pattern.filter(action="button2")) #фильтруем по значению ключа словаря "action"
async def button2_handler(callback: types.CallbackQuery):
    await callback.answer(text="World")


@my_disp.inline_handler()
async def inline_query_handler(inline_query: types.InlineQuery) -> None:
    text = inline_query.query or "Echo"
    input_content = InputTextMessageContent(text)
    result_id = hashlib.md5(text.encode()).hexdigest()

    item = InlineQueryResultArticle(
        input_message_content=input_content,
        id=result_id,
        title="Inline Echo Mode ❤️‍🔥"
    )

    await my_bot.answer_inline_query(inline_query_id=inline_query.id,
                                     results=[item],
                                     cache_time=1)


if __name__ == "__main__":
    executor.start_polling(my_disp, skip_updates=True,
                           on_startup=on_startup)
