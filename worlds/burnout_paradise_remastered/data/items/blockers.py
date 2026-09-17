from BaseClasses import ItemClassification
from worlds.burnout_paradise_remastered.constants import AreaType, ITEMS_OFFSET_BLOCKERS
from worlds.burnout_paradise_remastered.data import ItemTypeEnum


class Blockers(ItemTypeEnum):
        PALM_BAY_HEIGHTS = (f"{AreaType.PALM_BAY_HEIGHTS.value} Breakables", ITEMS_OFFSET_BLOCKERS + AreaType.PALM_BAY_HEIGHTS.index, ItemClassification.progression),
        SILVER_LAKE = (f"{AreaType.SILVER_LAKE.value} Breakables", ITEMS_OFFSET_BLOCKERS + AreaType.SILVER_LAKE.index, ItemClassification.progression),
        WHITE_MOUNTAIN = (f"{AreaType.WHITE_MOUNTAIN.value} Breakables", ITEMS_OFFSET_BLOCKERS + AreaType.WHITE_MOUNTAIN.index, ItemClassification.progression),
        HARBOR_TOWN = (f"{AreaType.HARBOR_TOWN.value} Breakables", ITEMS_OFFSET_BLOCKERS + AreaType.HARBOR_TOWN.index, ItemClassification.progression),
        DOWNTOWN_PARADISE = (f"{AreaType.DOWNTOWN_PARADISE.value} Breakables", ITEMS_OFFSET_BLOCKERS + AreaType.DOWNTOWN_PARADISE.index, ItemClassification.progression),
        BIG_SURF_ISLAND = (f"{AreaType.BIG_SURF_ISLAND.value} Breakables", ITEMS_OFFSET_BLOCKERS + AreaType.BIG_SURF_ISLAND.index, ItemClassification.progression),