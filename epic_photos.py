import os
import requests
import datetime
from dotenv import load_dotenv
from save_photos import save_photos

load_dotenv()
nasa_token = os.environ['NASA_TOKEN']

def epic_photos(count_photos, api_key):
    url = "https://api.nasa.gov/EPIC/api/natural/images"
    payload = {
        'api_key': api_key
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    for count, dict in enumerate(response.json()):
        if count == count_photos:
            break
        else:
            slash_date = datetime.datetime.fromisoformat(dict['date']).strftime("%Y/%m/%d")
            image_url = f"https://api.nasa.gov/EPIC/archive/natural/{slash_date}/png/{dict['image']}.png?api_key={api_key}"
            save_photos(image_url, 'images', f'space_{count}')

epic_photos(3, nasa_token)