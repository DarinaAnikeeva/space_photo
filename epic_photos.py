import os
import requests
import datetime
from dotenv import load_dotenv
from save_photos import save_photos


def get_epic_photos(images_path, count_photos_epic, api_key):
    url = "https://api.nasa.gov/EPIC/api/natural/images"
    payload = {
        'api_key': api_key
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    for count, dict in enumerate(response.json()[:count_photos_epic]):
        slash_date = datetime.datetime.fromisoformat(dict['date']).strftime("%Y/%m/%d")
        image_url = f"https://api.nasa.gov/EPIC/archive/natural/{slash_date}/png/{dict['image']}.png?api_key={api_key}"
        save_photos(image_url, images_path, f'epic_{count}')


if __name__ == '__main__':
    load_dotenv()
    nasa_token = os.environ['NASA_TOKEN']
    get_epic_photos('aboba', 3, nasa_token)
