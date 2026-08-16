"""URL-маршрутизация приложения catalog."""

from django.urls import path

from .apps import CatalogConfig
from .views import contacts, home

app_name = CatalogConfig.name
urlpatterns = [
    path("", home, name="home"),
    path("contacts/", contacts, name="contacts"),
]
