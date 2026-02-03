import os
from threading import Thread
from flask import Flask

from app import app as bot_app
from utils import LOGGER
from core import start_message
from core.mongo import MONGO_CLIENT 

# Flask server for Render
flask_app = Flask(__name__)

@flask_app.route("/")
def home():
    return "Bot is running!"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    flask_app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    LOGGER.info("Bot Successfully Started!")

    # Start Flask server
    Thread(target=run_flask).start()

    # Start Telegram bot
    bot_app.run()
