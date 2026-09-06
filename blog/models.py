"""Модели данных приложения blog."""

from django.db import models


class BlogPost(models.Model):
    """
    Модель записи в блоге.

    Представляет собой статью/запись с заголовком, содержимым, изображением для превью,
    датами создания и обновления, статусом публикации и счётчиком просмотров.

    Attributes:
        title (CharField): Заголовок записи (до 200 символов).
        content (TextField): Полное содержимое записи.
        preview (ImageField): Изображение для превью (опционально, загружается в папку 'blog/').
        created_at (DateTimeField): Дата и время создания записи (автоматически).
        updated_at (DateTimeField): Дата и время последнего изменения записи (автоматически).
        is_published (BooleanField): Флаг публикации записи (по умолчанию False).
        views_count (PositiveIntegerField): Количество просмотров записи (по умолчанию 0).

    Meta:
        verbose_name (str): Человекочитаемое имя модели в единственном числе.
        verbose_name_plural (str): Человекочитаемое имя модели во множественном числе.
        ordering (list): Сортировка записей по дате создания (новые сверху).

    Methods:
        __str__(): Возвращает заголовок записи как строковое представление.
    """

    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержимое")
    preview = models.ImageField(upload_to="blog/", null=True, blank=True, verbose_name="Превью")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего изменения")
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")
    views_count = models.PositiveIntegerField(default=0, verbose_name="Просмотры")

    class Meta:
        """
        Мета-параметры модели BlogPost.

        Attributes:
            verbose_name (str): Название модели в единственном числе для админки.
            verbose_name_plural (str): Название модели во множественном числе для админки.
            ordering (list): Поле сортировки по умолчанию (новые записи сверху).
        """

        verbose_name = "Запись в блоге"
        verbose_name_plural = "Записи в блоге"
        ordering = ["-created_at"]

    def __str__(self) -> str:
        """
        Возвращает строковое представление записи.

        Returns:
            str: Заголовок записи.
        """
        return str(self.title)
