"""Модуль форм."""

import os

from django import forms
from django.core.files.uploadedfile import UploadedFile

from catalog.models import Category, Product


class CategoryForm(forms.ModelForm):
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


class ProductForm(forms.ModelForm):
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
        fields = ["name", "description", "image", "category", "price"]
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
                    "accept": "image/*",
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
            ext = os.path.splitext(image.name)[1].lower()
            if ext not in valid_extensions:
                raise forms.ValidationError("Поддерживаются только JPG, PNG, WEBP")
        return image
