from .blighted_sands.lay_of_the_lands import lay_of_the_land_blighted_sands
from .bogwood_swamp.lay_of_the_land import lay_of_the_land_bogwood_swamp
from .canyons_of_the_howling_red_rocks.lay_of_the_land import canyon_lay
from .frozen_wastes.lay_of_the_land import frozen_lay_of_the_land
from .great_plains_of_unbidden_sorrow.lay_of_the_land import lay_great_plains
from .land_of_perpetual_stone_and_mire.lay_of_the_land import (
    land_of_perpetual_stone_and_mire_lay,
)
from .mountains_that_crawl.lay_of_the_land import lay_mountains_that_crawl
from .sea_that_runs_red.lay_of_the_land import lay_sea
from .the_unsettled_expanse.lay_of_the_land import unsettled_lay

lay_of_the_land = {
    "the-blighted-sands": lay_of_the_land_blighted_sands,
    "bogwood-swamp": lay_of_the_land_bogwood_swamp,
    "canyons-of-the-howling-red-rock": canyon_lay,
    "frozen-wastes": frozen_lay_of_the_land,
    "great-plains-of-unbidden-sorrow": lay_great_plains,
    "land-of-perpetual-stone-and-mire": land_of_perpetual_stone_and_mire_lay,
    "mountains-that-crawl": lay_mountains_that_crawl,
    "sea-that-runs-red": lay_sea,
    "the-unsettled-expanse": unsettled_lay,
}
