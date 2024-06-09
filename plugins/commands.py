import pyrogram, asyncio, random, time, os
import time
import psutil
import shutil
import string
import asyncio
from pyrogram import Client, filters, enums
from asyncio import TimeoutError
from pyrogram.errors import MessageNotModified
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery, ForceReply
from plugins.config import Config
from plugins.script import Translation
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from plugins.database.add import add_user_to_database
from plugins.functions.forcesub import handle_force_subscribe


@Client.on_message(filters.command(["start"]) & filters.private)
async def start(bot, update):
    if not update.from_user:
        return await update.reply_text("I don't know about you sar :(")
    await add_user_to_database(bot, update)
    await bot.send_message(
        Config.LOG_CHANNEL,
           f"#NEW_USER: \n\n__**○ New User :**__ [{update.from_user.first_name}](tg://user?id={update.from_user.id})\n __**○ Started :**__ @{Config.BOT_USERNAME}!!\n__**○ ID :**__ `{update.from_user.id}`\n__**○ link :**__ <code>https://t.me/{update.from_user.username}</code>"
    )
    
    if Config.UPDATES_CHANNEL:
      fsub = await handle_force_subscribe(bot, update)
      if fsub == 400:
        return       
    # Define the list of photo file IDs to be sent
    photo_file_ids = [
        "https://telegra.ph/file/f7f8409bef77fcba2b3c1.jpg",  # Replace with actual file IDs
        "https://telegra.ph/file/5097e8973b5c83d51794f.jpg"
        # Add more file IDs as needed
    ]

    # Send the media group (multiple photos) to the user
    await bot.send_media_group(
        chat_id=update.chat.id,
        media=photo_file_ids,
        caption=Translation.START_TEXT,
        reply_markup=Translation.START_BUTTONS
    )
