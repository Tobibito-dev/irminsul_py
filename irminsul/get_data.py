from .mode import get_mode
from .data_object import DataObject

from .local import get_data as local
from .rest import get_data as rest


def get_all_data():
    if get_mode() == 'rest':
        return rest.get_categories()
    elif get_mode() == 'local':
        return local.get_categories()


def get_category_data(category: str):
    if get_mode() == 'rest':
        return rest.get_item_names(category)
    elif get_mode() == 'local':
        return local.get_item_names(category)


def get_item_data(category: str, item: str) -> DataObject:
    if get_mode() == 'rest':
        return rest.get_item_name(category, item)
    elif get_mode() == 'local':
        return local.get_item_name(category, item)


def get_categories():
    if get_mode() == 'rest':
        return rest.get_categories()
    elif get_mode() == 'local':
        return local.get_categories()


def get_item_names(category: str):
    if get_mode() == 'rest':
        return rest.get_item_names(category)
    elif get_mode() == 'local':
        return local.get_item_names(category)


def get_item_name(category: str, item: str) -> DataObject:
    if get_mode() == 'rest':
        return rest.get_item_name(category, item)
    elif get_mode() == 'local':
        return local.get_item_name(category, item)


