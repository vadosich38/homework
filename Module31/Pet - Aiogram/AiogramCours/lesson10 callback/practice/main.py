from aiogram import types, executor, Bot, Dispatcher
from config import API_KEY
from keyboards import my_kb, my_inline_kb
import random
from data import HELP_TEXT, DESCRIPTION_TEXT, photos

my_bot = Bot(API_KEY)
my_disp = Dispatcher(my_bot)
photo_data = tuple()
temp_photo_data = photo_data


async def on_startup(_):
    print("Бот успешно запущен!")


def random_photo(photos_dict: dict) -> tuple:
    random_choice = random.randint(1, 3)
    if random_choice == 1 and len(photos_dict["not_marked"]) > 0:
        list_name = "not_marked"
        random_choice = random.randint(0, len(photos_dict["not_marked"])-1)
        return photos_dict["not_marked"][random_choice], list_name, random_choice
    elif random_choice == 2 and len(photos_dict["liked"]) > 0:
        list_name = "liked"
        random_choice = random.randint(0, len(photos_dict["liked"])-1)
        return photos_dict["liked"][random_choice], list_name, random_choice
    elif random_choice == 3 and len(photos_dict["disliked"]) > 0:
        list_name = "disliked"
        random_choice = random.randint(0, len(photos_dict["disliked"])-1)
        return photos_dict["disliked"][random_choice], list_name, random_choice
    else:
        return random_photo(photos_dict=photos)


@my_disp.message_handler(commands="start")
async def start_answer(message: types.Message):
    await message.delete()
    await my_bot.send_message(text="Добро пожаловать в нашего БОТА",
                              chat_id=message.chat.id,
                              reply_markup=my_kb)


@my_disp.message_handler(commands="funny_sticker")
async def start_answer(message: types.Message):
    await message.delete()
    await my_bot.send_sticker(chat_id=message.chat.id,
                              sticker="CAACAgIAAxkBAAEJolhkqVoEYSpStujs1svLjjO3dcf07wACXxEAAjyzxQfvu5gKYw7MZS8E")


@my_disp.message_handler(commands="funny_emoji")
async def start_answer(message: types.Message):
    await message.delete()
    await my_bot.send_message(chat_id=message.chat.id,
                              text="💩")


@my_disp.message_handler(commands="location")
async def start_answer(message: types.Message):
    await message.delete()
    await my_bot.send_location(chat_id=message.chat.id,
                               longitude=random.uniform(0.0, 90.0),
                               latitude=random.uniform(0.0, 90.0))


@my_disp.message_handler(commands="favorite")
async def start_answer(message: types.Message):
    await message.delete()
    if len(photos["liked"]) > 0:
        await my_bot.send_message(text="Вам нравятся эти города:",
                                  chat_id=message.chat.id)
        for i_photo in photos["liked"]:
            await my_bot.send_photo(chat_id=message.chat.id,
                                    photo=i_photo)
    else:
        await my_bot.send_message(text="У вас еще нет любимых городов",
                                  chat_id=message.chat.id)


@my_disp.message_handler(commands="not_favorite")
async def start_answer(message: types.Message):
    await message.delete()
    if len(photos["disliked"]) > 0:
        await my_bot.send_message(text="Вам не нравятся эти города:",
                                  chat_id=message.chat.id)
        for i_photo in photos["disliked"]:
            await my_bot.send_photo(chat_id=message.chat.id,
                                    photo=i_photo)
    else:
        await my_bot.send_message(text="У вас еще нет нелюбимых городов",
                                  chat_id=message.chat.id)


@my_disp.message_handler(commands="description")
async def description_answer(message: types.Message):
    await message.delete()
    await my_bot.send_message(text=DESCRIPTION_TEXT,
                              chat_id=message.chat.id)


@my_disp.message_handler(commands="help")
async def help_answer(message: types.Message):
    await message.delete()
    await my_bot.send_message(text=HELP_TEXT,
                              chat_id=message.chat.id,
                              parse_mode="HTML")


@my_disp.message_handler(commands="send_photo")
async def send_photo_answer(message: types.Message):
    global photo_data #! нежелательно использовать global в функциях
    global temp_photo_data #! нежелательно использовать global в функциях
    await message.delete()

    while True:
        photo_data = random_photo(photos_dict=photos)
        if isinstance(photo_data, tuple) and photo_data != temp_photo_data:
            break
    temp_photo_data = photo_data
    await my_bot.send_photo(chat_id=message.chat.id,
                            photo=photo_data[0],
                            caption="Вам нравится этот город?",
                            reply_markup=my_inline_kb)


@my_disp.callback_query_handler()
async def callback_vote(callback_object: types.CallbackQuery):
    global photo_data
    global temp_photo_data

    if callback_object.data == "like":
        photos["liked"].append(photos[photo_data[1]].pop(photo_data[2]))
        return await callback_object.answer(text="Вам понравился этот город! ❤️")
    elif callback_object.data == "dislike":
        photos["disliked"].append(photos[photo_data[1]].pop(photo_data[2]))
        await callback_object.answer(text="Вам не понравился этот город! 💩")
    elif callback_object.data == "location":
        await callback_object.answer(text="Отправляю вам рандомную локацию")
        await my_bot.send_location(chat_id=callback_object.message.chat.id,
                                   longitude=random.uniform(0.0, 90.0),
                                   latitude=random.uniform(0.0, 90.0))
    elif callback_object.data == "next_photo":
        while True:
            photo_data = random_photo(photos_dict=photos)
            if isinstance(photo_data, tuple) and photo_data != temp_photo_data:
                await callback_object.message.edit_media(types.InputMedia(media=photo_data[0],
                                                                          types="photo",
                                                                          caption="Вам нравится этот город?"),
                                                         reply_markup=my_inline_kb)
                break


if __name__ == "__main__":
    executor.start_polling(dispatcher=my_disp,
                           skip_updates=True,
                           on_startup=on_startup)
