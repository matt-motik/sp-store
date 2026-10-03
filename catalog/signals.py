"""Сигналы приложения catalog."""

from typing import Any

from django.core.cache import cache
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from catalog.models import Product


@receiver([post_save, post_delete], sender=Product)
def invalidate_product_cache(
    sender: type[Product],
    instance: Product,
    **kwargs: Any,
) -> None:
    """
    Сбрасывает кеш товара при его сохранении или удалении.

    Вызывается после любого сохранения Product, включая изменения
    is_published и owner, чтобы кеш не рассинхронизировался с БД.

    Args:
        sender: Класс модели, отправившей сигнал (Product).
        instance: Сохранённый или удалённый экземпляр товара.
        **kwargs: Дополнительные аргументы сигнала (created, raw, using и т.д.).
    """
    cache.delete(f"product:{instance.pk}")
