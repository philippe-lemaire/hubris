from django.urls import path
from django.urls.resolvers import URLPattern
from django.views.generic import TemplateView
from . import views

app_name = "territories"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<slug:slug>", views.TerritoryDetailView.as_view(), name="territory"),
    path("locations/<slug:slug>", views.LocationDetailView.as_view(), name="location"),
]
