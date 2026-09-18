from BaseClasses import EntranceType
from rule_builder.rules import Has
from .. import EntranceTypeEnum
from ..items.blockers import Blockers
from ..regions.regions import Regions


class Entrances(EntranceTypeEnum):
    DOWNTOWN_PARADISE_TO_PALM_BAY_HEIGHTS = (
        "Downtown Paradise To Palm Bay Heights",
        Regions.DOWNTOWN_PARADISE,
        Regions.PALM_BAY_HEIGHTS,
        EntranceType.TWO_WAY,
    )

    DOWNTOWN_PARADISE_TO_HARBOR_TOWN = (
        "Downtown Paradise To Harbor Town",
        Regions.DOWNTOWN_PARADISE,
        Regions.HARBOR_TOWN,
        EntranceType.TWO_WAY,
    )

    DOWNTOWN_PARADISE_TO_BIG_SURF_ISLAND = (
        "Downtown Paradise To Big Surf Island",
        Regions.DOWNTOWN_PARADISE,
        Regions.BIG_SURF_ISLAND,
        EntranceType.TWO_WAY,
    )

    PALM_BAY_HEIGHTS_TO_SILVER_LAKE = (
        "Palm Bay Heights To Silver Lake",
        Regions.PALM_BAY_HEIGHTS,
        Regions.SILVER_LAKE,
        EntranceType.TWO_WAY,
    )


    PALM_BAY_HEIGHTS_TO_HARBOR_TOWN = (
        "Palm Bay Heights To Harbor Town",
        Regions.PALM_BAY_HEIGHTS,
        Regions.HARBOR_TOWN,
        EntranceType.TWO_WAY,
    )

    SILVER_LAKE_TO_WHITE_MOUNTAIN = (
        "Silver Lake To White Mountain",
        Regions.SILVER_LAKE,
        Regions.WHITE_MOUNTAIN,
        EntranceType.TWO_WAY,
    )

    SILVER_LAKE_TO_HARBOR_TOWN = (
        "Silver Lake To Harbor Town",
        Regions.SILVER_LAKE,
        Regions.HARBOR_TOWN,
        EntranceType.TWO_WAY,
    )

    WHITE_MOUNTAIN_TO_HARBOR_TOWN = (
        "White Mountain To Harbor Town",
        Regions.WHITE_MOUNTAIN,
        Regions.HARBOR_TOWN,
        EntranceType.TWO_WAY,
    )

    DOWNTOWN_PARADISE_TO_BREAKABLES = (
        "Downtown Paradise To Downtown Paradise Breakables",
        Regions.DOWNTOWN_PARADISE,
        Regions.DOWNTOWN_PARADISE_BREAKABLES,
        EntranceType.TWO_WAY,
        Has(Blockers.DOWNTOWN_PARADISE.value),
    )

    PALM_BAY_HEIGHTS_TO_BREAKABLES = (
        "Palm Bay Heights To Palm Bay Heights Breakables",
        Regions.PALM_BAY_HEIGHTS,
        Regions.PALM_BAY_HEIGHTS_BREAKABLES,
        EntranceType.TWO_WAY,
        Has(Blockers.PALM_BAY_HEIGHTS.value),
    )

    SILVER_LAKE_TO_BREAKABLES = (
        "Silver Lake To Silver Lake Breakables",
        Regions.SILVER_LAKE,
        Regions.SILVER_LAKE_BREAKABLES,
        EntranceType.TWO_WAY,
        Has(Blockers.SILVER_LAKE.value),
    )

    WHITE_MOUNTAIN_TO_BREAKABLES = (
        "White Mountain To White Mountain Breakables",
        Regions.WHITE_MOUNTAIN,
        Regions.WHITE_MOUNTAIN_BREAKABLES,
        EntranceType.TWO_WAY,
        Has(Blockers.WHITE_MOUNTAIN.value),
    )

    HARBOR_TOWN_TO_BREAKABLES = (
        "Harbor Town To Harbor Town Breakables",
        Regions.HARBOR_TOWN,
        Regions.HARBOR_TOWN_BREAKABLES,
        EntranceType.TWO_WAY,
        Has(Blockers.HARBOR_TOWN.value),
    )

    BIG_SURF_ISLAND_TO_BREAKABLES = (
        "Big Surf Island To Big Surf Island Breakables",
        Regions.BIG_SURF_ISLAND,
        Regions.BIG_SURF_ISLAND_BREAKABLES,
        EntranceType.TWO_WAY,
        Has(Blockers.BIG_SURF_ISLAND.value),
    )