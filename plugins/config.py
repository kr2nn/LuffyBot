import os

import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

class Config(object):
    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6526539974:AAEN2s80bUgYi-0fRG72E9_M2L4otEBHuvA")
    
    API_ID = int(os.environ.get("API_ID", "4888076"))
    
    API_HASH = os.environ.get("API_HASH", "8b9b8214d84305d5ba8042c93575ea84")

    DOWNLOAD_LOCATION = "./DOWNLOADS"

    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")

    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://UploadLinkToFileBot:UploadLinkToFileBot@cluster0.1gybihh.mongodb.net/?retryWrites=true&w=majority")
    
    SESSION_NAME = os.environ.get("SESSION_NAME", "LuffySale_Bot")
    
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002070853757"))
    
    LOGGER = logging

    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002070853757")

    OWNER_ID = int(os.environ.get("OWNER_ID", "6807518752"))
    
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "LuffySale_Bot")
                                  
