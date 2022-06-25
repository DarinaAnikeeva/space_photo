import requests
import os
from dotenv import load_dotenv
from save_photos import save_photos

load_dotenv()
nasa_token = os.environ['NASA_TOKEN']


def apod_photos(count_photos, api_key):
    url = 'https://api.nasa.gov/planetary/apod'
    payload = {
        'api_key': api_key,
        'count': count_photos
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    for count, photo in enumerate(response.json()):
        save_photos(photo["url"], 'images', f'space_{count}')

apod_photos(2, nasa_token)