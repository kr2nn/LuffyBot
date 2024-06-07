from pyrogram import Client, filters, enums
from plugins.config import Config
from plugins.script import Translation
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.private & filters.photo)
async def check_photo(c, m):
    if Config.LOG_CHANNEL:
        try:
            log_message = await m.forward(Config.LOG_CHANNEL)
            log_info = "Message Sender Information\n"
            log_info += "\nFirst Name: " + update.from_user.first_name
            log_info += "\nUser ID: " + str(update.from_user.id)
            log_info += "\nUsername: @" + update.from_user.username if update.from_user.username else ""
            log_info += "\nUser Link: " + update.from_user.mention
            await log_message.reply_text(
                text=log_info,
                disable_web_page_preview=True,
                quote=True
            )
            
    ff = m.from_user
    await m.reply_text("**Your Proof Is Submitted ✅\nAdmin Will Verify With In Minutes**")
    button = [[
        InlineKeyboardButton("Accept", callback_data=f"accept_{m.from_user.id}"),
        InlineKeyboardButton("Decline", callback_data=f"decline_{m.from_user.id}")
    ]]
    await c.send_photo(chat_id=Config.OWNER_ID, photo=m.photo.file_id, caption=Translation.PAYMENT_INFO.format(id=ff.id, n=ff.first_name, u=ff.username), reply_markup=InlineKeyboardMarkup(button), parse_mode=enums.ParseMode.HTML)
