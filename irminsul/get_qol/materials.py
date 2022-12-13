from .. import get_data
from ..objects.material_object import Material

def get_name(name: str) -> dict:
    return get_data.get_item_name('materials', name)


def get_names() -> list:
    return get_data.get_item_names('materials')


def get(name: str) -> Material:
    return get_data.get_item_data('materials', name)


def get_all() -> dict[Material]:
    return get_data.get_category_data('materials')
