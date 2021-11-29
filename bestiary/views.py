from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Monster


class MonsterListView(ListView):
    model = Monster


class MonsterDetailView(DetailView):
    model = Monster
