import requests
from pathlib import Path
from api_helpers import save_image


def fetch_spacex_last_launch(url):
    payload, headers = {}, {}

    response = requests.get(url, headers=headers, data=payload)
    response.raise_for_status()

    spacex_images = response.json()['links']['flickr_images']
    for foto_number, foto in enumerate(spacex_images):
        save_image(foto, './images/spacex{}.jpg'.format(foto_number))


def main():
    Path("./images").mkdir(parents=True, exist_ok=True)
    url = "https://api.spacexdata.com/v3/launches/67"
    fetch_spacex_last_launch(url)

if __name__ == '__main__':
    main()
