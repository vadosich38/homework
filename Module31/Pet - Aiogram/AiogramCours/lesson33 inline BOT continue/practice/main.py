from aiogram import types, executor, Bot, Dispatcher
from config import API_KEY
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent
import hashlib

my_bot = Bot(API_KEY)
my_disp = Dispatcher(my_bot)


async def on_startup(_):
    print("Бот успешно запущен!")


@my_disp.inline_handler()
async def my_inline_handler(inline_query: types.InlineQuery):
    text = inline_query.query or "Текст отсутствует! 👎"
    answer_id = hashlib.md5(text.encode()).hexdigest()

    bold = InlineQueryResultArticle(id=str(answer_id+"bold"),
                                    title="BOLD",
                                    input_message_content=InputTextMessageContent(f"<b>{text}</b>",
                                                                                  parse_mode="HTML"),
                                    thumb_url="https://play-lh.googleusercontent.com/"
                                              "xfO6a13oViRQoaPJ7EFu1DW5kZXB6PHuREPVv9o4xVNlqrGlhUAjo5hBWo3N5Bf6XzZ0",
                                    description="Выберите этот пункт, чтобы вернуть жирный текст!")

    italic = InlineQueryResultArticle(id=str(answer_id+"italic"),
                                      title="ITALIC",
                                      input_message_content=InputTextMessageContent(f"<i>{text}</i>",
                                                                                    parse_mode="HTML"),
                                      thumb_url="https://cdn.dribbble.com/userupload/4816339/file/"
                                                "original-98c4b364bbe0b51bea0033f6596b16f6.png?resize=400x0",
                                      description="Выберите этот пункт, чтобы вернуть курсивный текст!")

    await my_bot.answer_inline_query(inline_query_id=inline_query.id,
                                     results=[bold, italic],
                                     cache_time=1)
if __name__ == "__main__":
    executor.start_polling(my_disp, skip_updates=True, on_startup=on_startup)
