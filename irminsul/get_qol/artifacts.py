from .. import get_data
from ..objects.artifact_object import Artifact

def get_name(name: str) -> dict:
    return get_data.get_item_name('artifacts', name)


def get_names() -> list:
    return get_data.get_item_names('artifacts')


def get(name: str) -> Artifact:
    return get_data.get_item_data('artifacts', name)


def get_all() -> dict[Artifact]:
    return get_data.get_category_data('artifacts')
