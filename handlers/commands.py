from aiogram import types, Dispatcher
import os
from config import bot


async def start_handler(message:types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Hello {message.from_user.first_name}!\n"
                           f"Your telegram id - {message.from_user.id}\n")

async def meme_handler(message:types.Message):
    photo_pass = os.path.join("media", "hqdefault.jpg")
    with open(photo_pass, "rb") as photo:
        await message.answer_photo(photo = photo, caption= "BUBUBU, I can't see, BUBUBU")

def register_commands_handlers(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands = "start")
    dp.register_message_handler(meme_handler, commands = "BUBUBU")