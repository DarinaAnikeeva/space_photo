import requests
import os
from dotenv import load_dotenv
from save_photos import save_photos


def apod_photos(images_path, count_photos_apod, api_key):
    url = 'https://api.nasa.gov/planetary/apod'
    payload = {
        'api_key': api_key,
        'count': count_photos_apod
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    for count, photo in enumerate(response.json()):
        save_photos(photo["url"], images_path, f'apod_{count}')


if __name__ == '__main__':
    load_dotenv()
    nasa_token = os.environ['NASA_TOKEN']
    apod_photos('sonya_is_the_best', 2, nasa_token)
