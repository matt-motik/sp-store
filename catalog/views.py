"""Представления (views) приложения catalog."""

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, QuerySet
from django.forms import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.functional import Promise
from django.views import View
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from catalog.forms import CategoryForm, ProductForm
from catalog.models import Category, Contact, Product

# Create your views here.


class ProductListView(ListView):
    """
    Представление для отображения списка товаров с пагинацией.

    Отображает все товары, отсортированные по дате создания (новые сверху).
    Использует пагинацию по 8 товаров на страницу.
    Контекст шаблона:
        - product_list (QuerySet[Product]): Список товаров для текущей страницы.
        - page_obj (Page): Объект пагинации для навигации по страницам.
    """

    model: type[Product] = Product
    paginate_by = 8

    def get_queryset(self) -> QuerySet[Product]:
        """
        Возвращает список товаров, при необходимости отфильтрованный по категории.

        Если в GET передан параметр category, возвращает товары только этой категории.

        Returns:
            QuerySet[Product]: Набор товаров, отсортированный по created_at (по убыванию).
        """
        queryset = super().get_queryset().order_by("-created_at")
        category_id = self.request.GET.get("category")
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset


class ProductDetailView(DetailView):
    """Представление для отображения товара."""

    model = Product


class ContactsView(View):
    """Отображает страницу контактов и обрабатывает форму обратной связи."""

    def get(self, request: HttpRequest) -> HttpResponse:
        """Получение данных о контакте для связи."""
        contact = Contact.objects.first()
        return render(request, "catalog/contacts.html", {"contact": contact})

    def post(self, request: HttpRequest) -> HttpResponse:
        """Отправка обратной связи."""
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        if all([name, phone, message]):
            print(f"You have new message from {name}({phone}): {message}")
            messages.success(request, "Сообщение успешно отправлено!", extra_tags="contact")
        else:
            messages.error(request, "Пожалуйста, заполните все поля", extra_tags="contact")

        return redirect("catalog:contacts")


class ProductCreateView(LoginRequiredMixin, CreateView):
    """
    Представление для добавления товара.

    Добавляет товар и выводит сообщение об успехе.
    """

    model = Product
    form_class: type[ProductForm] = ProductForm
    # fields = ["name", "description", "image", "category", "price" ]
    # template_name = "catalog/product_form.html"

    def get_success_url(self) -> Promise:
        """
        Возвращает URL для перенаправления после успешного создания.

        Returns:
            str: URL страницы деталей созданного товара.
        """
        return reverse_lazy("catalog:product_detail", kwargs={"pk": self.object.pk})

    def form_valid(self, form: ProductForm) -> HttpResponse:
        """Обрабатывает валидную форму и добавляет сообщение об успехе."""
        response = super().form_valid(form)
        messages.success(
            self.request,
            f"Товар '{self.object.name}' успешно добавлен!",
            extra_tags="product",
        )
        return response


class CategoryCreateView(LoginRequiredMixin, CreateView):
    """
    Представление для добавления категории.

    Добавляет категорию и выводит сообщение об успехе.
    """

    model = Category
    form_class: type[CategoryForm] = CategoryForm

    def get_success_url(self) -> Promise:
        """
        Возвращает URL для перенаправления после успешного создания.

        Returns:
            str: URL страницы создания товара.
        """
        return reverse_lazy("catalog:add_product")

    def form_valid(self, form: CategoryForm) -> HttpResponse:
        """Обрабатывает валидную форму и добавляет сообщение об успехе."""
        response = super().form_valid(form)
        messages.success(
            self.request,
            f"Категория '{self.object.name}' успешно добавлена!",
            extra_tags="category",
        )
        return response


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """
    Представление для редактирования товара.

    Доступно только авторизованным пользователям. После успешного
    редактирования перенаправляет на страницу товара и выводит
    сообщение об успехе.
    """

    model: type[Product] = Product
    form_class: type[ProductForm] = ProductForm

    def get_success_url(self) -> str:
        """
        Возвращает URL для перенаправления после успешного редактирования.

        Returns:
            str: URL страницы деталей отредактированного товара.
        """
        return str(reverse_lazy("catalog:product_detail", kwargs={"pk": self.object.pk}))

    def form_valid(self, form: ProductForm) -> HttpResponse:
        """
        Обрабатывает валидную форму и добавляет сообщение об успехе.

        Args:
            form: Валидная форма редактирования товара.

        Returns:
            HttpResponse: Ответ после успешного сохранения.
        """
        response = super().form_valid(form)
        messages.success(
            self.request,
            f"Товар '{self.object.name}' успешно обновлён!",
            extra_tags="product",
        )
        return response


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    """
    Представление для удаления товара.

    Доступно только авторизованным пользователям. После успешного
    удаления перенаправляет на список товаров и выводит сообщение
    об успехе.
    """

    model: type[Product] = Product
    success_url: str = reverse_lazy("catalog:product_list")

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        """
        Обрабатывает валидную форму и добавляет сообщение об успехе.

        Args:
            form: Форма подтверждения удаления.

        Returns:
            HttpResponse: Редирект на список товаров.
        """
        product_name = self.object.name
        response = super().form_valid(form)
        messages.success(
            self.request,
            f"Товар '{product_name}' успешно удалён!",
            extra_tags="product",
        )
        return response


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    """
    Представление для редактирования категории.

    Доступно только авторизованным пользователям. После успешного
    редактирования перенаправляет на форму добавления товара и выводит
    сообщение об успехе.
    """

    model: type[Category] = Category
    form_class: type[CategoryForm] = CategoryForm

    def get_success_url(self) -> str:
        """
        Возвращает URL для перенаправления после успешного редактирования.

        Returns:
            str: URL страницы добавления товара.
        """
        return str(reverse_lazy("catalog:add_product"))

    def form_valid(self, form: CategoryForm) -> HttpResponse:
        """
        Обрабатывает валидную форму и добавляет сообщение об успехе.

        Args:
            form: Валидная форма редактирования категории.

        Returns:
            HttpResponse: Ответ после успешного сохранения.
        """
        response = super().form_valid(form)
        messages.success(
            self.request,
            f"Категория '{self.object.name}' успешно обновлена!",
            extra_tags="category",
        )
        return response


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    """
    Представление для удаления категории.

    Доступно только авторизованным пользователям. После успешного
    удаления перенаправляет на список товаров и выводит сообщение
    об успехе.
    """

    model: type[Category] = Category
    success_url: str = reverse_lazy("catalog:product_list")

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        """
        Обрабатывает валидную форму и добавляет сообщение об успехе.

        Args:
            form: Форма подтверждения удаления.

        Returns:
            HttpResponse: Редирект на список товаров.
        """
        category_name = self.object.name
        response = super().form_valid(form)
        messages.success(
            self.request,
            f"Категория '{category_name}' успешно удалена!",
            extra_tags="category",
        )
        return response


class CategoryListView(ListView):
    """
    Представление для отображения списка категорий.

    Отображает все категории с аннотацией количества товаров в каждой.
    Доступно всем пользователям.
    """

    model: type[Category] = Category
    template_name = "catalog/category_list.html"
    context_object_name = "categories"

    def get_queryset(self) -> QuerySet[Category]:
        """
        Возвращает категории с подсчётом количества товаров.

        Returns:
            QuerySet[Category]: Категории, аннотированные полем product_count.
        """
        return super().get_queryset().annotate(product_count=Count("products"))
