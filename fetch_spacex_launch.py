import requests
from save_photos import save_photos


def fetch_spacex_launch(images_path, flight_number=None):
    url = 'https://api.spacexdata.com/v3/launches'
    response = requests.get(url)
    response.raise_for_status()
    if flight_number == None:
        for photo in response.json()[::-1]:
            if photo["links"]["flickr_images"]:
                links = photo["links"]["flickr_images"]
                break
    else:
        for photo in response.json():
            if photo['flight_number'] == flight_number:
                links = photo["links"]["flickr_images"]
    for count, link in enumerate(links):
        save_photos(link, images_path, f'space_{count}')


if __name__ == '__main__':
    fetch_spacex_launch('image', 108)
