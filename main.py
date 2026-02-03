import os
from threading import Thread
from flask import Flask

from app import app as bot_app   # 🔥 bot app ko rename kiya
from utils import LOGGER
from core import start_message
from core.mongo import MONGO_CLIENT 

# Flask web server (Render ke liye)
web_app = Flask(__name__)

@web_app.route("/")
def home():
    return "Bot is running!"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    web_app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    LOGGER.info("Bot Successfully Started!")

    # Flask server start (Render port binding)
    Thread(target=run_web).start()

    # Telegram bot start
    bot_app.run()
