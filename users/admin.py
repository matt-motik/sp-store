"""Настройки административной панели приложения users."""

from typing import Any

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.http import HttpRequest

from users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(BaseUserAdmin):
    """Настройки административной панели для модели CustomUser.

    Наследуется от стандартного UserAdmin, но адаптирован под модель
    без username: в качестве идентификатора используется email.
    Дополнительно отображает и позволяет редактировать поля avatar,
    phone_number и country.

    Attributes:
        list_display (tuple): Колонки в списке пользователей.
        list_filter (tuple): Фильтры справа.
        search_fields (tuple): Поля для поиска.
        ordering (tuple): Сортировка по умолчанию.
        fieldsets (tuple): Секции формы редактирования пользователя.
        add_fieldsets (tuple): Секции формы создания пользователя.
    """

    list_display = (
        "email",
        "first_name",
        "last_name",
        "phone_number",
        "country",
        "is_staff",
        "is_active",
    )
    list_filter = ("is_staff", "is_superuser", "is_active", "country")
    search_fields = ("email", "first_name", "last_name", "phone_number")
    ordering = ("email",)

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Персональные данные",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "avatar",
                    "phone_number",
                    "country",
                )
            },
        ),
        (
            "Права доступа",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Важные даты", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )

    def get_fieldsets(
        self,
        request: HttpRequest,
        obj: CustomUser | None = None,
    ) -> tuple[Any, ...]:
        """Возвращает fieldsets в зависимости от режима (создание/редактирование).

        Args:
            request: HTTP-запрос.
            obj: Редактируемый объект или None при создании.

        Returns:
            tuple: Набор секций формы.
        """
        if obj is None:
            return self.add_fieldsets
        fieldsets: tuple[Any, ...] = super().get_fieldsets(request, obj)
        return fieldsets
