import telegram
import os
import argparse
import random
import time
import sys

from fetch_spacex_launch import get_fetch_spacex_launch
from apod_photos import get_apod_photos
from epic_photos import get_epic_photos
from dotenv import load_dotenv


def combines_functions(images_path, count_photos_apod, count_photos_epic, api_key, flight_number):
    get_apod_photos(images_path, count_photos_apod, api_key)
    get_epic_photos(images_path, count_photos_epic, api_key)
    get_fetch_spacex_launch(images_path, flight_number)


def get_images(images_path,
               count_photos_apod,
               count_photos_epic,
               api_key,
               time_sleep,
               flight_number=None,
               user_image=None):
    if user_image:
        bot.send_document(chat_id=chat_id, document=open(f'{user_image}', 'rb'))
        time.sleep(time_sleep)
        get_images(images_path,
                   count_photos_apod,
                   count_photos_epic,
                   api_key,
                   time_sleep,
                   flight_number=None)
    else:
        get_random_image(images_path,
                         count_photos_apod,
                         count_photos_epic,
                         api_key,
                         flight_number,
                         time_sleep)
        get_images(images_path,
                   count_photos_apod,
                   count_photos_epic,
                   api_key,
                   time_sleep,
                   flight_number=None)


def get_random_image(images_path,
                     count_photos_apod,
                     count_photos_epic,
                     api_key,
                     flight_number,
                     time_sleep):
    if not os.path.exists(images_path):
        combines_functions(images_path,
                           count_photos_apod,
                           count_photos_epic,
                           api_key,
                           flight_number)
    images = os.listdir(f'{images_path}/')
    while images:
        random_image = random.choice(images)
        bot.send_document(chat_id=chat_id, document=open(f'{images_path}/{random_image}', 'rb'))
        images.remove(random_image)
        time.sleep(time_sleep)
    else:
        combines_functions(images_path,
                           count_photos_apod,
                           count_photos_epic,
                           api_key,
                           flight_number)


if __name__ == '__main__':
    load_dotenv()
    api_key = os.environ['NASA_TOKEN']
    bot = telegram.Bot(token=os.environ['BOT_TOKEN'])
    chat_id = os.environ['TG_CHAT_ID']

    parser = argparse.ArgumentParser()
    parser.add_argument('timer', nargs='?', default=20)
    namespace = parser.parse_args(sys.argv[1:])

    get_images(images_path='images',
               count_photos_apod=2,
               count_photos_epic=1,
               api_key=api_key,
               time_sleep=namespace.timer,
               flight_number=108)
