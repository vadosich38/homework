from aiogram import types, Bot, Dispatcher, executor
from config import API_KEY
from func import find_substring
import requests


my_bot = Bot(API_KEY)
my_disp = Dispatcher(my_bot)


async def on_startup(_):
    print("Бот успешно запущен!")


@my_disp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.delete()
    await message.answer(text="Привет!  🤝\nЧтобы скачать видео из TikTok без watermark просто пришли мне ссылку "
                              "на видео  📸")


@my_disp.message_handler()
async def send_video(message: types.Message):
    req = requests.get(message.text)
    str_search = 'content="snssdk1233://aweme/detail/'

    link_download = "https://tikcdn.io/ssstik/" + find_substring(string=req.text, sub_string=str_search)

    await message.reply(text=f"Нажми на ссылку чтобы скачать видео\n\n➡️  {link_download}  ⬅️")


if __name__ == "__main__":
    executor.start_polling(dispatcher=my_disp,
                           skip_updates=True,
                           on_startup=on_startup)
