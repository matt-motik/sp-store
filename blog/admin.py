"""Настройки административной панели приложения blog."""

from django.contrib import admin

from blog.models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    """Настройки административной панели записи блога."""

    list_display = ("title", "is_published", "views_count", "created_at")
    list_filter = ("is_published", "created_at")
    search_fields = ("title", "content")
    list_editable = ("is_published",)
