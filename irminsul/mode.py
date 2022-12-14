import os

from .urls import get_url, Url

from .manage_data import download_data, load_data, cache_data


class Mode:
    ONLINE = 'online'
    LOCAL = 'local'
    CACHE = 'cache'


mode = Mode.ONLINE


def change_mode(new_mode: str, force_download=True):
    global mode
    if new_mode == Mode.ONLINE:
        mode = Mode.ONLINE
    elif new_mode == Mode.LOCAL:
        if force_download or not os.path.exists(get_url(Url.LOCAL)):
            download_data()
        load_data()
        mode = Mode.LOCAL
    elif new_mode == Mode.CACHE:
        cache_data()
        mode = Mode.CACHE
    else:
        print('Mode does not exist. Keeping', mode, 'mode.', sep=' ')


def get_mode():
    return mode
