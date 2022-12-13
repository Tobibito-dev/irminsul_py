from .. import get_data
from ..objects.common_object import Common

def get_name(name: str) -> dict:
    return get_data.get_item_name('common', name)


def get_names() -> list:
    return get_data.get_item_names('common')


def get(name: str) -> Common:
    return get_data.get_item_data('common', name)


def get_all() -> dict[Common]:
    return get_data.get_category_data('common')
