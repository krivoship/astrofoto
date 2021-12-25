import telegram
import os
from random import choice
from dotenv import load_dotenv

load_dotenv()
tg_token = os.getenv("TELEGRAM_TOKEN")
chat_id = os.getenv("CHAT_ID")

images = os.listdir('./images')
random_image = choice(images)
image_path = os.path.join('./images', random_image)

bot = telegram.Bot(token=tg_token)
bot.send_photo(chat_id=chat_id, photo=open(image_path, 'rb'))
