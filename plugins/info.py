import re, time
from os import environ
from plugins.script import Translation

PICS = (environ.get('PICS' ,'https://telegra.ph/file/13138bb072d6ae54386d4.jpg')).split()

PIC = (environ.get('PICS' ,'https://telegra.ph/file/3e68bfd9242aefd68cb70.jpg')).split()

QR_PIC = (environ.get('QR_PIC' ,'https://telegra.ph/file/4acfd5a112e10ba0bf34f.jpg')).split()
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6807518752').split()]
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', 0))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
PROTECT_CONTENT = is_enabled(environ.get('PROTECT_CONTENT', "False"), False)
PUBLIC_FILE_STORE = is_enabled(environ.get('PUBLIC_FILE_STORE', "True"), True)

