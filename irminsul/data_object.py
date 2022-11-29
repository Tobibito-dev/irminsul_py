from . import stats
from . import get_resources


class DataObject:
    def __init__(self, object_data: dict):
        self.data = object_data
        if type(object_data) != int:
            for key in object_data:
                setattr(self, key, object_data[key])

    def get_value(self, key: str):
        value = getattr(self, key)
        return value

    def get_stats(self, level: int, promoted=False):
        converted_stats = stats.get_stats(self, level, promoted)
        return converted_stats

    def get_icon(self, icon_type: str):
        if hasattr(self, 'sideIconName') and icon_type == 'side':
            return get_resources.get_image(getattr(self, 'sideIconName'))
        elif hasattr(self, 'iconName') and icon_type == 'front':
            return get_resources.get_image(getattr(self, 'iconName'))
        else:
            print("No icon of type", icon_type, sep=' ')



