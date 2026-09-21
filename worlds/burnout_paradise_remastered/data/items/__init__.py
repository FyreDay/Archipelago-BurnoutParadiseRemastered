from BaseClasses import ItemClassification
from .cars import Cars, StartingCar, BurningCars
from ...data import ItemTypeEnum
from .blockers import Blockers
from .events import Events, BurningEvents
from .filler import Filler

all_items: list[ItemTypeEnum] = [
    *Blockers,
    *StartingCar,
    *Cars,
    *BurningCars,
    *Events,
    *BurningEvents,
    *Filler
]