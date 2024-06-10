from pyrogram import Client, filters, enums
from plugins.config import Config
from plugins.script import Translation
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.private & filters.photo)
async def check_photo(c, m):
    ff = m.from_user
    await m.reply_text("**Your Proof Is Submitted ✅\nAdmin Will Verify With In Minutes**")
    button = [[
        InlineKeyboardButton("Accept", callback_data=f"accept_{m.from_user.id}"),
        InlineKeyboardButton("Decline", callback_data=f"decline_{m.from_user.id}")
    ]]
    await c.send_photo(chat_id=Config.LOG_CHANNEL, photo=m.photo.file_id, caption=Translation.PAYMENT_INFO.format(id=ff.id, n=ff.first_name, u=ff.username), reply_markup=InlineKeyboardMarkup(button), parse_mode=enums.ParseMode.HTML)
    await c.send_message(chat_id=Config.LOG_CHANNEL, text=Translation.PAYMENT_USER.format(id=ff.id, n=ff.first_name, u=ff.username))
