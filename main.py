import os
from dotenv import load_dotenv
from pyrogram import Client


load_dotenv()

Bot = Client(
    "QR Code Bot",
    bot_token=os.environ.get("BOT_TOKEN"),
    api_id=int(os.environ.get("API_ID")),
    api_hash=os.environ.get("API_HASH"),
    mongodb_uri=(os.environ.get.("MONGODB_URI")
    plugins=dict(root="plugins")
)

Bot.run()
