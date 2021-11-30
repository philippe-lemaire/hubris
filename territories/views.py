from typing import List
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from hubris.utils import roll, find_key

from .models import Territory, Location
from .encounters import encounters
from .lay_of_the_land import lay_of_the_land

# Create your views here.


class IndexView(ListView):
    model = Territory


class TerritoryDetailView(DetailView):
    model = Territory

    def get_context_data(self, **kwargs):
        # get default context
        context = super().get_context_data(**kwargs)
        # find the slug of the territory we are in, used as key in the lay and encounters dicts
        land = context.get("territory").slug

        # roll and find result for lay of the land
        if lay_of_the_land.get(land):
            roll_lay = roll("d100")
            key_lay = find_key(roll_lay, lay_of_the_land.get(land))
            lay = lay_of_the_land.get(land).get(key_lay)
            context["lay"] = lay

        # roll and find result for encounter of the land
        if encounters.get(land):
            roll_encounter = roll("d100")
            key_encounter = find_key(roll_encounter, encounters.get(land))
            encounter = encounters.get(land).get(key_encounter)
            context["encounter"] = encounter
        return context


class LocationDetailView(DetailView):
    model = Location
