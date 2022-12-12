from .. import get_data

def get_name(name: str):
    return get_data.get_item_name('characters', name)


def get_names():
    return get_data.get_item_names('characters')


def get(name: str):
    return get_data.get_item_data('characters', name)


def get_all():
    return get_data.get_category_data('characters')
