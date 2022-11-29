import requests
from json.decoder import JSONDecodeError

from .urls import get_url
from .data_object import DataObject


# Necessity
def get_categories():
    try:
        categories = requests.get(get_url('api'))
        return categories.json()
    except JSONDecodeError:
        print("No valid json files at url. Please change url or update package")


def get_item_names(category: str):
    url = get_url('api')
    if not url.endswith("/"):
        url = url + "/"
    try:
        items = requests.get(url + category)
        return items.json()
    except JSONDecodeError:
        print("No valid json files at url. Please change url or update package")


def get_item(category: str, item: str) -> DataObject:
    url = get_url('api')
    if not url.endswith("/"):
        url = url + "/"
    try:
        item = requests.get(url + category + "/" + item)
        return DataObject(item.json())
    except JSONDecodeError:
        print("No valid json files at url. Please change url or update package")


# QoL
# artifacts
def get_artifact_names():
    return get_item_names('artifacts')


def get_artifact(artifact_name: str) -> DataObject:
    return get_item('artifacts', artifact_name)


# common
def get_common_names():
    return get_item_names('common')


def get_common(common_name: str) -> DataObject:
    return get_item('common', common_name)


# food
def get_food_names():
    return get_item_names('food')


def get_food(food_name: str) -> DataObject:
    return get_item('food', food_name)


# weapons
def get_weapon_names():
    return get_item_names('weapons')


def get_weapon(weapon_name: str) -> DataObject:
    return get_item('weapons', weapon_name)


# characters
def get_character_names():
    return get_item_names('characters')


def get_character(character_name: str) -> DataObject:
    return get_item('characters', character_name)


# materials
def get_material_names():
    return get_item_names('materials')


def get_material(material_name: str) -> DataObject:
    return get_item('materials', material_name)
