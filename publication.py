import telegram
import os
from dotenv import load_dotenv

load_dotenv()
tg_token = os.getenv("TELEGRAM_TOKEN")
chat_id = os.getenv("CHAT_ID")

bot = telegram.Bot(token=tg_token)
bot.send_message(chat_id=chat_id, text="Test")
