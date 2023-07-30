from aiogram import types, executor, Bot, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from config import API_KEY

my_bot = Bot(API_KEY)
my_disp = Dispatcher(my_bot)

my_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
button1 = KeyboardButton(text="/vote")
my_kb.add(button1)

my_inline_kb = InlineKeyboardMarkup(row_width=2)
like_button = InlineKeyboardButton(text="❤️", callback_data="like")
dislike_button = InlineKeyboardButton(text="👎", callback_data="dislike")
my_inline_kb.add(like_button, dislike_button)


async def on_startup(_):
    print("Бот успешно запущен!")


@my_disp.message_handler(commands="start")
async def start_answer(message: types.Message):
    await message.delete()
    await my_bot.send_message(text="Добро пожаловать в бот!", chat_id=message.chat.id, reply_markup=my_kb)


@my_disp.message_handler(commands="vote")
async def vote_command(message: types.Message):
    await message.delete()
    await my_bot.send_photo(chat_id=message.chat.id,
                            photo="https://tripmydream.cc/travelhub/travel/blocks/20/5779/block_205779.jpg?v1",
                            caption="Вам нравится это фото?",
                            reply_markup=my_inline_kb)


@my_disp.callback_query_handler()
async def callback_handler(callback_object: types.CallbackQuery):
    if callback_object.data == "like":
        await callback_object.answer("Вам понравилась эта фотография")
    await callback_object.answer("Вам не понравилась эта фотография")

if __name__ == "__main__":
    executor.start_polling(my_disp, skip_updates=True, on_startup=on_startup)
