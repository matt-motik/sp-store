"""Настройки административной панели приложения catalog."""

from django.contrib import admin

from catalog.models import Category, Product


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Настройки административной панели Категорий."""

    list_display = ("id", "name")
    list_display_links = ("id", "name")
    search_fields = ("name", "description")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Настройки административной панели Продуктов."""

    list_display = ("id", "name", "price", "category")
    list_display_links = ("id", "name")
    search_fields = ("name", "description")
    list_filter = ("category",)
