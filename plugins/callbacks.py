import os
from plugins.functions.display_progress import progress_for_pyrogram, humanbytes
from plugins.config import Config
from plugins.script import Translation
from pyrogram import Client, types   
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery, ForceReply
from plugins.database.database import db
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


@Client.on_callback_query()
async def button(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=Translation.START_TEXT.format(update.from_user.mention),
            reply_markup=Translation.START_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "premium":
        await update.message.edit_text(
            text=Translation.DETAILS_TEXT.format(update.from_user.mention),
            reply_markup=Translation.PREMIUM_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "payment":
      await update.message.edit_text(
        text=Translation.QR_TEXT,
        reply_markup=Translation.BUTTONS,
        disable_web_page_preview=True
      )
    elif "close" in update.data:
        await update.message.delete(True)
