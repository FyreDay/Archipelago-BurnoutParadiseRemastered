from .. import GeneratedLocationData
from ..regions.regions import Regions
from ...constants import AreaType, BreakableType, LOCATIONS_OFFSET_BREAKABLES

breakable_count_lookup = {
    AreaType.DOWNTOWN_PARADISE : {
        BreakableType.SMASH : 80,
        BreakableType.BILLBOARD : 30,
        BreakableType.SUPER_JUMP : 10,

    },
    AreaType.HARBOR_TOWN: {
        BreakableType.SMASH: 90,
        BreakableType.BILLBOARD : 25,
        BreakableType.SUPER_JUMP : 10,

    },
    AreaType.WHITE_MOUNTAIN: {
        BreakableType.SMASH: 90,
        BreakableType.BILLBOARD : 25,
        BreakableType.SUPER_JUMP : 10,

    },
    AreaType.SILVER_LAKE: {
        BreakableType.SMASH: 90,
        BreakableType.BILLBOARD : 20,
        BreakableType.SUPER_JUMP : 10,

    },
    AreaType.PALM_BAY_HEIGHTS: {
        BreakableType.SMASH: 50,
        BreakableType.BILLBOARD : 20,
        BreakableType.SUPER_JUMP : 10,

    },
    AreaType.BIG_SURF_ISLAND: {
        BreakableType.SMASH: 75,
        BreakableType.BILLBOARD : 45,
        BreakableType.SUPER_JUMP : 15,

    }
}

name_lookup = {
    BreakableType.SMASH: "Smash",
    BreakableType.BILLBOARD: "Billboard",
    BreakableType.SUPER_JUMP: "Super Jump"
}

region_lookup = {
    AreaType.PALM_BAY_HEIGHTS: Regions.PALM_BAY_HEIGHTS_BREAKABLES,
    AreaType.SILVER_LAKE: Regions.SILVER_LAKE_BREAKABLES,
    AreaType.WHITE_MOUNTAIN: Regions.WHITE_MOUNTAIN_BREAKABLES,
    AreaType.HARBOR_TOWN: Regions.HARBOR_TOWN_BREAKABLES,
    AreaType.DOWNTOWN_PARADISE: Regions.DOWNTOWN_PARADISE_BREAKABLES,
    AreaType.BIG_SURF_ISLAND: Regions.BIG_SURF_ISLAND_BREAKABLES,
}

def get_locations_for_breakable(breakable: BreakableType, area: AreaType, count):
    locs: list[GeneratedLocationData] = []
    count = count if count <= breakable_count_lookup[area][breakable] else breakable_count_lookup[area][breakable]
    for num in range(count):
        name = f"{area.name} {"Mega Jump" if area == AreaType.BIG_SURF_ISLAND and breakable == BreakableType.SUPER_JUMP else name_lookup[breakable]} {num+1}"
        locs.append(GeneratedLocationData(
            name = name,
            location_id=LOCATIONS_OFFSET_BREAKABLES + 1000 * area.index + 100 * breakable.value,
            region=region_lookup[area]))
    return locs


