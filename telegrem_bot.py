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


def combine_functions(images_path, count_photos_apod, count_photos_epic, api_key, flight_number):
    get_apod_photos(images_path, count_photos_apod, api_key)
    get_epic_photos(images_path, count_photos_epic, api_key)
    get_fetch_spacex_launch(images_path, flight_number)


def send_images_to_telegram(images_path, count_photos_apod, count_photos_epic, api_key, time_sleep,
                            flight_number=None,
                            user_image=None):
    if user_image:
        send_image(images_path, user_image)
        time.sleep(time_sleep)
        send_images_to_telegram(images_path, count_photos_apod, count_photos_epic, api_key, time_sleep,
                                flight_number=None)
    else:
        send_random_image(images_path, count_photos_apod, count_photos_epic, api_key, flight_number, time_sleep)
        send_images_to_telegram(images_path, count_photos_apod, count_photos_epic, api_key, time_sleep,
                                flight_number=None)

def send_image(image_directory, image):
    with open(f'{image_directory}/{image}', 'rb') as file:
        bot.send_document(chat_id=chat_id, document=file)
        

def send_random_image(images_path, count_photos_apod, count_photos_epic, api_key, flight_number, time_sleep):
    if not os.path.exists(images_path):
        combine_functions(images_path, count_photos_apod, count_photos_epic, api_key, flight_number)
    images = os.listdir(f'{images_path}/')
    while images:
        random_image = random.choice(images)
        send_image(images_path, random_image)
        images.remove(random_image)
        time.sleep(time_sleep)
    else:
        combine_functions(images_path, count_photos_apod, count_photos_epic, api_key, flight_number)


if __name__ == '__main__':
    load_dotenv()
    api_key = os.environ['NASA_TOKEN']
    bot = telegram.Bot(token=os.environ['BOT_TOKEN'])
    chat_id = os.environ['TG_CHAT_ID']

    parser = argparse.ArgumentParser()
    parser.add_argument('timer', nargs='?', default=20)
    namespace = parser.parse_args(sys.argv[1:])

    send_images_to_telegram(images_path='images',
                            count_photos_apod=2,
                            count_photos_epic=1,
                            api_key=api_key,
                            time_sleep=namespace.timer,
                            flight_number=108)
