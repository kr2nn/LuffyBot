from pyrogram import Client, filters
from pyrogram.types import InputMediaPhoto

# Define a command handler
@Client.on_message(filters.command(["send_media_group"]) & filters.private)
async def send_media_group(bot, update):
    # Prepare a list of media objects (photos in this example)
    media_group = [
        {"type": "photo", "media": "https://telegra.ph/file/f7f8409bef77fcba2b3c1.jpg"},
        {"type": "photo", "media": "https://telegra.ph/file/5097e8973b5c83d51794f.jpg"},
        {"type": "photo", "media": "https://telegra.ph/file/dba42aa7eff08c3b3bbc9.jpg"},
        # Add more media objects as needed
    ]

    # Send the media group
    await bot.send_media_group(update.chat.id, media=media_group)
