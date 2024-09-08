from typing import Any
from pydantic.dataclasses import dataclass

from typing import Literal

VERSIONS = Literal["2024-07", "2023-12"]

@dataclass
class OrphanetFile:
    url: str
    known_hash: str

def get_optional_enum(tree: dict, field_name: str) -> Any:
    field = tree[field_name]
    if field is None:
        return field
    
    return field['Name']['#text']

def get_list_field(tree: dict, field_name: str) -> list:
    """
    Get list field. Assumes an outer tag `field_name`List and an inner one `field_name`.
    Returns an empty list if inner field is not provided.
    """
    parent_element = tree[f'{field_name}List']

    if field_name not in parent_element:
        return []
    
    return parent_element[field_name]

