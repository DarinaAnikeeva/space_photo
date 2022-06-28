import requests
import urllib.parse
import os


def save_photos(url, images_path, name):
    if not os.path.exists(images_path):
        os.mkdir(images_path)
    response = requests.get(url)
    response.raise_for_status()
    with open(images_path + f'/{name}{get_expansion(url)}', 'wb') as file:
        file.write(response.content)


def get_expansion(url):
    url_division = urllib.parse.urlsplit(url, scheme='', allow_fragments=True)
    url_path = url_division[2]
    filename = os.path.splitext(url_path)
    expansion_name = filename[1]
    return expansion_name
