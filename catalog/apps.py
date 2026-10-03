"""Конфигурация приложения catalog."""

from django.apps import AppConfig


class CatalogConfig(AppConfig):
    """Конфигурация приложения каталога."""

    name = "catalog"
    default_auto_field = "django.db.models.BigAutoField"
    verbose_name = "Каталог"

    def ready(self) -> None:
        """Регистрирует сигналы приложения."""
        from . import signals  # noqa: F401
