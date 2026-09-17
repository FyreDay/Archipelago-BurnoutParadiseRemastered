import json
from importlib.metadata import files
from typing import ClassVar, Any

from BaseClasses import Tutorial, Item
from Utils import visualize_regions
from rule_builder.rules import Has, HasFromList, HasFromListUnique
from worlds.AutoWorld import WebWorld
from . import locations, items
from .constants import BURNOUT_PARADISE_REMASTERED, D_CLASS_WINS, BURNOUT_WINS, BURNOUT_ELITE_WINS, A_CLASS_WINS, \
    B_CLASS_WINS, C_CLASS_WINS
from .data.items import all_items
from .data.items.cars import Cars
from .data.locations import all_Generated_locations, all_Enum_locations
from .data.rules.state_rules import HasEventWins
from .options import burnout_paradise_remastered_option_groups, BurnoutParadiseRemasteredOptions
from .world_base import BurnoutParadiseRemasteredBase


class BurnoutParadiseRemasteredWeb(WebWorld):
    theme = "partyTime"
    setup_en = Tutorial(
        tutorial_name="Multiworld Setup Guide",
        description="A guide to setting up the Burnout Paradise Remasteredrandomizer connected to an Archipelago Multiworld.",
        language="English",
        file_name="setup_en.md",
        link="setup/en",
        authors=["FyreDay"],
    )
    option_groups = burnout_paradise_remastered_option_groups
    tutorials = [setup_en]


def load_manifest():
    return json.loads(
        files(__package__).joinpath("archipelago.json").read_text("utf-8")
    )


class BurnoutParadiseRemasteredWorld(BurnoutParadiseRemasteredBase):

    manifest = load_manifest()

    game = BURNOUT_PARADISE_REMASTERED
    web = BurnoutParadiseRemasteredWeb()

    item_name_to_id: ClassVar[dict[str, int]] = {
        item.value: item.item_id for item in all_items
    }
    location_name_to_id: ClassVar[dict[str, int]] = {
        {loc.value: loc.location_id for loc in all_Enum_locations}
        | {loc.name: loc.location_id for loc in all_Generated_locations}
    }

    item_name_groups: ClassVar[dict[str, set[str]]] = {
        "Car": set(),
        "Event": set(),
        "Area": set(),
    }

    item_lookup = {item.value: item for item in all_items}

    ut_can_gen_without_yaml = True

    @staticmethod
    def interpret_slot_data(slot_data: dict[str, Any]) -> dict[str, Any]:
        return slot_data

    def __init__(self, multiworld, player):
        self.regions: set[str] = set()
        self.itempool: list[Item] = []
        self.starting_items:list[Item] = []

        self.goal_event_wins = 0

        self.is_ut = False
        super().__init__(multiworld, player)

    def generate_early(self) -> None:
        if self.options.goal == BurnoutParadiseRemasteredOptions.goal.option_license_level:
            match self.options.license_goal:
                case BurnoutParadiseRemasteredOptions.license_goal.option_C_Class:
                    self.goal_event_wins = C_CLASS_WINS
                case BurnoutParadiseRemasteredOptions.license_goal.option_B_Class:
                    self.goal_event_wins = B_CLASS_WINS
                case BurnoutParadiseRemasteredOptions.license_goal.option_A_Class:
                    self.goal_event_wins = A_CLASS_WINS
                case BurnoutParadiseRemasteredOptions.license_goal.option_Burnout:
                    self.goal_event_wins = BURNOUT_WINS
                case BurnoutParadiseRemasteredOptions.license_goal.option_Burnout_Elite:
                    self.goal_event_wins = BURNOUT_ELITE_WINS



        self.is_ut = (hasattr(self.multiworld, "re_gen_passthrough")
                      and isinstance(self.multiworld.re_gen_passthrough, dict)
                      and self.game in self.multiworld.re_gen_passthrough)
        self.handle_ut_yamless(None)

    def create_regions(self):
        locations.create_regions(self)
        locations.create_entrances(self)

    def connect_entrances(self) -> None:
        pass

    def create_item(self, item: str) -> Item:
        item_enum = self.item_lookup[item]

        return Item(
            item,
            item_enum.classification,
            item_enum.item_id,
            self.player,
        )

    def create_items(self):
        self.starting_items = items.create_items(self)
        for item in self.starting_items:
            self.push_precollected(item)

    def set_rules(self):
        if self.options.goal.value == self.options.goal.option_collect_cars:
            self.set_completion_rule(HasFromListUnique(
                *(item.value for item in Cars),
                count=self.options.car_goal.value
            ))
        if self.options.goal.value == self.options.goal.option_license_level:
            self.set_completion_rule(HasEventWins(wins=self.goal_event_wins))


    def generate_output(self, output_directory: str):
        print("Generating Output")
        visualize_regions(
            self.multiworld.get_region("Menu", self.player),
            f"Player{self.player}_output.puml",
            show_entrance_names=True,
            regions_to_highlight=self.multiworld.get_all_state(
                self.player
            ).reachable_regions[self.player],
        )

    def fill_slot_data(self) -> id:
        return {
            "sem_ver": self.manifest["mod_version"],
            "goal_config": self.options.goal.value,
            "license_goal_count": self.options.license_goal.value,
            "car_goal_count": self.options.car_goal.value,
            "smash_sanity": self.options.smash_counts.value,
            "billboard_sanity": self.options.billboard_counts.value,
            "super_jump_sanity": self.options.super_jump_counts.value,
            "death_link": self.options.deathlink.value,

        }


    def handle_ut_yamless(
        self, slot_data: dict[str, Any] | None
    ) -> dict[str, Any] | None:
        if self.is_ut and not slot_data:
            slot_data = self.multiworld.re_gen_passthrough[self.game]
        if not slot_data:
            return None

        self.options.deathlink.value = slot_data["death_link"]

        self.options.goal.value = slot_data["goal_config"]
        self.options.license_goal.value = slot_data["license_goal_count"]
        self.options.car_goal.value = slot_data["car_goal_count"]
        self.smash_counts.value = slot_data["smash_sanity"]
        self.options.billboard_counts.value = slot_data["billboard_sanity"]
        self.super_jump_counts.value = slot_data["super_jump_sanity"]

        return slot_data
