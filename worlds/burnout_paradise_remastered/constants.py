from enum import IntEnum, StrEnum, Enum

BURNOUT_PARADISE_REMASTERED = "Burnout Paradise Remastered"

class BreakableType(IntEnum):
    SMASH = 1
    BILLBOARD = 2
    SUPER_JUMP = 0

class AreaTypeEnum(Enum):
    def __new__(cls, value: str, index: int):
        obj = object.__new__(cls)
        obj._value_ = value
        return obj

    def __init__(self, value: str, index: int):
        self._value_ = value
        self.index = index

class AreaType(AreaTypeEnum):
    PALM_BAY_HEIGHTS = ("Palm Bay Heights", 0)
    SILVER_LAKE = ("Silver Lake", 1)
    WHITE_MOUNTAIN = ("White Mountain", 3)
    HARBOR_TOWN = ("Harbor Town",2)
    DOWNTOWN_PARADISE = ("Downtown Paradise",4)
    BIG_SURF_ISLAND = ("Big Surf Island", 5)


D_CLASS_WINS = 2
C_CLASS_WINS = 9
B_CLASS_WINS = 24
A_CLASS_WINS = 50
BURNOUT_WINS = 90
BURNOUT_ELITE_WINS = 210

ITEMS_OFFSET_TRAPS = 5000
ITEMS_OFFSET_BLOCKERS = 1000
ITEMS_OFFSET_Filler = 100

#locations
LOCATIONS_OFFSET_LICENSES = 1000
LOCATIONS_OFFSET_BREAKABLES = 10000