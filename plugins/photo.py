from pyrogram import Client, filters
from pyrogram.types import InputMediaPhoto

# Define a command handler
@app.on_message(filters.command("send_photos"))
def send_photos(client, message):
    # List of photo file paths
    photos = ["https://telegra.ph/file/f7f8409bef77fcba2b3c1.jpg", "https://telegra.ph/file/5097e8973b5c83d51794f.jpg", "https://telegra.ph/file/dba42aa7eff08c3b3bbc9.jpg"]

    # Convert file paths to InputMediaPhoto objects
    media = [InputMediaPhoto(photo) for photo in photos]

    # Send the media group
    client.send_media_group(message.chat.id, media)
