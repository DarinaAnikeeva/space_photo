import requests
import urllib.parse
from pprint import pprint
import os


def save_photos(url, images_path, name):
    if not os.path.exists(images_path):
        os.mkdir(images_path)
    response = requests.get(url)
    response.raise_for_status()
    with open(images_path + f'/{name}{expansion(url)}', 'wb') as file:
        file.write(response.content)

# def fetch_spacex_launch(flight_number=None):
#     url = 'https://api.spacexdata.com/v3/launches'
#     response = requests.get(url)
#     response.raise_for_status()
#     if flight_number==None:
#         for photo in response.json()[::-1]:
#             if photo["links"]["flickr_images"]:
#                 links = photo["links"]["flickr_images"]
#                 break
#     else:
#         for photo in response.json():
#             if photo['flight_number'] == flight_number:
#                 links = photo["links"]["flickr_images"]
#     for count, link in enumerate(links):
#         save_photos(link, 'images', f'space_{count}')

def expansion(url):
    url_division = urllib.parse.urlsplit(url, scheme='', allow_fragments=True)
    url_path = url_division[2]
    filename = os.path.splitext(url_path)
    expansion_name = filename[1]
    return expansion_name

# def apod_photos(count_photos, api_key):
#     url = 'https://api.nasa.gov/planetary/apod'
#     payload = {
#         'api_key': api_key,
#         'count': count_photos
#     }
#     response = requests.get(url, params=payload)
#     response.raise_for_status()
#     for count, photo in enumerate(response.json()):
#         save_photos(photo["url"], 'images', f'space_{count}')
#
# def epic_photos(count_photos, api_key):
#     url = "https://api.nasa.gov/EPIC/api/natural/images"
#     payload = {
#         'api_key': api_key
#     }
#     response = requests.get(url, params=payload)
#     response.raise_for_status()
#     for count, dict in enumerate(response.json()):
#         if count == count_photos:
#             break
#         else:
#             slash_date = datetime.datetime.fromisoformat(dict['date']).strftime("%Y/%m/%d")
#             image_url = f"https://api.nasa.gov/EPIC/archive/natural/{slash_date}/png/{dict['image']}.png?api_key={api_key}"
#             save_photos(image_url, 'images', f'space_{count}')
#https://api.nasa.gov/EPIC/archive/natural/{2019/05/30}/png/epic_1b_20190530011359.png?api_key={DEMO_KEY}
# epic_photos(3, nasa_token)
