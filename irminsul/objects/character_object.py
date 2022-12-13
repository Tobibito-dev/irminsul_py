from .data_object import DataObject
from .object_methods import stats

class Character(DataObject):
    def get_stats(self, level: int, promoted=False):
        converted_stats = stats.get_stats(self, level, promoted)
        return converted_stats
