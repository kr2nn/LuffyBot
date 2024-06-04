import os
from plugins.functions.display_progress import progress_for_pyrogram, humanbytes
from plugins.config import Config
from plugins.script import Translation
from pyrogram import Client, types, enums   
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, Message, CallbackQuery, ForceReply
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
       await update.message.delete()
    # Send the photo
       await bot.send_photo(
           chat_id=update.message.chat.id,
           photo=Translation.PAYMENT_QR,  # Assuming PAYMENT_QR contains the file ID or file path of the photo
           caption=Translation.QR_TEXT,  # Caption for the photo
           reply_markup=Translation.BUTTONS  # Optional: Add reply markup if needed
       )
    elif update.data == "demopic":
       await bot.edit_message_media(
           media=types.InputMediaPhoto(Translation.PAYMENT_QR), 
           caption=Translation.QR_TEXT, 
           reply_markup=Translation.BUTTONS
       )                                       
    elif "close" in update.data:
        await update.message.delete(True)
