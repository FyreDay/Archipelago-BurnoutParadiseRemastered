from collections import defaultdict
from typing import TYPE_CHECKING

from BaseClasses import Location, Region, EntranceType
from .data import RegionTypeEnum, GeneratedLocationData
from .data.locations import all_Generated_locations, get_locations_for_breakable, EventLocations, LicenseLocations
from .data.locations.cars import CarLocations
from .data.regions.entrances import Entrances
from .data.regions.regions import Regions
from .constants import BreakableType, AreaType

if TYPE_CHECKING:
    from . import BurnoutParadiseRemasteredWorld


class DefaultRegions(RegionTypeEnum):
    MENU = "Menu"


def create_location(world, data: GeneratedLocationData):
    region = world.get_region(data.region.value)
    location = Location(world.player, data.name, data.location_id, region)
    location.progress_type = data.progress_type
    # location.item_rule = data.item_rule
    print(location.name)
    region.locations.append(location)
    world.set_rule(location, data.rule)

def create_region(world: "BurnoutParadiseRemasteredWorld", region_type: RegionTypeEnum, locations_by_region: dict[RegionTypeEnum, list[GeneratedLocationData]] | None = None):
    region = Region(region_type.value, world.player, world.multiworld)
    world.multiworld.regions.append(region)

    if locations_by_region is None:
        return region

    for data in locations_by_region[region_type]:
        location = Location(world.player, data.name, data.location_id, region)
        location.progress_type = data.progress_type
        # location.item_rule = data.item_rule
        print(f"{location.name} : {data.location_id}")
        region.locations.append(location)
        world.set_rule(location, data.rule)

    return region

def create_regions(world: "BurnoutParadiseRemasteredWorld"):
    menu = create_region(world, DefaultRegions.MENU)

    locations_by_region: dict[RegionTypeEnum, list[GeneratedLocationData]] = defaultdict(list)
    for _location in CarLocations:
        locations_by_region[_location.region].append(GeneratedLocationData(
            name=_location.value,
            region=_location.region,
            rule=_location.rule,
            location_id=_location.location_id
        ))

    for _location in EventLocations:
        locations_by_region[_location.region].append(GeneratedLocationData(
             name=_location.value,
             region=_location.region,
             rule=_location.rule,
             location_id=_location.location_id
         ))

    for _location in LicenseLocations:
        locations_by_region[_location.region].append(GeneratedLocationData(
             name=_location.value,
             region=_location.region,
             rule=_location.rule,
             location_id=_location.location_id
         ))

    for area_name, value in world.options.smash_counts.value.items():
        generated_locs = get_locations_for_breakable(BreakableType.SMASH, AreaType(area_name), value)
        for _location in generated_locs:
            locations_by_region[_location.region].append(_location)

    for area_name, value in world.options.billboard_counts.value.items():
        generated_locs = get_locations_for_breakable(BreakableType.BILLBOARD, AreaType(area_name), value)
        for _location in generated_locs:
            locations_by_region[_location.region].append(_location)

    for area_name, value in world.options.super_jump_counts.value.items():
        generated_locs = get_locations_for_breakable(BreakableType.SUPER_JUMP, AreaType(area_name), value)
        for _location in generated_locs:
            locations_by_region[_location.region].append(_location)

    for region in Regions:
        create_region(world, region, locations_by_region)


def create_entrances(world: "BurnoutParadiseRemasteredWorld"):

    menu = world.get_region("Menu")
    world.create_entrance(menu, world.get_region(Regions.DOWNTOWN_PARADISE.value), name="Menu To Paradise")

    for transition_data in Entrances:
        exiting_region = world.get_region(transition_data.exiting_region.value)
        entering_region = world.get_region(transition_data.entering_region.value)

        entrance = world.create_entrance(exiting_region, entering_region, rule=transition_data.rule, name=transition_data.value, force_creation=True)
        if transition_data.two_way == EntranceType.TWO_WAY:
            entrance_other = world.create_entrance(entering_region,exiting_region, rule=transition_data.rule,
                                             name=transition_data.value + "_back", force_creation=True)
