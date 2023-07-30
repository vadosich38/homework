from aiogram import types, Dispatcher, Bot, executor
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent
from keyboards import get_ikb
from config import API_KEY
import hashlib

my_bot = Bot(API_KEY)
my_disp = Dispatcher(my_bot)


@my_disp.message_handler(commands="start")
async def start_handler(message: types.Message):
    await message.delete()
    await my_bot.send_message(chat_id=message.chat.id,
                              text="Добро пожаловать в бота!",
                              reply_markup=get_ikb())


@my_disp.inline_handler()
async def inline_message_handler(inline_query: types.InlineQuery):
    if inline_query.query == "photo" or inline_query.query == "Photo":
        text = "This is photo"
    else:
        text = inline_query.query or "Echo"

    input_content = InputTextMessageContent(text)
    answer_id = hashlib.md5(text.encode()).hexdigest()

    item = InlineQueryResultArticle(
        input_message_content=input_content,
        id=answer_id,
        title="Функция Ехо для ващего текста!"
    )

    await my_bot.answer_inline_query(
        inline_query_id=inline_query.id,
        results=[item],
        cache_time=1)


async def on_startup(_):
    print("Бот успешно запущен")


if __name__ == "__main__":
    executor.start_polling(dispatcher=my_disp,
                           on_startup=on_startup,
                           skip_updates=True)
