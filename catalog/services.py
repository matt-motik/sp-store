"""Сервисные функции приложения catalog."""

from django.contrib.auth.models import AbstractUser, AnonymousUser
from django.core.cache import cache
from django.db.models import Q, QuerySet

from catalog.models import Product

UNPUBLISH_PERMISSION = "catalog.can_unpublish_product"
CATEGORY_CACHE_TIMEOUT = 60 * 15  # 15 минут


def get_available_products(user: AbstractUser | AnonymousUser, category_id: int | None = None) -> QuerySet[Product]:
    """
    Возвращает доступные пользователю товары с сортировкой по дате создания.

    Опубликованные товары видны всем, неопубликованные — только их владельцам,
    модераторам и суперпользователям.

    Args:
        user: Текущий пользователь запроса.
        category_id: Идентификатор категории для фильтрации (None — все категории).

    Returns:
        QuerySet[Product]: Товары, отфильтрованные по правам и категории.
    """
    queryset = Product.objects.order_by("-created_at")

    if not user.has_perm(UNPUBLISH_PERMISSION):
        if user.is_authenticated:
            queryset = queryset.filter(Q(is_published=True) | Q(owner=user))
        else:
            queryset = queryset.filter(is_published=True)

    if category_id is not None:
        queryset = queryset.filter(category_id=category_id)

    return queryset


def get_category_products(category_id: int) -> list[Product]:
    """
    Возвращает товары категории с низкоуровневым кешированием.

    При первом запросе список загружается из БД и сохраняется в Redis
    под ключом category_{id} на CATEGORY_CACHE_TIMEOUT секунд.
    При повторных запросах берётся из кеша.

    Args:
        category_id: Идентификатор категории.

    Returns:
        list[Product]: Список опубликованных товаров категории,
        отсортированный по created_at (по убыванию).
    """
    cache_key = f"category_{category_id}"
    products: list[Product] | None = cache.get(cache_key)

    if products is None:
        products = list(Product.objects.filter(category_id=category_id, is_published=True).order_by("-created_at"))
        cache.set(cache_key, products, timeout=CATEGORY_CACHE_TIMEOUT)

    return products
