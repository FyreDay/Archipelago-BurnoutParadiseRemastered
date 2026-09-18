from .breakables import get_locations_for_breakable, breakable_count_lookup
from .cars import CarLocations
from .events import EventLocations
from .licenses import LicenseLocations
from .. import GeneratedLocationData
from ...constants import BreakableType, AreaType
from ...data import LocationTypeEnum

all_Enum_locations: list[LocationTypeEnum] = [
    *CarLocations,
    *EventLocations,
    *LicenseLocations,
]

all_Generated_locations: list[GeneratedLocationData] = [
    location
    for area_name, breakables in breakable_count_lookup.items()
    for breakable_type, count in breakables.items()
    for location in get_locations_for_breakable(
        breakable_type,
        AreaType(area_name),
        count,
    )
]