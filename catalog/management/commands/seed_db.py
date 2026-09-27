"""Модуль команды засеивания."""

from django.core.management import call_command
from django.core.management.base import BaseCommand

MODERATOR_EMAIL = "moderator@example.com"
CONTENT_MANAGER_EMAILS = ("content@example.com", "editor@example.com")


class Command(BaseCommand):
    """Команда засеивания базы тестовыми данными.

    Загружает пять фикстур: демо-пользователей, контакты, категории, товары
    и записи блога. Затем создаёт группы «Модератор продуктов»
    и «Контент-менеджер» и добавляет в них нужных пользователей.
    Товары и записи связаны с владельцами, поэтому они загружаются
    после пользователей.

    Example:
        python manage.py seed_db
    """

    help = "Очищаем и загружаем тестовые данные в БД"

    def handle(self, *args: tuple, **kwargs: dict) -> None:
        """Хенндл."""
        call_command("dell_all")

        self.stdout.write("Загружаем тестовые данные пользователей в БД...")
        call_command("loaddata", "users.json")

        self.stdout.write("Загружаем тестовые данные контактов в БД...")
        call_command("loaddata", "contacts.json")

        self.stdout.write("Загружаем тестовые данные категорий в БД...")
        call_command("loaddata", "categories.json")

        self.stdout.write("Загружаем тестовые данные продуктов в БД...")
        call_command("loaddata", "products.json")

        self.stdout.write("Загружаем тестовые данные записей блога в БД...")
        call_command("loaddata", "blogposts.json")

        self.stdout.write("Создаём группу модераторов и назначаем модератора...")
        call_command("create_moderator_group")
        call_command("add_moderator", f"--email={MODERATOR_EMAIL}")

        self.stdout.write("Создаём группу контент-менеджеров и назначаем контент-менеджеров...")
        call_command("create_content_manager_group")
        for email in CONTENT_MANAGER_EMAILS:
            call_command("add_content_manager", f"--email={email}")

        self.stdout.write(self.style.SUCCESS("Данные из фикстур загружены."))
