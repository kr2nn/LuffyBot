import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
from plugins.config import Config

from pyrogram import Client, filters
logging.getLogger("pyrogram").setLevel(logging.WARNING)


if __name__ == "__main__" :

    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    plugins = dict(root="plugins")
    app = Client(
        "LuffyBot",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        plugins=plugins)

   # Start the bot
print("♻️ I AM ALIVE  @LuffyBot ♻️")
app.run()

