import os

import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

class Config(object):
    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7477234408:AAGI7iXDHrBU9VGGUnAl0IEKSBrQ_IrdupY")
    
    API_ID = int(os.environ.get("API_ID", "29478734"))
    
    API_HASH = os.environ.get("API_HASH", "8bd53e36eceada3329fbe46d9b961d1f")

    DOWNLOAD_LOCATION = "./DOWNLOADS"

    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")

    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://nikzgod:nikzgod@cluster0.lqn4wau.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
    SESSION_NAME = os.environ.get("SESSION_NAME", "LuffySale_Bot")
    
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002142928842"))
    
    PAYMENT_LOG = int(os.environ.get("PAYMENT_LOG", "-1002224622658"))
    
    LOGGER = logging

    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002072970024")

    OWNER_ID = int(os.environ.get("OWNER_ID", "6807518752"))
    
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "LuffySale_Bot")
                                  
