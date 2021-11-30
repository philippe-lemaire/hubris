from .blighted_sands.lay_of_the_lands import lay_of_the_land_blighted_sands
from .bogwood_swamp.lay_of_the_land import lay_of_the_land_bogwood_swamp
from .canyons_of_the_howling_red_rocks.lay_of_the_land import canyon_lay
from .frozen_wastes.lay_of_the_land import frozen_lay_of_the_land

lay_of_the_land = {
    "the-blighted-sands": lay_of_the_land_blighted_sands,
    "bogwood-swamp": lay_of_the_land_bogwood_swamp,
    "canyons-of-the-howling-red-rock": canyon_lay,
    "frozen-wastes": frozen_lay_of_the_land,
}
