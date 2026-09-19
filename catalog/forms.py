"""Модуль форм."""

from pathlib import Path
from typing import Any

from django import forms
from django.core.files.uploadedfile import UploadedFile

from catalog.models import Category, Product

EXCLUDE_WORDS = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]


def _check_banned_words(value: str, field_name: str) -> str:
    """Проверяет строку на запрещённые слова.

    Args:
        value: Проверяемое значение.
        field_name: Имя поля для текста ошибки.

    Returns:
        str: Исходное значение, если проверка пройдена.

    Raises:
        forms.ValidationError: Если найдено запрещённое слово.
    """
    lowered = (value or "").lower()
    banned = next((w for w in EXCLUDE_WORDS if w in lowered), None)
    if banned:
        raise forms.ValidationError(f'{field_name} не должно содержать слово "{banned}".')
    return value


class BootstrapStyleMixin(forms.Form):
    """Миксин для стилизации полей формы под Bootstrap."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Навешивает CSS-классы на виджеты полей."""
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            widget = field.widget
            if isinstance(widget, forms.CheckboxInput):
                css_class = "form-check-input"
            elif isinstance(widget, forms.Select):
                css_class = "form-select"
            else:
                css_class = "form-control"
            widget.attrs["class"] = css_class


class CategoryForm(BootstrapStyleMixin, forms.ModelForm):
    """Форма для создания и редактирования категории."""

    class Meta:
        """
        Внутренний класс с настройками формы.

        Attributes:
            model (Model): Модель, с которой связана форма.
            fields (list): Список полей, включенных в форму.
            widgets (dict): Словарь с настройками виджетов для полей.
        """

        model = Category
        fields = ["name", "description"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введите название категории",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Введите описание категории",
                }
            ),
        }


class ProductForm(BootstrapStyleMixin, forms.ModelForm):
    """Форма для создания и редактирования товара."""

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label="Выберите категорию",  # Это работает как плейсхолдер
        widget=forms.Select(
            attrs={
                "class": "form-select",
                "aria-describedby": "categoryHelp",
            }
        ),
    )

    class Meta:
        """
        Внутренний класс с настройками формы.

        Attributes:
            model (Model): Модель, с которой связана форма.
            fields (list): Список полей, включенных в форму.
            widgets (dict): Словарь с настройками виджетов для полей.
        """

        model = Product
        fields = ["name", "description", "image", "category", "price", "in_stock"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введите название товара",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Введите описание товара",
                }
            ),
            "price": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "step": "0.01",
                    "placeholder": "0.00",
                    "min": "0",
                }
            ),
            "image": forms.FileInput(
                attrs={
                    "class": "form-control",
                    "accept": "image/jpeg,image/jpg,image/png,image/webp",
                }
            ),
        }

    def clean_price(self) -> float:
        """Проверяет, что цена больше 0."""
        price = self.cleaned_data.get("price")
        if price is None:
            raise forms.ValidationError("Цена обязательна для заполнения")
        if price <= 0:
            raise forms.ValidationError("Цена должна быть больше 0")
        return float(price)

    def clean_image(self) -> UploadedFile | None:
        """Проверяет, что размер изображение не больше 0.5MB. И тип JPG, PNG, WEBP."""
        image = self.cleaned_data.get("image")
        if image:
            if image.size > 0.5 * 1024 * 1024:
                raise forms.ValidationError("Изображение не должно превышать 0.5MB")

            valid_extensions = [".jpg", ".jpeg", ".png", ".webp"]
            ext = Path(image.name).suffix.lower()
            if ext not in valid_extensions:
                raise forms.ValidationError("Поддерживаются только JPG, PNG, WEBP")
            if image.content_type not in ("image/jpeg", "image/jpg", "image/png", "image/webp"):
                raise forms.ValidationError("Поддерживаются только JPG, PNG, WEBP")
        return image

    def clean_name(self) -> str:
        """Проверяет, что имя не содержит запрещённые слова."""
        return _check_banned_words(self.cleaned_data.get("name"), "Имя")

    def clean_description(self) -> str:
        """Проверяет, что описание не содержит запрещённые слова."""
        return _check_banned_words(self.cleaned_data.get("description"), "Описание")
