from json.decoder import JSONDecodeError

from ..data_object import DataObject


# Necessity
def get_categories():
    try:
        categories = requests.get(get_url('api'))
        return categories.json()
    except JSONDecodeError:
        print("No valid json files at url. Please change url or update package")


def get_item_names(category: str):
    url = get_url('api')
    if not url.endswith("/"):
        url = url + "/"
    try:
        items = requests.get(url + category)
        return items.json()
    except JSONDecodeError:
        print("No valid json files at url. Please change url or update package")


def get_item_name(category: str, item: str) -> DataObject:
    url = get_url('api')
    if not url.endswith("/"):
        url = url + "/"
    try:
        item = requests.get(url + category + "/" + item)
        return DataObject(item.json())
    except JSONDecodeError:
        print("No valid json files at url. Please change url or update package")


