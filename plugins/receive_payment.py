from pyrogram import Client, filters, enums
from plugins.config import Config
from plugins.script import Translation
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.private & filters.photo)
async def check_photo(c, m):
    message = m
    ff = m.from_user
    md = m.reply_to_message
    await m.reply_text("**Your Proof Is Submitted ✅\nAdmin Will Verify With In Minutes**")
    button = [[
        InlineKeyboardButton("Accept", callback_data=f"accept_{m.from_user.id}"),
        InlineKeyboardButton("Decline", callback_data=f"decline_{m.from_user.id}")
    ]]
    await c.send_photo(chat_id=Config.OWNER_ID, photo=m.photo.file_id, caption=Translation.INFO_TXT.format(id=ff.id, dc=ff.dc_id, n=ff.first_name, u=ff.username), reply_markup=InlineKeyboardMarkup(button), quote=True,
               parse_mode=enums.ParseMode.HTML, disable_notification=True)
