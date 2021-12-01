from .blighted_sands.encounters import encounters_blighted_sands
from .bogwood_swamp.encounters import encounters_bogwood_swamp
from .canyons_of_the_howling_red_rocks.encounters import canyons_encounters
from .frozen_wastes.encounters import frozen_waste_encounters
from .great_plains_of_unbidden_sorrow.encounters import encounters_great_plains
from .land_of_perpetual_stone_and_mire.encounters import (
    land_of_perpetual_stone_and_mire_encounters,
)
from .mountains_that_crawl.encounters import encounters_mountains_that_crawl

encounters = {
    "the-blighted-sands": encounters_blighted_sands,
    "bogwood-swamp": encounters_bogwood_swamp,
    "canyons-of-the-howling-red-rock": canyons_encounters,
    "frozen-wastes": frozen_waste_encounters,
    "great-plains-of-unbidden-sorrow": encounters_great_plains,
    "land-of-perpetual-stone-and-mire": land_of_perpetual_stone_and_mire_encounters,
    "mountains-that-crawl": encounters_mountains_that_crawl,
    # "sea-that-runs-red":
}
