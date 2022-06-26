import telegram
import os
import argparse
import random
import time
import sys

from fetch_spacex_launch import fetch_spacex_launch
from apod_photos import apod_photos
from epic_photos import epic_photos
from dotenv import load_dotenv


def full(images_path, count_photos_apod, count_photos_epic, api_key, flight_number):
    apod_photos(images_path, count_photos_apod, api_key)
    epic_photos(images_path, count_photos_epic, api_key)
    fetch_spacex_launch(images_path, flight_number)


def get_images(images_path, count_photos_apod, count_photos_epic, api_key, time_sleep, flight_number=None,
               user_image=None):
    if user_image == None:
        if not os.path.exists(images_path):
            full(images_path, count_photos_apod, count_photos_epic, api_key, flight_number)
        images = os.listdir(f'{images_path}/')
        while images:
            random_image = random.choice(images)
            bot.send_document(chat_id=chat_id, document=open(f'{images_path}/{random_image}', 'rb'))
            images.remove(random_image)
            time.sleep(time_sleep)
        else:
            full(images_path, count_photos_apod, count_photos_epic, api_key, flight_number)
            get_images(images_path, count_photos_apod, count_photos_epic, api_key, time_sleep, flight_number=None)
    else:
        bot.send_document(chat_id=chat_id, document=open(f'{user_image}', 'rb'))
        time.sleep(time_sleep)
        get_images(images_path, count_photos_apod, count_photos_epic, api_key, time_sleep, flight_number=None)


if __name__ == '__main__':
    load_dotenv()
    api_key = os.environ['NASA_TOKEN']
    bot = telegram.Bot(token=os.environ['BOT_TOKEN'])
    chat_id = "@fabio_bot_1"
    parser = argparse.ArgumentParser()
    parser.add_argument('timer', nargs='?', default=20)
    namespace = parser.parse_args(sys.argv[1:])
    get_images(images_path='images', count_photos_apod=2, count_photos_epic=1, api_key=api_key,
               time_sleep=namespace.timer)
