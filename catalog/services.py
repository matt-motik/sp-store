"""Сервисные функции приложения catalog."""

from django.contrib.auth.models import AbstractUser, AnonymousUser
from django.db.models import Q, QuerySet

from catalog.models import Product

UNPUBLISH_PERMISSION = "catalog.can_unpublish_product"


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
