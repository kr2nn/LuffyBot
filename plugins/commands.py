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
    mkn = await update.reply_sticker("CAACAgIAAxkBAAJbimZctsnmFpfbGwHGEKIRBKId82e4AAJuAAOtZbwUmdKVOaHouYc1BA")  
    await asyncio.sleep(2)
    await mkn.delete()
    await update.reply_photo(
        photo=Translation.PIC,
        caption=Translation.START_TEXT.format(update.from_user.mention),
       # disable_web_page_preview=True,
        reply_markup=Translation.START_BUTTONS
    )


