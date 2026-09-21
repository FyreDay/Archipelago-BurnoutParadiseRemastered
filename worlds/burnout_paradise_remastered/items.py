from typing import TYPE_CHECKING

from BaseClasses import Item
from .data import ItemTypeEnum, ItemData
from .data.items.blockers import Blockers
from .data.items.cars import Cars, StartingCar, BurningCars
from .data.items.events import Events, BurningEvents
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

    starting_items: list[Item] = []

    starting_items.append(world.create_item(StartingCar.HUNTER_CAVALRY.value))

    starting_events = set(world.random.sample(list(Events), 5))


    for event in starting_events:
        starting_items.append(world.create_item(event.value))

    remaining_events = set(Events) - starting_events

    for item_type in Blockers:
        create_single_item(world, item_type)
    for item_type in Cars:
        create_single_item(world, item_type)
    for item_type in BurningCars:
        create_single_item(world, item_type)
    for item_type in remaining_events:
        create_single_item(world, item_type)


    total_location_count = len(world.multiworld.get_unfilled_locations(world.player))

    _remaining = total_location_count - len(world.itempool)
    print(f"Location Count: {total_location_count} | Item count: {len(world.itempool)}")
    user_response = input("Enter: ")
    create_item(world, ItemData(Filler.BOOST, _remaining))

    world.multiworld.itempool += world.itempool

    return starting_items