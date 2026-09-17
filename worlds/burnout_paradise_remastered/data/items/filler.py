from BaseClasses import ItemClassification
from worlds.burnout_paradise_remastered.constants import ITEMS_OFFSET_Filler
from worlds.burnout_paradise_remastered.data import ItemTypeEnum


class Filler(ItemTypeEnum):
        BOOST = ("Boost", ITEMS_OFFSET_Filler + 0, ItemClassification.filler),
