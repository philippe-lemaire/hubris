from django.urls import path
from django.urls.resolvers import URLPattern
from django.views.generic import TemplateView
from . import views

app_name = "bestiary"

urlpatterns = [
    path(
        "",
        views.MonsterListView.as_view(),
        name="index",
    ),
    path(
        "<int:pk>",
        views.MonsterDetailView.as_view(),
        name="detail",
    ),
]
