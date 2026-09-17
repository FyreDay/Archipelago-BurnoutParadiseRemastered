import dataclasses
from typing import override

from BaseClasses import CollectionState
from NetUtils import JSONMessagePart
from rule_builder.rules import Rule
from worlds.burnout_paradise_remastered import BurnoutParadiseRemasteredBase, BURNOUT_PARADISE_REMASTERED
from worlds.burnout_paradise_remastered.data.items.events import Events



@dataclasses.dataclass(kw_only=True)
class HasEventWins(Rule[BurnoutParadiseRemasteredBase], game=BURNOUT_PARADISE_REMASTERED):
    wins: int

    @override
    def _instantiate(self, world: BurnoutParadiseRemasteredBase) -> Rule.Resolved:
        # caching_enabled only needs to be passed in when your world inherits from CachedRuleBuilderWorld
        return self.Resolved(wins=self.wins, player=world.player, caching_enabled=False)

    class Resolved(Rule.Resolved):
        wins: int


        @override
        def _evaluate(self, state: CollectionState) -> bool:
            LICENSE_THRESHOLDS = (2, 7, 15, 26, 40, 120)

            remaining_wins = self.wins
            required_events = 0

            for threshold in LICENSE_THRESHOLDS:
                stage_wins = min(remaining_wins, threshold)
                required_events = max(required_events, stage_wins)

                if remaining_wins <= threshold:
                    break

                remaining_wins -= threshold

            return state.has_from_list(
                [item.value for item in Events],
                self.player,
                required_events
            )

        @override
        def item_dependencies(self) -> dict[str, set[int]]:
            return {item.value: {id(self)} for item in Events}

        @override
        def __str__(self) -> str:
            return f"Must Win {self.wins} Events"