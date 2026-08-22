"""Модуль команды засеивания."""

from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Команда засеивания базы тестовыми данными."""

    help = "Очищаем и загружаем тестовые данные в БД"

    def handle(self, *args, **kwargs):
        """Хенндл."""
        call_command("dell_all")

        self.stdout.write("Загружаем тестовые данные категорий в БД...")
        call_command("loaddata", "categories.json")

        self.stdout.write("Загружаем тестовые данные продуктов в БД...")
        call_command("loaddata", "products.json")

        self.stdout.write(self.style.SUCCESS("Данные из фикстур загружены."))
