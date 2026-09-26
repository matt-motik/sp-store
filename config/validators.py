"""Общие валидаторы проекта."""

from pathlib import Path

from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import UploadedFile

ALLOWED_IMAGE_EXTENSIONS = [".jpg", ".jpeg", ".png", ".webp"]
ALLOWED_IMAGE_CONTENT_TYPES = ("image/jpeg", "image/jpg", "image/png", "image/webp")
MAX_IMAGE_SIZE = 0.5 * 1024 * 1024  # 0.5 МБ


def validate_image_file(image: UploadedFile) -> None:
    """Проверяет размер и формат загружаемого изображения.

    Args:
        image: Загруженный файл изображения.

    Raises:
        ValidationError: Если размер больше 0.5 МБ или формат не JPG/PNG/WEBP.
    """
    if image.size > MAX_IMAGE_SIZE:
        raise ValidationError("Изображение не должно превышать 0.5MB")

    ext = Path(image.name).suffix.lower()
    if ext not in ALLOWED_IMAGE_EXTENSIONS:
        raise ValidationError("Поддерживаются только JPG, PNG, WEBP")

    if image.content_type not in ALLOWED_IMAGE_CONTENT_TYPES:
        raise ValidationError("Поддерживаются только JPG, PNG, WEBP")
