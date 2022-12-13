import requests
from json.decoder import JSONDecodeError

from ..urls import get_url

from ..util import class_util

from ..objects.data_object import DataObject
from ..objects.artifact_object import Artifact
from ..objects.character_object import Character
from ..objects.common_object import Common
from ..objects.food_object import Food
from ..objects.material_object import Material
from ..objects.weapon_object import Weapon

def get_data_json():
    url = get_url('api')
    if not url.endswith("/"):
        url = url + "/"
    try:
        data = requests.get(url + "data")
        return data.json()
    except JSONDecodeError:
        print("No valid json files at url. Please change url or update package")

def get_all_data():
    data = {}
    temp_data = {}
    url = get_url('api')
    if not url.endswith("/"):
        url = url + "/"

    try:
        temp_data = requests.get(url + 'data').json()
    except JSONDecodeError:
        print("No valid json files at url. Please change url or update package")

    for category in temp_data:
        data[category] = {}
        for item in temp_data[category]:
            data[category][item] = DataObject(temp_data[category][item])
            class_util.change_class(data[category][item], category)
    return data


def get_category_data(category: str):
    items = {}
    temp_items = {}
    url = get_url('api')
    if not url.endswith("/"):
        url = url + "/"

    try:
        temp_items = requests.get(url + category + "/data").json()
    except JSONDecodeError:
        print("No valid json files at url. Please change url or update package")

    for item in temp_items:
        item_object = DataObject(temp_items[item])
        class_util.change_class(item_object, category)
        items[item] = item_object
    return items

def get_item_data(category: str, item: str) -> DataObject | Artifact | Character | Common | Food | Material | Weapon:
    url = get_url('api')
    if not url.endswith("/"):
        url = url + "/"
    try:
        raw_item = requests.get(url + category + "/" + item + "/data")
        item = DataObject(raw_item.json())
        class_util.change_class(item, category)
        return item
    except JSONDecodeError:
        print("No valid json files at url. Please change url or update package")

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

def get_item_name(category: str, item: str):
    url = get_url('api')
    if not url.endswith("/"):
        url = url + "/"
    try:
        item = requests.get(url + category + "/" + item)
        return item.json()
    except JSONDecodeError:
        print("No valid json files at url. Please change url or update package")

