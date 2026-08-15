"""URL configuration for catalog."""
from django.urls import path
from . import views
from .apps import CatalogConfig

app_name = CatalogConfig.name
urlpatterns = [
#    path('admin/', admin.site.urls),
]
