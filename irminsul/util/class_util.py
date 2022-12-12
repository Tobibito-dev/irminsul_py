from ..objects.data_object import DataObject
from ..objects.artifact_object import Artifact
from ..objects.character_object import Character
from ..objects.common_object import Common
from ..objects.food_object import Food
from ..objects.material_object import Material
from ..objects.weapon_object import Weapon

def change_class(data: DataObject, object_type: str):
    if object_type == 'artifacts':
        data.__class__ = Artifact
    elif object_type == 'characters':
        data.__class__ = Character
    elif object_type == 'common':
        data.__class__ = Common
    elif object_type == 'food':
        data.__class__ = Food
    elif object_type == 'materials':
        data.__class__ = Material
    elif object_type == 'weapons':
        data.__class__ = Weapon
