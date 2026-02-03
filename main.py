import os
from app import app
from utils import LOGGER
from core import start_message
from core.mongo import MONGO_CLIENT 

if __name__ == "__main__":
    LOGGER.info("Bot Successfully Started! ")
    
    port = int(os.environ.get("PORT", 10000))  # Render ka port
    app.run(host="0.0.0.0", port=port)
