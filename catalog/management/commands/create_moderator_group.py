"""Management-команда для создания группы модераторов продуктов."""

from typing import Any

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand, CommandParser

from catalog.models import Category, Product

MODERATOR_GROUP_NAME = "Модератор продуктов"
PRODUCT_MODERATOR_PERMISSIONS = (
    "view_product",
    "change_product",
    "add_product",
    "can_unpublish_product",
    "delete_product",
)
CATEGORY_MODERATOR_PERMISSIONS = (
    "add_category",
    "change_category",
    "delete_category",
)
MODERATOR_PERMISSIONS = PRODUCT_MODERATOR_PERMISSIONS + CATEGORY_MODERATOR_PERMISSIONS


class Command(BaseCommand):
    """Создаёт группу «Модератор продуктов» и назначает ей права.

    Группа получает права на товары: просмотр, создание, изменение,
    отмену публикации и удаление. Также получает права на категории:
    создание, изменение и удаление. Право change_category даёт доступ
    к категориям и в админке, так как право просмотра Django считает
    достаточным. Повторный запуск обновляет состав группы.

    Право can_unpublish_product появляется только после применения миграций,
    поэтому перед первым запуском нужно выполнить migrate.

    Example:
        python manage.py create_moderator_group
    """

    help = "Создаёт группу «Модератор продуктов» с правами на товары"

    def add_arguments(self, parser: CommandParser) -> None:
        """Добавляет аргументы командной строки.

        Args:
            parser: Парсер аргументов Django.
        """
        parser.add_argument(
            "--name",
            type=str,
            default=MODERATOR_GROUP_NAME,
            help="Название группы модераторов",
        )

    def handle(self, *args: Any, **options: Any) -> None:
        """Создаёт группу и назначает ей права на товары и категории.

        Args:
            *args: Позиционные аргументы (не используются).
            **options: Опции команды, содержащая name группы.
        """
        group_name: str = options["name"]
        group, created = Group.objects.get_or_create(name=group_name)

        product_content_type = ContentType.objects.get_for_model(Product)
        category_content_type = ContentType.objects.get_for_model(Category)
        permissions = list(
            Permission.objects.filter(
                content_type=product_content_type,
                codename__in=PRODUCT_MODERATOR_PERMISSIONS,
            )
        ) + list(
            Permission.objects.filter(
                content_type=category_content_type,
                codename__in=CATEGORY_MODERATOR_PERMISSIONS,
            )
        )
        group.permissions.set(permissions)

        if created:
            self.stdout.write(self.style.SUCCESS(f"Группа '{group_name}' создана"))
        else:
            self.stdout.write(self.style.WARNING(f"Группа '{group_name}' уже существовала — обновлена"))

        for permission in permissions:
            self.stdout.write(f"  {permission.content_type.app_label}.{permission.codename} — {permission.name}")

        missing = set(MODERATOR_PERMISSIONS) - {permission.codename for permission in permissions}
        if missing:
            self.stdout.write(
                self.style.WARNING(
                    f"Не найдены права: {', '.join(sorted(missing))}. Примените миграции: python manage.py migrate"
                )
            )
