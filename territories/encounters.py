from .blighted_sands.encounters import encounters_blighted_sands
from .bogwood_swamp.encounters import encounters_bogwood_swamp
from .canyons_of_the_howling_red_rocks.encounters import canyons_encounters
from .frozen_wastes.encounters import frozen_waste_encounters

encounters = {
    "the-blighted-sands": encounters_blighted_sands,
    "bogwood-swamp": encounters_bogwood_swamp,
    "canyons-of-the-howling-red-rock": canyons_encounters,
    "frozen-wastes": frozen_waste_encounters,
}
