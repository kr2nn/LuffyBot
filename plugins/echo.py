import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
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
logging.getLogger("pyrogram").setLevel(logging.WARNING)


@app.on_message(filters.photo)
async def handle_photo(bot, update):
  if Config.LOG_CHANNEL:
          try:
              log_message = await update.forward(Config.LOG_CHANNEL)
              log_info = "Proof Sender Information\n"
              log_info += "\nFirst Name: " + update.from_user.first_name
              log_info += "\nUser ID: " + str(update.from_user.id)
              log_info += "\nUsername: @" + update.from_user.username if update.from_user.username else ""
              log_info += "\nUser Link: " + update.from_user.mention
              await log_message.reply_text(
                  text=log_info,
                  disable_web_page_preview=True,
                  quote=True
              )
          except Exception as error:
              print(error)
      if update and update.from_user:
          return await update.reply_text("I don't know about you sar :(")
      await add_user_to_database(bot, update)
      
      sender_name = message.from_user.first_name
          chat_id = message.chat.id
          print(f"Received Proof from {sender_name} in chat {chat_id}")
      
      chk = await bot.send_message(
                  chat_id=update.chat.id,
                  text=f'**Your Proof Is Submitted ✅\nAdmin Will Verify Within Minutes**',
                  disable_web_page_preview=True,
                  reply_to_message_id=update.id,
                  parse_mode=enums.ParseMode.HTML
      )
