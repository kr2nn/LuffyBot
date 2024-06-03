import traceback, datetime, asyncio, string, random, time, os, aiofiles, aiofiles.os
from pyrogram import filters
from pyrogram import Client
from plugins.script import Translation
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid
from plugins.database.database import db
from plugins.config import Config

@Client.on_message(filters.private & filters.command("status"))
async def status(bot, update):
    total_users = await db.total_users_count()
    text = "**Bot Status**\n"
    text += f"\n**Total Users:** `{total_users}`"
    await update.reply_text(
        text=text,
        quote=True,
        disable_web_page_preview=True
    )
@Client.on_message(filters.command('stats') & filters.incoming)
async def get_ststs(bot, message):
    rju = await message.reply('<b>Pʟᴇᴀꜱᴇ Wᴀɪᴛ...</b>')
    total_users = await db.total_users_count()
    size = await db.get_db_size()
    free = 536870912 - size
    size = get_size(size)
    free = get_size(free)
    await rju.edit(Transaction.STATUS_TXT.format(total_users, size, free))
