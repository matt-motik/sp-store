"""Management-команда для создания группы контент-менеджеров."""

from typing import Any

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand, CommandParser

from blog.models import BlogPost

CONTENT_MANAGER_GROUP_NAME = "Контент-менеджер"
CONTENT_MANAGER_PERMISSIONS = (
    "add_blogpost",
    "change_blogpost",
    "delete_blogpost",
    "view_blogpost",
)


class Command(BaseCommand):
    """Создаёт группу «Контент-менеджер» и назначает ей права на записи блога.

    Группа получает все права на модель записи блога: создание, изменение,
    удаление и просмотр. Именно эти права проверяют представления блога,
    поэтому обычный пользователь и модератор другого отдела не могут
    управлять публикациями. Повторный запуск обновляет состав группы.

    Example:
        python manage.py create_content_manager_group
    """

    help = "Создаёт группу «Контент-менеджер» с правами на записи блога"

    def add_arguments(self, parser: CommandParser) -> None:
        """Добавляет аргументы командной строки.

        Args:
            parser: Парсер аргументов Django.
        """
        parser.add_argument(
            "--name",
            type=str,
            default=CONTENT_MANAGER_GROUP_NAME,
            help="Название группы контент-менеджеров",
        )

    def handle(self, *args: Any, **options: Any) -> None:
        """Создаёт группу и назначает ей права на записи блога.

        Args:
            *args: Позиционные аргументы (не используются).
            **options: Опции команды, содержащая name группы.
        """
        group_name: str = options["name"]
        group, created = Group.objects.get_or_create(name=group_name)

        content_type = ContentType.objects.get_for_model(BlogPost)
        permissions = Permission.objects.filter(
            content_type=content_type,
            codename__in=CONTENT_MANAGER_PERMISSIONS,
        )
        group.permissions.set(permissions)

        if created:
            self.stdout.write(self.style.SUCCESS(f"Группа '{group_name}' создана"))
        else:
            self.stdout.write(self.style.WARNING(f"Группа '{group_name}' уже существовала — обновлена"))

        for permission in permissions:
            self.stdout.write(f"  {content_type.app_label}.{permission.codename} — {permission.name}")

        missing = set(CONTENT_MANAGER_PERMISSIONS) - {permission.codename for permission in permissions}
        if missing:
            self.stdout.write(
                self.style.WARNING(
                    f"Не найдены права: {', '.join(sorted(missing))}. Примените миграции: python manage.py migrate"
                )
            )
