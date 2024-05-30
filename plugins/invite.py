from pyrogram import Client, filters
from plugins.config import Config
from plugins.script import Translation
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery, ForceReply

PIC = "https://telegra.ph/file/97e325476ebe8dd8676ad.jpg"


@Client.on_message(filters.private & filters.command(["invite"]))
async def refer(client,message):
   # await message.react(emoji="🔥")
    await message.reply_photo(
      photo=Translation.PIC,
      caption=Translation.INVITE_TEXT, 
      reply_markup=Translation.BUTTONS
    )
