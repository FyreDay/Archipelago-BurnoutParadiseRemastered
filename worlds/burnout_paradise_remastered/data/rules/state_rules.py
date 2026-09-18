import dataclasses
from typing import override

from BaseClasses import CollectionState
from NetUtils import JSONMessagePart
from rule_builder.rules import Rule
from ...world_base import BurnoutParadiseRemasteredBase
from ..items.events import Events, BurningEvents
from ...constants import BURNOUT_PARADISE_REMASTERED



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

            event_count = state.count_from_list(
                [item.value for item in Events],
                self.player
            )

            burning_event_count = state.count_from_list(
                [item.value for item in BurningEvents],
                self.player
            )

            remaining_wins = self.wins
            remaining_burning_events = burning_event_count

            for threshold in LICENSE_THRESHOLDS:
                stage_wins = min(remaining_wins, threshold)

                normal_wins = min(event_count, stage_wins)
                missing_wins = stage_wins - normal_wins

                burning_wins = min(remaining_burning_events, missing_wins)

                if normal_wins + burning_wins < stage_wins:
                    return False

                remaining_burning_events -= burning_wins
                remaining_wins -= stage_wins

                if remaining_wins <= 0:
                    return True

            return remaining_wins <= 0

        @override
        def item_dependencies(self) -> dict[str, set[int]]:
            return {
                **{item.value: {id(self)} for item in Events},
                **{item.value: {id(self)} for item in BurningEvents}
            }

        @override
        def __str__(self) -> str:
            return f"Must Win {self.wins} Events"