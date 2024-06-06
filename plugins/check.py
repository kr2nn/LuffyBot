from pyrogram import Client, filters
from plugins.config import Config
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply


@Client.on_message(filters.command(["video"]) & filters.private)
async def video(bot, update):
  awit update.reply_video(
    
  )
