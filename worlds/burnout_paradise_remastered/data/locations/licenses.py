from .. import LocationTypeEnum
from ..regions.regions import Regions
from ..rules.state_rules import HasEventWins
from ...constants import *


class LicenseLocations(LocationTypeEnum):
    CLASS_D_LICENSE = ("Class D License", LOCATIONS_OFFSET_LICENSES + 1, Regions.DOWNTOWN_PARADISE, HasEventWins(wins=D_CLASS_WINS))
    CLASS_C_LICENSE = ("Class C License", LOCATIONS_OFFSET_LICENSES + 2, Regions.DOWNTOWN_PARADISE, HasEventWins(wins=C_CLASS_WINS))
    CLASS_B_LICENSE = ("Class B License", LOCATIONS_OFFSET_LICENSES + 3, Regions.DOWNTOWN_PARADISE, HasEventWins(wins=B_CLASS_WINS))
    CLASS_A_LICENSE = ("Class A License", LOCATIONS_OFFSET_LICENSES + 4, Regions.DOWNTOWN_PARADISE, HasEventWins(wins=A_CLASS_WINS))
    BURNOUT_LICENSE = ("Burnout License", LOCATIONS_OFFSET_LICENSES + 5, Regions.DOWNTOWN_PARADISE, HasEventWins(wins=BURNOUT_WINS))
    BURNOUT_ELITE_LICENSE = ("Burnout Elite License", LOCATIONS_OFFSET_LICENSES + 6, Regions.DOWNTOWN_PARADISE, HasEventWins(wins=BURNOUT_ELITE_WINS))