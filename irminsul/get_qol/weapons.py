from .. import get_data
from ..objects.weapon_object import Weapon

def get_name(name: str) -> dict:
    return get_data.get_item_name('weapons', name)


def get_names() -> list:
    return get_data.get_item_names('weapons')


def get(name: str) -> Weapon:
    return get_data.get_item_data('weapons', name)


def get_all() -> dict[Weapon]:
    return get_data.get_category_data('weapons')
