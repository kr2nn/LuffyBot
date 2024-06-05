import os, random
from plugins.functions.display_progress import progress_for_pyrogram, humanbytes
from plugins.config import Config
from plugins.script import Translation
from plugins.info import PICS, QR_PIC
from pyrogram import Client, types, enums   
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, Message, CallbackQuery, ForceReply
from pyrogram.errors import FloodWait, UserIsBlocked, MessageNotModified, PeerIdInvalid
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
    elif update.data == "demopic":
        await update.send_photo(
            chat_id=update.message.chat.id,
            photo=Translation.DEMO_PIC,  # Assuming PAYMENT_QR contains the file ID or file path of the photo
            caption=Translation.DEMO_TEXT  # Caption for the photo
       )
    elif update.data == "payment":
        buttons = [[
        InlineKeyboardButton('Sᴇɴᴛ Sᴄʀᴇᴇɴꜱʜᴏᴛ 📲', user_id='6807518752')           
        ],[
        InlineKeyboardButton('« Bᴀᴄᴋ', callback_data='premium'),       
        InlineKeyboardButton('✘ Cʟᴏsᴇ', callback_data='close')
        ]]
        await update.edit_message_media(InputMediaPhoto(random.choice(QR_PIC), Translation.QR_TEXT, enums.ParseMode.HTML), reply_markup=InlineKeyboardMarkup(buttons))
    elif "close" in update.data:
        await update.message.delete(True)
