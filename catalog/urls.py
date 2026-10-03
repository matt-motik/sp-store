"""URL-маршрутизация приложения catalog."""

from django.urls import path

from .apps import CatalogConfig
from .views import (
    CategoryCreateView,
    CategoryDeleteView,
    CategoryListView,
    CategoryUpdateView,
    ContactsView,
    ProductCreateView,
    ProductDeleteView,
    ProductDetailView,
    ProductListView,
    ProductUnpublishView,
    ProductUpdateView,
)

app_name = CatalogConfig.name
urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("products/add/", ProductCreateView.as_view(), name="add_product"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("products/<int:pk>/edit/", ProductUpdateView.as_view(), name="edit_product"),
    path("products/<int:pk>/unpublish/", ProductUnpublishView.as_view(), name="unpublish_product"),
    path("products/<int:pk>/delete/", ProductDeleteView.as_view(), name="delete_product"),
    path("category/add/", CategoryCreateView.as_view(), name="add_category"),
    path("category/<int:pk>/edit/", CategoryUpdateView.as_view(), name="edit_category"),
    path("category/<int:pk>/delete/", CategoryDeleteView.as_view(), name="delete_category"),
    path("categories/", CategoryListView.as_view(), name="category_list"),
]
