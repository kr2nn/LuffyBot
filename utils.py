import logging, os, re, asyncio, requests, aiohttp 
from pyrogram import filters, enums
from database.database import db

# temp db for banned 
class temp(object):
    BANNED_USERS = []
    BANNED_CHATS = []
    CURRENT = 0
    CANCEL = False
    MELCOW = {}
    U_NAME = None
    B_NAME = None
    SETTINGS = {}
    GP_BUTTONS = {}
    PM_BUTTONS = {}
    PM_SPELL = {}
    GP_SPELL = {}
