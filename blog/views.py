"""Представления (views) приложения blog."""

import smtplib

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.mail import send_mail
from django.db.models import F, QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.utils.functional import Promise
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from blog.forms import BlogPostForm
from blog.models import BlogPost

ADD_PERMISSION = "blog.add_blogpost"
CHANGE_PERMISSION = "blog.change_blogpost"
DELETE_PERMISSION = "blog.delete_blogpost"


class BlogPostDetailView(DetailView):
    """Представление для отображения записи."""

    model = BlogPost

    def get_queryset(self) -> QuerySet[BlogPost]:
        """
        Возвращает набор записей, доступных текущему пользователю.

        Returns:
            QuerySet[BlogPost]: Опубликованные записи, либо все записи для роли
            «Контент-менеджер» и суперпользователя.
        """
        queryset = super().get_queryset()
        if not self.request.user.has_perm(CHANGE_PERMISSION):
            queryset = queryset.filter(is_published=True)
        return queryset

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
        default_from_email = settings.DEFAULT_FROM_EMAIL
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
        except (smtplib.SMTPException, OSError) as e:
            print(f"Ошибка отправки email: {e}")


class BlogPostListView(ListView):
    """
    Представление для отображения списка записей в блоге.

    Опубликованные записи видны всем, черновики — только роли «Контент-менеджер»
    и суперпользователю.
    """

    model: type[BlogPost] = BlogPost
    paginate_by = 8

    def get_queryset(self) -> QuerySet[BlogPost]:
        """
        Возвращает отсортированный список записей.

        Returns:
            QuerySet[BlogPost]: Набор записей, отсортированный по created_at (по убыванию).
        """
        queryset = super().get_queryset().order_by("-created_at")
        if not self.request.user.has_perm(CHANGE_PERMISSION):
            queryset = queryset.filter(is_published=True)
        return queryset


class BlogPostMyListView(LoginRequiredMixin, ListView):
    """
    Представление для отображения записей, созданных текущим пользователем.

    Показывает и опубликованные записи, и черновики, принадлежащие пользователю.
    """

    model: type[BlogPost] = BlogPost
    paginate_by = 8
    template_name = "blog/blogpost_mine.html"

    def get_queryset(self) -> QuerySet[BlogPost]:
        """
        Возвращает записи текущего пользователя.

        Returns:
            QuerySet[BlogPost]: Набор собственных записей, отсортированный по created_at.
        """
        return super().get_queryset().filter(owner=self.request.user).order_by("-created_at")


class BlogPostCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """
    Представление для добавления записи блога.

    Доступно только роли «Контент-менеджер» и суперпользователю.
    Текущий пользователь автоматически становится владельцем новой записи.
    """

    model = BlogPost
    form_class: type[BlogPostForm] = BlogPostForm
    permission_required = ADD_PERMISSION

    def get_success_url(self) -> Promise:
        """
        Возвращает URL для перенаправления после успешного создания.

        Returns:
            str: URL страницы деталей созданной записи.
        """
        return reverse_lazy("blog:detail", kwargs={"pk": self.object.pk})

    def form_valid(self, form: BlogPostForm) -> HttpResponse:
        """Обрабатывает валидную форму и добавляет сообщение об успехе."""
        form.instance.owner = self.request.user
        response = super().form_valid(form)
        messages.success(
            self.request,
            f"Запись '{self.object.title}' успешно добавлена!",
            extra_tags="blog",
        )
        return response


class BlogPostUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """
    Представление для редактирования записи блога.

    Доступно только роли «Контент-менеджер» и суперпользователю.
    После успешного редактирования перенаправляет на страницу записи.
    """

    model: type[BlogPost] = BlogPost
    form_class: type[BlogPostForm] = BlogPostForm
    permission_required = CHANGE_PERMISSION

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


class BlogPostDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """
    Представление для удаления записи блога.

    Доступно только роли «Контент-менеджер» и суперпользователю.
    После успешного удаления перенаправляет на список записей.
    """

    model: type[BlogPost] = BlogPost
    success_url: str = reverse_lazy("blog:list")
    permission_required = DELETE_PERMISSION

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
