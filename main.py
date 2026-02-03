import os
from threading import Thread
from flask import Flask

from app import app as bot_app
from utils import LOGGER
from core import start_message
from core.mongo import MONGO_CLIENT 

# Fake Web Server (Render ke liye)
web = Flask(__name__)

@web.route("/")
def home():
    return "Bot is running!"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    web.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    LOGGER.info("Bot Successfully Started! ")

    # Web server start (Render ke liye)
    Thread(target=run_web).start()

    # Telegram bot start
    bot_app.run()
