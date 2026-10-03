"""Сигналы приложения catalog."""

from typing import Any

from django.core.cache import cache
from django.db.models.signals import post_delete, post_save, pre_save
from django.dispatch import receiver

from catalog.models import Product


@receiver([post_save, post_delete], sender=Product)
def invalidate_product_cache(sender: type[Product], instance: Product, **kwargs: Any) -> None:
    """
    Сбрасывает кеш товара и связанных категорий.

    Вызывается после любого сохранения Product, включая изменения
    is_published и owner, чтобы кеш не рассинхронизировался с БД.

    Args:
        sender: Класс модели, отправившей сигнал (Product).
        instance: Сохранённый или удалённый экземпляр товара.
        **kwargs: Дополнительные аргументы сигнала (created, raw, using и т.д.).
    """
    cache.delete(f"product_{instance.pk}")
    cache.delete(f"category_{instance.category_id}")

    old_category_id = getattr(instance, "_old_category_id", None)
    if old_category_id and old_category_id != instance.category_id:
        cache.delete(f"category_{old_category_id}")


@receiver(pre_save, sender=Product)
def remember_old_category(sender: type[Product], instance: Product, **kwargs: Any) -> None:
    """Запоминает старую категорию товара перед сохранением."""
    if instance.pk:
        try:
            old = Product.objects.get(pk=instance.pk)
            instance._old_category_id = old.category_id
        except Product.DoesNotExist:
            instance._old_category_id = None
    else:
        instance._old_category_id = None
