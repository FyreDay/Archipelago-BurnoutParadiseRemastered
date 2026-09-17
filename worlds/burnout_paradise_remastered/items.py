from typing import TYPE_CHECKING

from BaseClasses import Item
from .data import ItemTypeEnum, ItemData
from .data.items.blockers import Blockers
from .data.items.cars import Cars, StartingCar
from .data.items.events import Events
from .data.items.filler import Filler

if TYPE_CHECKING:
    from . import MinaTheHollowerWorld


def create_item(world: "MinaTheHollowerWorld", item: ItemData):
    for i in range(item.amount):
        world.itempool.append(world.create_item(item.type.value))


def create_single_item(world: "MinaTheHollowerWorld", item_type: ItemTypeEnum):
    world.itempool.append(world.create_item(item_type.value))

def create_item_unchecked(world: "MinaTheHollowerWorld", item_value: str):
    world.itempool.append(world.create_item(item_value))

def create_items(world: "MinaTheHollowerWorld"):

    all_items: list[ItemData] = []
    starting_items: list[Item] = []

    starting_items.append(world.create_item(StartingCar.HUNTER_CAVALRY.value))

    for item_type in Blockers:
        all_items.append(ItemData(item_type, 1))
    for item_type in Cars:
        all_items.append(ItemData(item_type, 1))
    for item_type in Events:
        all_items.append(ItemData(item_type, 1))

    total_location_count = len(world.multiworld.get_unfilled_locations(world.player))

    _remaining = total_location_count - len(world.itempool)

    create_item(world, ItemData(Filler.BOOST, _remaining))

    world.multiworld.itempool += world.itempool

    return starting_items