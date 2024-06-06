#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("28293310", default=None, cast=int)
API_HASH = config("1e5bae7865a03ef0a7948012de2952b2", default=None)
BOT_TOKEN = config("7479725873:AAEEXBCkechEtt3qDu4_M9Ve7DEUbp34hjw", default=None)
SESSION = config("BQGqa00AjLefyHWkJB9WYYZSOA42WCVmgXb3632h-5TFbef7340r1mFUcQfzQ0N-FeaQP01755sSHPr6W_vYGUco9Z21Qt3jlinIZIF73b05kbfVVAWSx-LY1RJF7LyrLYAhHpg7SbJLXsHaL7LoRQSYGODCNWgN2sTd_QnJ4Tz8oTSZGTTms1ZrTfXRyE9LEBxG-70mcY_2PSi2pWiUthGNX4EAd84TqIjjTJ6w659SPmFLfjBWe1bBDX4sfp4jLbkXv7AqaKMG0IFsDAAI4i0UTpLN12_aYeGSIoDg4xx_ifUL359rJrC22nYCec7uiHoYdQRu3cBgYencSwZNTXWkD3M6bwAAAABXF31LAA", default=None)
FORCESUB = config("blublubaba", default=None)
AUTH = config("1461157195", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
