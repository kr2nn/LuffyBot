from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ForceReply
from pyrogram import Client, filters
from pyrogram.types import Message



# Define handlers for different types of messages
@Client.on_message(filters.video)
async def handle_video(bot, message: Message):
    # Handle video message
    await message.reply_text(f"**Video File ID:**\n `{message.video.file_id}`")

@Client.on_message(filters.sticker)
async def handle_sticker(bot, message: Message):
    # Handle sticker message
    await message.reply_text(f"**Sticker File ID:**\n `{message.sticker.file_id}`")

@Client.on_message(filters.photo)
async def handle_photo(bot, message: Message):
    # Handle photo message
    await message.reply_text(f"**Photo file ID:**\n `{message.photo.file_id}`")

@Client.on_message(filters.document)
async def handle_document(bot, message: Message):
    # Handle document message
    await message.reply_text(f"**Document File ID:**\n `{message.document.file_id}`")

# Define handlers for voice and audio messages
@Client.on_message(filters.voice)
async def handle_voice(bot, message: Message):
    # Handle voice message
    await message.reply_text(f"**Voice File ID:**\n `{message.voice.file_id}`")

@Client.on_message(filters.audio)
async def handle_audio(bot, message: Message):
    # Handle audio message
    await message.reply_text(f"**Audio File ID:**\n `{message.audio.file_id}`")
    
