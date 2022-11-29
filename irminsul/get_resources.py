import requests

from .urls import get_url


def get_image(path: str):
    url = get_url('res')
    if not url.endswith("/"):
        url = url + "/"

    image = requests.get(url + path + ".png")
    return image
