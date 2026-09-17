from BaseClasses import ItemClassification
from .cars import Cars
from ...data import ItemTypeEnum
from .blockers import Blockers
from .events import Events
from .filler import Filler

all_items: list[ItemTypeEnum] = [
    *Blockers,
    *Cars,
    *Events,
    *Filler
]