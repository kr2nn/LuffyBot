import os

import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

class Config(object):
    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    
    API_ID = int(os.environ.get("API_ID", ""))
    
    API_HASH = os.environ.get("API_HASH", "")

    DOWNLOAD_LOCATION = "./DOWNLOADS"

    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")

    DATABASE_URL = os.environ.get("DATABASE_URL", "")
    
    SESSION_NAME = os.environ.get("SESSION_NAME", "")
    
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))
    
    PAYMENT_LOG = int(os.environ.get("PAYMENT_LOG", ""))
    
    LOGGER = logging

    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")

    OWNER_ID = int(os.environ.get("OWNER_ID", ""))
    
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
                                  
