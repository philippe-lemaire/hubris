from typing import List
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Territory, Location

# Create your views here.


class IndexView(ListView):
    model = Territory


class TerritoryDetailView(DetailView):
    model = Territory


class LocationDetailView(DetailView):
    model = Location
