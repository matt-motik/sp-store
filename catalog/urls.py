"""URL-маршрутизация приложения catalog."""

from django.urls import path

from .apps import CatalogConfig
from .views import add_product, contacts, home, product_detail

app_name = CatalogConfig.name
urlpatterns = [
    path("", home, name="home"),
    path("contacts/", contacts, name="contacts"),
    path("products/<int:pk>/", product_detail, name="product_detail"),
    path("products/add/", add_product, name="add_product"),
]
