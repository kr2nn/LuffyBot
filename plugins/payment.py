import os
import time
import psutil
import shutil
import string
import asyncio
from pyrogram import Client, filters
from asyncio import TimeoutError
from pyrogram.errors import MessageNotModified
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery, ForceReply
from plugins.config import Config
from plugins.script import Translation
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from plugins.database.add import add_user_to_database
from plugins.functions.forcesub import handle_force_subscribe


@Client.on_message(filters.command(["payment"]) & filters.private)
async def start(bot, update):
    if not update.from_user:
        return await update.reply_text("I don't know about you sar :(")
    await add_user_to_database(bot, update)
    await bot.send_message(
        Config.LOG_CHANNEL,
           f"#PAYMENT💰 : \n\nPay Button Clicked [{update.from_user.first_name}](tg://user?id={update.from_user.id})\n 💰 Payment @{Config.BOT_USERNAME}!!"
    )
    
    if Config.UPDATES_CHANNEL:
      fsub = await handle_force_subscribe(bot, update)
      if fsub == 400:
        return
    await update.reply_photo(
        photo=Translation.PAYMENT_QR,
        caption=Translation.QR_TEXT.format(update.from_user.mention),
       # disable_web_page_preview=True,
        reply_markup=Translation.BUTTONS
    )
