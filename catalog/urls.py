"""URL configuration for catalog."""
from django.urls import path
from .views import home, contacts
from .apps import CatalogConfig

app_name = CatalogConfig.name
urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
]
