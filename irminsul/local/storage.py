import json

from ..util.class_util import change_class
from ..objects.data_object import DataObject

data = {}


def load_storage(path: str):
    with open(path, 'r', encoding='utf8') as data_file:
        global data
        json_data = json.loads(data_file.read())
        for category in json_data:
            data[category] = {}
            for item in json_data[category]:
                    data[category][item] = DataObject(json_data[category][item])
                    change_class(data[category][item], category)

def json_to_cache(json_data: dict):
    for category in json_data:
        data[category] = {}
        for item in json_data[category]:
            data[category][item] = DataObject(json_data[category][item])
            change_class(data[category][item], category)

def get_data():
    return data
