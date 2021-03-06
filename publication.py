import telegram
import os
import time
from random import choice
from dotenv import load_dotenv


def main():
    load_dotenv()
    tg_token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("CHAT_ID")
    time_step = int(os.getenv("TIME_STEP", 24*60*60))

    images = os.listdir('images')
    bot = telegram.Bot(token=tg_token)

    while True:
        random_image = choice(images)
        image_path = os.path.join('images', random_image)

        with open(image_path, 'rb') as file:
            bot.send_photo(chat_id=chat_id, photo=file)

        time.sleep(time_step)

if __name__ == '__main__':
    main()
