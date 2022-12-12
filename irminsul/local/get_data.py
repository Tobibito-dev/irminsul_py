from irminsul.objects.data_object import DataObject

from .storage import get_data


# Necessity
def get_all_data():
    return get_data()


def get_category_data(category: str):
    return get_data()[category]


def get_item_data(category: str, item: str):
    return get_data()[category][item]


def get_categories():
    categories = []
    for category in get_data():
        categories.append(category)
    return categories


def get_item_names(category: str):
    item_names = []
    if category in get_data():
        for item_name in get_data()[category]:
            item_names.append(item_name)
    return item_names


def get_item_name(category: str, item: str):
    return get_data()[category][item]['name']
