"""Модуль форм."""

import os

from django import forms
from django.core.files.uploadedfile import UploadedFile

from blog.models import BlogPost


class BlogPostForm(forms.ModelForm):
    """Форма для создания и редактирования записи блога."""

    class Meta:
        """
        Внутренний класс с настройками формы.

        Attributes:
            model (Model): Модель, с которой связана форма.
            fields (list): Список полей, включенных в форму.
            widgets (dict): Словарь с настройками виджетов для полей.
        """

        model = BlogPost
        fields = ["title", "content", "preview", "is_published"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ведите заголовок",
                }
            ),
            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Введите содержимое записи",
                }
            ),
            "is_published": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
            "preview": forms.FileInput(
                attrs={
                    "class": "form-control",
                    "accept": "image/*",
                }
            ),
        }

    def clean_preview(self) -> UploadedFile | None:
        """Проверяет, что размер изображение не больше 0.5MB. И тип JPG, PNG, WEBP."""
        image = self.cleaned_data.get("preview")
        if image:
            if image.size > 0.5 * 1024 * 1024:
                raise forms.ValidationError("Изображение не должно превышать 0.5MB")

            valid_extensions = [".jpg", ".jpeg", ".png", ".webp"]
            ext = os.path.splitext(image.name)[1].lower()
            if ext not in valid_extensions:
                raise forms.ValidationError("Поддерживаются только JPG, PNG, WEBP")
        return image
