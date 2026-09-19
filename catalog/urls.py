"""URL-маршрутизация приложения catalog."""

from django.urls import path

from .apps import CatalogConfig
from .views import CategoryCreateView, ContactsView, ProductCreateView, ProductDetailView, ProductListView

app_name = CatalogConfig.name
urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("products/add/", ProductCreateView.as_view(), name="add_product"),
    path("category/add/", CategoryCreateView.as_view(), name="add_category"),
]
