import json

data = []


def load_storage(path: str):
    with open(path, 'r', encoding='utf8') as data_file:
        global data
        data = json.loads(data_file.read())


def get_data():
    return data
