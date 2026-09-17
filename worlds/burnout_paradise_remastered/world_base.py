from rule_builder.cached_world import CachedRuleBuilderWorld
from worlds.AutoWorld import World
from .options import BurnoutParadiseRemasteredOptions



class BurnoutParadiseRemasteredBase(CachedRuleBuilderWorld):
    options_dataclass = BurnoutParadiseRemasteredOptions
    options: BurnoutParadiseRemasteredOptions

    def __init__(self, multiworld, player):
        super().__init__(multiworld, player)