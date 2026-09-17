from .breakables import get_locations_for_breakable, breakable_count_lookup
from .. import GeneratedLocationData
from ...constants import BreakableType, AreaType
from ...data import LocationTypeEnum

all_Enum_locations: list[LocationTypeEnum] = [
    *cars,
    *events,
    *licenses,
]

all_Generated_locations: list[GeneratedLocationData] = [
    location
    for area, breakables in breakable_count_lookup.items()
    for breakable_type, count in breakables.items()
    for location in get_locations_for_breakable(
        breakable_type,
        area,
        count,
    )
]