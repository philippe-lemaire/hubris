from typing import List
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from hubris.utils import roll, find_key

from .models import Territory, Location
from .lay_of_the_land_blighted_sands import lay_of_the_land_blighted_sands

# Create your views here.


class IndexView(ListView):
    model = Territory


class TerritoryDetailView(DetailView):
    model = Territory

    def get_context_data(self, **kwargs):
        roll_lay = roll("d100")
        key_lay = find_key(roll_lay, lay_of_the_land_blighted_sands)
        lay = lay_of_the_land_blighted_sands.get(key_lay)
        context = super().get_context_data(**kwargs)
        context["lay"] = lay
        return context


class LocationDetailView(DetailView):
    model = Location
