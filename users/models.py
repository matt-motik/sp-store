"""Модели данных приложения users."""

from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from config.validators import validate_image_file
from users.managers import CustomUserManager


class CustomUser(AbstractUser):
    """
    Кастомная модель пользователя.

    Наследуется от AbstractUser, но в качестве идентификатора для аутентификации
    использует email (поле username отключено). Дополнительно хранит имя, фамилию,
    аватар, номер телефона и страну.

    Attributes:
        username (None): Поле отключено, авторизация выполняется по email.
        email (EmailField): Уникальный email пользователя, используется для входа.
        first_name (CharField): Имя пользователя (опционально).
        last_name (CharField): Фамилия пользователя (опционально).
        avatar (ImageField): Изображение профиля (опционально, загружается в 'users/avatars/').
        phone_number (PhoneNumberField): Номер телефона в формате E.164 (опционально).
        country (CharField): Страна проживания пользователя (до 100 символов, опционально).

    Meta:
        verbose_name (str): Человекочитаемое имя модели в единственном числе.
        verbose_name_plural (str): Человекочитаемое имя модели во множественном числе.

    Methods:
        __str__(): Возвращает email пользователя как строковое представление.
    """

    username = None

    email: models.EmailField = models.EmailField(
        unique=True,
        verbose_name="Email",
        help_text="Используется для входа в систему.",
    )
    first_name: models.CharField = models.CharField(
        max_length=150,
        blank=True,
        verbose_name="Имя",
    )
    last_name: models.CharField = models.CharField(
        max_length=150,
        blank=True,
        verbose_name="Фамилия",
    )
    avatar: models.ImageField = models.ImageField(
        upload_to="users/avatars/",
        blank=True,
        null=True,
        validators=[validate_image_file],
        verbose_name="Аватар",
    )
    phone_number: PhoneNumberField = PhoneNumberField(
        blank=True,
        verbose_name="Номер телефона",
    )
    country: models.CharField = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Страна",
    )

    USERNAME_FIELD: str = "email"
    REQUIRED_FIELDS: list[str] = []
    objects: CustomUserManager = CustomUserManager()

    class Meta:
        """
        Мета-параметры модели CustomUser.

        Attributes:
            verbose_name (str): Название модели в единственном числе для админки.
            verbose_name_plural (str): Название модели во множественном числе для админки.
        """

        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self) -> str:
        """
        Возвращает строковое представление пользователя.

        Returns:
            str: Email пользователя.
        """
        return str(self.email)
