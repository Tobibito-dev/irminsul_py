from .mode import get_mode, Mode
from .data_object import DataObject

from .local import get_data as local
from .online import get_data as online


def get_all_data():
    if get_mode() == Mode.ONLINE:
        return online.get_all_data()
    elif get_mode() == Mode.LOCAL:
        return local.get_all_data()


def get_category_data(category: str):
    if get_mode() == Mode.ONLINE:
        return online.get_category_data(category)
    elif get_mode() == Mode.LOCAL:
        return local.get_category_data(category)


def get_item_data(category: str, item: str) -> DataObject:
    if get_mode() == Mode.ONLINE:
        return online.get_item_data(category, item)
    elif get_mode() == Mode.LOCAL:
        return local.get_item_data(category, item)


def get_categories():
    if get_mode() == Mode.ONLINE:
        return online.get_categories()
    elif get_mode() == Mode.LOCAL:
        return local.get_categories()


def get_item_names(category: str):
    if get_mode() == Mode.ONLINE:
        return online.get_item_names(category)
    elif get_mode() == Mode.LOCAL:
        return local.get_item_names(category)


def get_item_name(category: str, item: str):
    if get_mode() == Mode.ONLINE:
        return online.get_item_name(category, item)
    elif get_mode() == Mode.LOCAL:
        return local.get_item_name(category, item)


