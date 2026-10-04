"""Модуль форм."""

from django import forms
from django.core.files.uploadedfile import UploadedFile

from blog.models import BlogPost
from config.mixins import BootstrapStyleMixin
from config.validators import validate_image_file


class BlogPostForm(BootstrapStyleMixin, forms.ModelForm):
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
                    "placeholder": "Ведите заголовок",
                }
            ),
            "content": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Введите содержимое записи",
                }
            ),
            "preview": forms.FileInput(
                attrs={
                    "accept": "image/jpeg,image/png,image/webp",
                }
            ),
        }

    def clean_preview(self) -> UploadedFile | None:
        """Проверяет, что размер изображение не больше 0.5MB. И тип JPG, PNG, WEBP."""
        image = self.cleaned_data.get("preview")
        if image:
            validate_image_file(image)
        return image
