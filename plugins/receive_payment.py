from pyrogram import Client, filters
from plugins.config import Config
from plugins.script import Translation
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.private & filters.photo)
async def check_photo(c, m):
    await m.reply_text("**Your Proof Is Submitted Admin Will Verify With In Minutes**")
    button = [[
        InlineKeyboardButton("Accept", callback_data=f"accept_{m.from_user.id}"),
        InlineKeyboardButton("Decline", callback_data=f"decline_{m.from_user.id}")
    ]]
    await c.send_photo(chat_id=Config.OWNER_ID, photo=m.photo.file_id, caption=Translation.INFO_TXT, reply_markup=InlineKeyboardMarkup(button))
