"""Модели данных приложения catalog."""

from django.db import models


class Category(models.Model):
    """
    Модель категории товаров.

    Attributes:
        name (str): Название категории (максимум 150 символов)
        description (str): Описание категории (необязательное поле)
        created_at (datetime): Дата и время создания записи
        updated_at (datetime): Дата и время последнего обновления записи
    """

    name = models.CharField(max_length=150, verbose_name="Название")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего изменения")

    class Meta:
        """Мета для админки."""

        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self) -> str:
        """
        Возвращает строковое представление категории.

        Returns:
            str: Название категории
        """
        return self.name


class Product(models.Model):
    """
    Модель товара.

    Attributes:
        name (str): Наименование товара (максимум 200 символов)
        description (str): Описание товара (необязательное поле)
        image (ImageField): Изображение товара (необязательное поле)
        category (ForeignKey): Связь с моделью Category
        price (Decimal): Цена за покупку (максимум 10 цифр, 2 знака после запятой)
        created_at (datetime): Дата и время создания записи
        updated_at (datetime): Дата и время последнего обновления записи
    """

    name = models.CharField(max_length=200, verbose_name="Наименование", help_text="Наименование товара")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    image = models.ImageField(upload_to="products/", null=True, blank=True, verbose_name="Изображение")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products", verbose_name="Категория")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена за покупку")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего изменения")

    class Meta:
        """Мета для админки."""

        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["name"]

    def __str__(self) -> str:
        """
        Возвращает строковое представление товара.

        Returns:
            str: Наименование товара
        """
        return self.name
