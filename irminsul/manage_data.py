import json
from json import JSONDecodeError

from .urls import Url, get_url
from .online.get_data import get_data_json
from .local.storage import load_storage, json_to_cache


def cache_data():
    data = get_data_json()
    json_to_cache(data)

def download_data():
    try:
        data = get_data_json()
    except JSONDecodeError:
        print('No connection or data available. Keeping old Data.'
              ' Please check api version, url and internet connection.')
    else:
        with open(get_url(Url.LOCAL), 'w', encoding='utf8') as file:
            json.dump(data, file, ensure_ascii=False)


def load_data():
    load_storage(get_url(Url.LOCAL))



