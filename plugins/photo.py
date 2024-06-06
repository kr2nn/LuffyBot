from pyrogram import Client, filters
from pyrogram.types import InputMediaPhoto

@Client.on_message(filters.command(["send_multiple_photos"]) & filters.private)
async def send_multiple_photos(bot, update):
    # Define the chat ID where you want to send the photos
    chat_id = update.chat.id

    # Define a list of photo file IDs or URLs
    photos = [
        "https://telegra.ph/file/f7f8409bef77fcba2b3c1.jpg",
        "https://telegra.ph/file/5097e8973b5c83d51794f.jpg",
        "https://telegra.ph/file/dba42aa7eff08c3b3bbc9.jpg",
        # Add more photo file IDs or URLs as needed
    ]

    # Send the photos as a media group
    await bot.send_media_group(
        chat_id=chat_id,
        media=[
            {"type": "photo", "media": photo} for photo in photos
        ]
    )
