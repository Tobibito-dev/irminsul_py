from .. import get_data
from ..objects.character_object import Character

def get_name(name: str) -> dict:
    return get_data.get_item_name('characters', name)


def get_names() -> list:
    return get_data.get_item_names('characters')


def get(name: str) -> Character:
    return get_data.get_item_data('characters', name)


def get_all() -> dict[Character]:
    return get_data.get_category_data('characters')
