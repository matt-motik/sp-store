"""Management-команда для добавления пользователя в группу модераторов продуктов."""

from typing import Any

from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand, CommandParser

from catalog.management.commands.create_moderator_group import MODERATOR_GROUP_NAME
from users.models import CustomUser


class Command(BaseCommand):
    """Добавляет пользователя в группу «Модератор продуктов».

    Если пользователя с таким email ещё нет — создаёт его, а переданный
    пароль устанавливает вместе с активным статусом, чтобы можно было
    сразу войти под ним. Повторный запуск обновляет пароль и активность.

    Группа должна существовать, иначе команду create_moderator_group
    нужно запустить заранее.

    Example:
        python manage.py add_moderator --email=moderator@example.com --password=secret123
    """

    help = "Добавляет пользователя в группу «Модератор продуктов»"

    def add_arguments(self, parser: CommandParser) -> None:
        """Добавляет аргументы командной строки.

        Args:
            parser: Парсер аргументов Django.
        """
        parser.add_argument(
            "--email",
            type=str,
            required=True,
            help="Email пользователя",
        )
        parser.add_argument(
            "--password",
            type=str,
            help="Пароль пользователя, обязателен для нового пользователя",
        )

    def handle(self, *args: Any, **options: Any) -> None:
        """Создаёт или обновляет пользователя и добавляет его в группу.

        Args:
            *args: Позиционные аргументы (не используются).
            **options: Опции команды, включающие email и password.
        """
        email: str = options["email"]
        password: str | None = options["password"]

        try:
            group = Group.objects.get(name=MODERATOR_GROUP_NAME)
        except Group.DoesNotExist:
            self.stderr.write(
                self.style.ERROR(
                    f"Группа '{MODERATOR_GROUP_NAME}' не найдена. "
                    f"Сначала выполните: python manage.py create_moderator_group"
                )
            )
            return

        if not CustomUser.objects.filter(email=email).exists() and not password:
            self.stderr.write(
                self.style.ERROR(f"Пользователь {email} не найден. Укажите --password, чтобы создать его.")
            )
            return

        user, created = CustomUser.objects.get_or_create(email=email)
        if password:
            user.set_password(password)
            user.is_active = True
            user.save()

        user.groups.add(group)

        if created:
            self.stdout.write(self.style.SUCCESS(f"Пользователь {email} создан и добавлен в группу"))
        else:
            self.stdout.write(
                self.style.WARNING(f"Пользователь {email} уже существовал — обновлён и добавлен в группу")
            )
