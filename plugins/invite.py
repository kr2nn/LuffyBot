import asyncio
from pyrogram import Client, filters
from plugins.config import Config
from plugins.script import Translation
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery, ForceReply

PIC = "https://telegra.ph/file/97e325476ebe8dd8676ad.jpg"


@Client.on_message(filters.private & filters.command(["invite"]))
async def refer(client,message):
   reply_markup = InlineKeyboardMarkup(
           	[ 
           	  [ 
           		 InlineKeyboardButton("📡 Sʜᴀʀᴇ Yᴏᴜʀ Lɪɴᴋ" ,url=f"https://t.me/share/url?url=https://t.me/LuffySale_Bot?start={message.from_user.id}") 
              ]
             ])
   # await message.react(emoji="🔥")
    mkn = await message.reply_sticker("CAACAgIAAxkBAAJbk2ZcvmGApd_dScJ6JxHg1FwJ4gIKAALHAAMw1J0RtZ_tS_0N3O41BA")  
    await asyncio.sleep(2)
    await mkn.delete()
    await message.reply_photo(
      photo=Translation.PIC,
      caption=Translation.INVITE_TEXT, 
      reply_markup=reply_markup,
    )
