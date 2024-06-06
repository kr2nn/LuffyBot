import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import random
import numpy
import os
from PIL import Image
import time

# the Strings used for this "thing"
from plugins.script import Translation
from pyrogram import Client

from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
logging.getLogger("pyrogram").setLevel(logging.WARNING)
from pyrogram import filters
from plugins.functions.help_Nekmo_ffmpeg import take_screen_shot
import psutil
import shutil
import string
import asyncio
from asyncio import TimeoutError
from pyrogram.errors import MessageNotModified
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery, ForceReply
from plugins.functions.forcesub import handle_force_subscribe
from plugins.database.database import db
from plugins.config import Config
from plugins.database.add import add_user_to_database
from plugins.settings.settings import *

@Client.on_message(filters.photo)
async def save_photo(bot, update):
  if not update.from_user:
        return await update.reply_text("I don't know about you sar :(")
    await add_user_to_database(bot, update)
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
    # received single photo
    download_location = os.path.join(
        Config.DOWNLOAD_LOCATION,
        str(update.from_user.id) + ".jpg"
    )
    await bot.download_media(
        message=update,
        file_name=download_location
    )
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.PROOF_UPLOAD,
        reply_to_message_id=update.id
    )
    await db.set_thumbnail(update.from_user.id, thumbnail=update.photo.file_id)
