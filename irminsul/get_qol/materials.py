from .. import get_data

def get_name(name: str):
    return get_data.get_item_name('materials', name)


def get_names():
    return get_data.get_item_names('materials')


def get(name: str):
    return get_data.get_item_data('materials', name)


def get_all():
    return get_data.get_category_data('materials')
