from pyrogram import Client, filters

@Client.on_message(filters.command("stickerid") & filters.private)
async def stickerid(bot, message):
    nikz_msg = await bot.ask(stickerid = message.from_user.id, text = "Now Send Me Your Sticker")
    if nikz_msg.sticker:
        await nikz_msg.reply_text(f"**Sticker ID is**  \n `{s_msg.sticker.file_id}` \n \n ** Unique ID is ** \n\n`{s_msg.sticker.file_unique_id}`")
    else: 
        await nikz_msg.reply_text("Oops !! Not a sticker file")
