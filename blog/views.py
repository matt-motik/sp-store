"""Представления (views) приложения blog."""

from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.db.models import F, QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.utils.functional import Promise
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from blog.forms import BlogPostForm
from blog.models import BlogPost


class BlogPostDetailView(DetailView):
    """Представление для отображения записи."""

    model = BlogPost

    def get_object(self, queryset: QuerySet[BlogPost] | None = None) -> BlogPost:
        """Переопредение данных записи, для увеличения счётчика просмотров."""
        obj = super().get_object(queryset)
        assert isinstance(obj, BlogPost)
        old_views = obj.views_count
        BlogPost.objects.filter(pk=obj.pk).update(views_count=F("views_count") + 1)
        obj.refresh_from_db()

        # Отправляем поздравление при достижении 100 просмотров
        if old_views < 100 <= obj.views_count:
            self.send_congratulation_email(obj)

        return obj

    def send_congratulation_email(self, obj: BlogPost) -> None:
        """Отправляет поздравление о достижении 100 просмотров."""
        subject = f'Запись "{obj.title}" достигла 100 просмотров!'
        message = f"""
        Поздравляем!

        Запись "{obj.title}" достигла 100 просмотров!

        Ура! Возьми с полки пирожок!
        Их там два, левый не бери, а правый я сам съем!
        """

        # Получаем email из MAILERS
        mail_config = settings.MAILERS["default"]
        default_from_email = mail_config.get("DEFAULT_FROM_EMAIL", "admin@example.com")
        recipient_email = default_from_email  # отправляем себе

        try:
            send_mail(
                subject=subject,
                message=message,
                from_email=default_from_email,
                recipient_list=[recipient_email],
                fail_silently=False,
            )
            print("Письмо успешно отправлено")
        except Exception as e:
            print(f"Ошибка отправки email: {e}")


class BlogPostListView(ListView):
    """
    Представление для отображения списка опубликованных записей в блоге.

    Отображает все записи, отсортированные по дате создания (новые сверху).
    """

    model: type[BlogPost] = BlogPost
    paginate_by = 8

    def get_queryset(self) -> QuerySet[BlogPost]:
        """
        Возвращает отсортированный список записей.

        Returns:
            QuerySet[Product]: Набор записей, отсортированный по created_at (по убыванию).
        """
        return super().get_queryset().filter(is_published=True).order_by("-created_at")


class BlogPostCreateView(CreateView):
    """
    Представление для добавления записи блога.

    Добавляет запись и выводит сообщение об успехе.
    """

    model = BlogPost
    form_class: type[BlogPostForm] = BlogPostForm

    def get_success_url(self) -> str | Promise:
        """
        Возвращает URL для перенаправления после успешного создания.

        Returns:
            str: URL страницы деталей созданного товара.
        """
        return reverse_lazy("blog:detail", kwargs={"pk": self.object.pk})


class BlogPostUpdateView(UpdateView):
    """
    Представление для редактирования записи блога.

    После успешного редактирования перенаправляет на страницу записи.
    """

    model: type[BlogPost] = BlogPost
    form_class: type[BlogPostForm] = BlogPostForm

    def get_success_url(self) -> str:
        """
        Возвращает URL для перенаправления после успешного редактирования.

        Returns:
            str: URL страницы деталей отредактированной записи.
        """
        return str(reverse_lazy("blog:detail", kwargs={"pk": self.object.pk}))

    def form_valid(self, form: BlogPostForm) -> HttpResponse:
        """Обрабатывает валидную форму и добавляет сообщение об успехе."""
        response = super().form_valid(form)
        messages.success(
            self.request,
            f"Запись '{self.object.title}' успешно обновлена!",
            extra_tags="blog",
        )
        return response


class BlogPostDeleteView(DeleteView):
    """
    Представление для удаления записи блога.

    После успешного удаления перенаправляет на список записей.
    """

    model: type[BlogPost] = BlogPost
    success_url: str = reverse_lazy("blog:list")

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        """Обрабатывает валидную форму и добавляет сообщение об успехе."""
        post_title = self.object.title
        response = super().form_valid(form)
        messages.success(
            self.request,
            f"Запись '{post_title}' успешно удалена!",
            extra_tags="blog",
        )
        return response
