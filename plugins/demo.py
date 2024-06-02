import os
import time
import psutil
import shutil
import string
import asyncio
import aiohttp
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


@Client.on_message(filters.command(["demo"]) & filters.private)
async def videosdemo(bot, update):
    if not update.from_user:
        return await update.reply_text("I don't know about you sar :(")
    await add_user_to_database(bot, update)
    await bot.send_message(
        Config.LOG_CHANNEL,
           f"**#Dᴇᴍᴏ Sᴇɴᴅᴇʀ:** \n\n__**○ New User :**__ [{update.from_user.first_name}](tg://user?id={update.from_user.id})\n __**○ Started :**__ @{Config.BOT_USERNAME}!!\n__**○ ID :**__ `{update.from_user.id}`\n__**○ link :**__ <code>https://t.me/{update.from_user.username}</code>"
    )
    
    if Config.UPDATES_CHANNEL:
      fsub = await handle_force_subscribe(bot, update)
      if fsub == 400:
        return
    await update.reply_video(
        video="https://telegra.ph/file/ad54fa01434e211d79125.mp4",
        caption=Translation.ADS_TEXT
    )
    await update.reply_video(
        video="https://telegra.ph/file/915721b8d204fab00c270.mp4",
        caption=Translation.ADS_TEXT
    )
    await update.reply_video(
        video="https://telegra.ph/file/fb4eebce9e4a5f50f7e25.mp4",
        caption=Translation.ADS_TEXT
    )
    await update.reply_video(
        video="https://telegra.ph/file/e0526d0e6ae8c0a1473de.mp4",
        caption=Translation.ADS_TEXT
    )
    await update.reply_video(
        video="https://telegra.ph/file/ce899ad82ae6012db8923.mp4",
        caption=Translation.ADS_TEXT
    )
    await update.reply_video(
        video="https://telegra.ph/file/69b0e51312b1a298ec0dc.mp4",
        caption=Translation.ADS_TEXT
    )
    await update.reply_video(
        video="https://telegra.ph/file/1d80b5d35c795e8485b9d.mp4",
        caption=Translation.ADS_TEXT
    )
    await update.reply_video(
        video="https://telegra.ph/file/1b80f5ba4a2040cb76cd7.mp4",
        caption=Translation.ADS_TEXT
    )
