
class DataObject:
    def __init__(self, object_data: dict):
        self.data = object_data
        if type(object_data) != int:
            for key in object_data:
                setattr(self, key, object_data[key])

    def get_value(self, key: str):
        value = getattr(self, key)
        return value

    def get_name(self, language='all'):
        if language == 'all':
            return self.get_value('name')
        else:
            return self.get_value('name')[language]
