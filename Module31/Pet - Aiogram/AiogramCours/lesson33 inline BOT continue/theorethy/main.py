from aiogram import types, executor, Bot, Dispatcher
from config import API_KEY
from aiogram.types import InputTextMessageContent, InlineQueryResultArticle
import hashlib

my_bot = Bot(API_KEY)
my_disp = Dispatcher(my_bot)
user_num = ""


@my_disp.message_handler(commands="start")
async def start_command(message: types.Message) -> None:
    await message.delete()
    await message.answer(text="Добро пожаловать в бот, это не простой ЭХО бот! Введите ваше число: ")


@my_disp.message_handler()
async def get_my_message(message: types.Message) -> None:
    global user_num
    user_num = message.text

    await message.reply(text="Данные сохранены!")


@my_disp.inline_handler()
async def inline_handler(inline_query: types.InlineQuery):
    text = f"{inline_query.query} - {user_num}"

    input_content = InputTextMessageContent(f"<b>{text}</b>", parse_mode="HTML")
    answer_id = hashlib.md5(text.encode()).hexdigest()

    item = InlineQueryResultArticle(
        id=answer_id,
        input_message_content=input_content,
        title=text)

    await my_bot.answer_inline_query(
        inline_query_id=inline_query.id,
        results=[item],
        cache_time=1
    )


async def on_startup(_):
    print("Бот успешно запущен!")


if __name__ == "__main__":
    executor.start_polling(my_disp, skip_updates=True, on_startup=on_startup)
