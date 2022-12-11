from .data_object import DataObject

from .get_data import get_category_data
from .get_data import get_item_data
from .get_data import get_item_names
from .get_data import get_item_name


# artifacts
def get_artifact_names():
    return get_item_names('artifacts')


def get_artifact_name(artifact_name: str) -> DataObject:
    return get_item_name('artifacts', artifact_name)


# common
def get_common_names():
    return get_item_names('common')


def get_common_name(common_name: str) -> DataObject:
    return get_item_name('common', common_name)


# food
def get_food_names():
    return get_item_names('food')


def get_food_name(food_name: str) -> DataObject:
    return get_item_name('food', food_name)


# weapons
def get_weapon_names():
    return get_item_names('weapons')


def get_weapon_name(weapon_name: str) -> DataObject:
    return get_item_name('weapons', weapon_name)


# characters
def get_character_names():
    return get_item_names('characters')


def get_character_name(character_name: str) -> DataObject:
    return get_item_name('characters', character_name)


# materials
def get_material_names():
    return get_item_names('materials')


def get_material_name(material_name: str) -> DataObject:
    return get_item_name('materials', material_name)
