"""Формы приложения users."""

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ValidationError
from phonenumber_field.widgets import RegionalPhoneNumberWidget

from config.mixins import BootstrapStyleMixin
from users.models import CustomUser


class CustomUserCreationForm(BootstrapStyleMixin, UserCreationForm):
    """Форма регистрации нового пользователя.

    Использует email вместо username. Включает встроенные поля password1
    и password2 (пароль и его подтверждение) из UserCreationForm.

    Attributes:
        Meta: Внутренний класс с настройками формы.
    """

    class Meta(UserCreationForm.Meta):
        """
        Внутренний класс с настройками формы.

        Attributes:
            model (Model): Модель, с которой связана форма.
            fields (tuple): Список полей, включённых в форму.
            widgets (dict): Словарь с настройками виджетов для полей.
        """

        model = CustomUser
        fields = ("email", "first_name", "last_name", "phone_number")
        widgets = {
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "you@example.com",
                    "autocomplete": "email",
                }
            ),
            "first_name": forms.TextInput(
                attrs={
                    "placeholder": "Иван",
                    "autocomplete": "given-name",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "placeholder": "Иванов",
                    "autocomplete": "family-name",
                }
            ),
            "phone_number": RegionalPhoneNumberWidget(
                attrs={
                    "autocomplete": "tel",
                }
            ),
        }

    def clean_email(self) -> str:
        """Проверяет, что email ещё не занят.

        Returns:
            str: Email в нижнем регистре.

        Raises:
            ValidationError: Если пользователь с таким email уже существует.
        """
        email = self.cleaned_data.get("email", "").lower()
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("Пользователь с таким email уже зарегистрирован.")
        return email


class CustomAuthenticationForm(BootstrapStyleMixin, AuthenticationForm):
    """Форма авторизации по email и паролю.

    Переопределяет стандартную AuthenticationForm: поле username
    переименовано в email, добавлено понятное сообщение для неактивного
    пользователя (который ещё не подтвердил email).
    """

    username = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(
            attrs={
                "placeholder": "you@example.com",
                "autocomplete": "email",
                "autofocus": True,
            }
        ),
    )
