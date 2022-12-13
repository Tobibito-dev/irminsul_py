from .data_object import DataObject
from .object_methods import stats
from .. import get_resources

class Weapon(DataObject):
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
