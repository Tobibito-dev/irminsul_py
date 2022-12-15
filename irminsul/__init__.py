import irminsul
from .mode import change_mode, Mode

from .urls import change_url, Url

from .objects.data_object import DataObject
from .objects.artifact_object import Artifact
from .objects.character_object import Character
from .objects.common_object import Common
from .objects.food_object import Food
from .objects.material_object import Material
from .objects.weapon_object import Weapon

# Data
# Necessity
from .get_data import get_all_data, get_category_data, get_item_data
from .get_data import get_categories, get_item_names, get_item_name

# QoL
from .get_qol import artifacts, characters, common, food, materials, weapons

# Assets
# Necessity
from .get_resources import get_image

irminsul.change_mode(Mode.CACHE)
