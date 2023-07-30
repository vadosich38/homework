from aiogram import types, Dispatcher, Bot, executor
from config import API_KEY


my_bot = Bot(API_KEY)
my_disp = Dispatcher(my_bot)
help_text = """
<b>/command1</b> – <i>описание первой команды</i>
<b>/command2</b> – <i>описание второй команды</i>
<b>/command3</b> – <i>описание третей команды</i>
<b>/command4</b> – <i>описание четвертой команды</i>
<b>/command5</b> – <i>описание пятой команды</i>
"""


async def on_startup(_):
    print("Я запустился!")


@my_disp.message_handler(commands="help")
async def answer(message: types.Message):
    await message.answer(help_text, parse_mode="HTML")
    await message.delete()


@my_disp.message_handler(content_types=['sticker'])
async def get_sticker_id(message: types.Message):
    sticker_id = message.sticker.file_id
    await message.reply(sticker_id)


@my_disp.message_handler()
async def count_emoji(message: types.Message):
    count = str(message).count("✅")
    await message.reply("В этом сообщениие {} emoji ✅".format(count))


if __name__ == "__main__":
    executor.start_polling(my_disp, on_startup=on_startup)
