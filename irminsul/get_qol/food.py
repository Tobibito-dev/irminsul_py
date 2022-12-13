from .. import get_data
from ..objects.food_object import Food

def get_name(name: str) -> dict:
    return get_data.get_item_name('food', name)


def get_names() -> list:
    return get_data.get_item_names('food')


def get(name: str) -> Food:
    return get_data.get_item_data('food', name)


def get_all() -> dict[Food]:
    return get_data.get_category_data('food')
