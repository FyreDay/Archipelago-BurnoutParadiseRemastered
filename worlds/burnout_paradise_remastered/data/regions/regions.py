from ...constants import AreaType
from .. import RegionTypeEnum


class Regions(RegionTypeEnum):
    PALM_BAY_HEIGHTS = AreaType.PALM_BAY_HEIGHTS.value
    SILVER_LAKE = AreaType.SILVER_LAKE.value
    WHITE_MOUNTAIN = AreaType.WHITE_MOUNTAIN.value
    HARBOR_TOWN = AreaType.HARBOR_TOWN.value
    DOWNTOWN_PARADISE = AreaType.DOWNTOWN_PARADISE.value
    BIG_SURF_ISLAND = AreaType.BIG_SURF_ISLAND.value

    PALM_BAY_HEIGHTS_BREAKABLES = f"{AreaType.PALM_BAY_HEIGHTS.value} Breakables"
    SILVER_LAKE_BREAKABLES = f"{AreaType.SILVER_LAKE.value} Breakables"
    WHITE_MOUNTAIN_BREAKABLES = f"{AreaType.WHITE_MOUNTAIN.value} Breakables"
    HARBOR_TOWN_BREAKABLES = f"{AreaType.HARBOR_TOWN.value} Breakables"
    DOWNTOWN_PARADISE_BREAKABLES = f"{AreaType.DOWNTOWN_PARADISE.value} Breakables"
    BIG_SURF_ISLAND_BREAKABLES = f"{AreaType.BIG_SURF_ISLAND.value} Breakables"
