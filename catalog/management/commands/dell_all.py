"""Модуль команды удаления."""

from django.core.management.base import BaseCommand

from blog.models import BlogPost
from catalog.models import Category, Product


class Command(BaseCommand):
    """Команда удаления."""

    help = "Удаляем всё"

    def handle(self, *args: tuple, **kwargs: dict) -> None:
        """Хендл."""
        # Удаляем существующие записи
        self.stdout.write("Удаляем существующие записи...")
        BlogPost.objects.all().delete()
        Product.objects.all().delete()
        Category.objects.all().delete()
        self.stdout.write(self.style.SUCCESS("Данные успешно удалены"))
