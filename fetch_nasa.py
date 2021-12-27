import requests
import os
from pathlib import Path
from urllib.parse import urlsplit, unquote
from dotenv import load_dotenv
from api_helpers import save_image


def get_file_extension(url):
    pathname = urlsplit(url).path
    filename = unquote(os.path.split(pathname)[1])
    extension = os.path.splitext(filename)[1]
    return extension


def fetch_apod_images(url, token):
    params = {
        'api_key': token,
        'count': 40,
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    apod_images = response.json()
    for foto_number, foto in enumerate(apod_images):
        foto = foto['url']
        extension = get_file_extension(foto)
        save_image(foto, './images/apod{}{}'.format(foto_number, extension))


def fetch_epic_images(url, token):
    params = {'api_key': token}

    response = requests.get(url+'/api/natural', params=params)
    response.raise_for_status()

    epic_data = response.json()
    epic_images = []
    for data in epic_data:
        image = data['image']
        date = data['date'].split()[0].replace('-', '/')
        epic_images.append((image, date))

    for number, image in enumerate(epic_images[:7]):
        image, date = image[0], image[1]
        link = url+'/archive/natural/'+date+'/png/'+image+'.png'
        save_image(link, './images/epic{}.png'.format(number), params=params)


def main():
    load_dotenv()
    nasa_token = os.getenv("NASA_TOKEN")
    Path("./images").mkdir(parents=True, exist_ok=True)

    apod_url = 'https://api.nasa.gov/planetary/apod'
    epic_url = 'https://api.nasa.gov/EPIC'

    fetch_apod_images(apod_url, nasa_token)
    fetch_epic_images(epic_url, nasa_token)

if __name__ == '__main__':
    main()
