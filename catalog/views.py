"""Представления (views) приложения catalog."""

from typing import Any

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.cache import cache
from django.db.models import Count, Q, QuerySet
from django.forms import BaseModelForm
from django.http import Http404, HttpRequest, HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.functional import Promise
from django.views import View
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from catalog.forms import CategoryForm, ProductForm
from catalog.models import Category, Contact, Product
from catalog.services import get_available_products

# Create your views here.

UNPUBLISH_PERMISSION = "catalog.can_unpublish_product"
DELETE_PERMISSION = "catalog.delete_product"
CATEGORY_ADD_PERMISSION = "catalog.add_category"
CATEGORY_CHANGE_PERMISSION = "catalog.change_category"
CATEGORY_DELETE_PERMISSION = "catalog.delete_category"


class ProductListView(ListView):
    """
    Представление для отображения списка товаров с пагинацией.

    Отображает все товары, отсортированные по дате создания (новые сверху).
    Опубликованные товары видны всем, неопубликованные — только их владельцам,
    модераторам и суперпользователям.
    Поддерживает фильтрацию по категории через GET-параметр category.
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
        category_id = self.request.GET.get("category")
        category_id_int = int(category_id) if category_id and category_id.isdigit() else None
        return get_available_products(self.request.user, category_id_int)


class ProductDetailView(DetailView):
    """
    Представление для отображения товара.

    Неопубликованные товары видны только владельцам, модераторам и суперпользователям.
    """

    model = Product
    CACHE_TIMEOUT = 60 * 15  # 15 минут

    def get_object(self, queryset=None) -> Product:
        """
        Возвращает товар, доступный текущему пользователю.

        Сначала проверяются права (дешёвый EXISTS-запрос),
        затем товар берётся из кеша или из БД.

        Raises:
            Http404: Если товар не существует или недоступен пользователю.
        """
        pk = self.kwargs["pk"]

        if not self._user_can_view(pk):
            raise Http404

        cache_key = f"product:{pk}"
        product = cache.get(cache_key)

        if product is not None and product.pk is None:
            cache.delete(cache_key)
            product = None

        if product is None:
            try:
                product = Product.objects.get(pk=pk)
            except Product.DoesNotExist:
                raise Http404(f"Товар с pk={pk} не найден") from None
            cache.set(cache_key, product, timeout=self.CACHE_TIMEOUT)
        return product

    def _user_can_view(self, pk: int) -> bool:
        """Проверяет, может ли текущий пользователь видеть товар с указанным pk."""
        user = self.request.user
        if user.has_perm(UNPUBLISH_PERMISSION):
            return Product.objects.filter(pk=pk).exists()
        if user.is_authenticated:
            return Product.objects.filter(Q(pk=pk) & (Q(is_published=True) | Q(owner=user))).exists()
        return Product.objects.filter(pk=pk, is_published=True).exists()


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

    Текущий пользователь автоматически становится владельцем нового товара.
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
        form.instance.owner = self.request.user
        response = super().form_valid(form)
        messages.success(
            self.request,
            f"Товар '{self.object.name}' успешно добавлен!",
            extra_tags="product",
        )
        return response


class CategoryCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """
    Представление для добавления категории.

    Доступно только роли «Модератор продуктов» и суперпользователю.
    Добавляет категорию и выводит сообщение об успехе.
    """

    model: type[Category] = Category
    form_class: type[CategoryForm] = CategoryForm
    permission_required = CATEGORY_ADD_PERMISSION

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

    Доступно только владельцу товара и суперпользователю. После успешного
    редактирования перенаправляет на страницу товара и выводит
    сообщение об успехе.
    """

    model: type[Product] = Product
    form_class: type[ProductForm] = ProductForm

    def get_queryset(self) -> QuerySet[Product]:
        """
        Возвращает товары, которые текущий пользователь может редактировать.

        Returns:
            QuerySet[Product]: Все товары для суперпользователя,
            либо только товары текущего владельца.
        """
        queryset = super().get_queryset()
        if not self.request.user.is_superuser:
            queryset = queryset.filter(owner=self.request.user)
        return queryset

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

    Доступно только владельцу товара и пользователям с правом delete_product.
    После успешного удаления перенаправляет на список товаров и выводит
    сообщение об успехе.
    """

    model: type[Product] = Product
    success_url: str = reverse_lazy("catalog:product_list")

    def get_queryset(self) -> QuerySet[Product]:
        """
        Возвращает товары, которые текущий пользователь может удалить.

        Returns:
            QuerySet[Product]: Все товары для пользователя с правом delete_product,
            либо только товары текущего владельца.
        """
        queryset = super().get_queryset()
        if not self.request.user.has_perm(DELETE_PERMISSION):
            queryset = queryset.filter(owner=self.request.user)
        return queryset

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


class ProductUnpublishView(LoginRequiredMixin, PermissionRequiredMixin, View):
    """
    Представление для снятия товара с публикации.

    Доступно только пользователям с правом can_unpublish_product.
    Показывает страницу подтверждения, а после отправки формы снимает
    товар с публикации и выводит сообщение об успехе.
    """

    template_name = "catalog/product_unpublish.html"
    permission_required = UNPUBLISH_PERMISSION

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        """
        Отображает страницу подтверждения снятия товара с публикации.

        Args:
            request: Запрос страницы подтверждения.
            *args: Позиционные аргументы (не используются).
            **kwargs: Именованные аргументы, содержащие pk товара.

        Returns:
            HttpResponse: Страница с формой подтверждения.
        """
        product = get_object_or_404(Product, id=kwargs["pk"])
        return render(request, self.template_name, {"product": product})

    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        """
        Снимает товар с публикации и перенаправляет на страницу товара.

        Args:
            request: Запрос с отправленной формой подтверждения.
            *args: Позиционные аргументы (не используются).
            **kwargs: Именованные аргументы, содержащие pk товара.

        Returns:
            HttpResponse: Редирект на страницу деталей товара.
        """
        product = get_object_or_404(Product, id=kwargs["pk"])
        if not request.user.has_perm(UNPUBLISH_PERMISSION):
            return HttpResponseForbidden("У Вас нет прав на снятие публикации")
        product.is_published = False
        product.save(update_fields=["is_published", "updated_at"])
        messages.success(
            self.request,
            f"Товар '{product.name}' снят с публикации!",
            extra_tags="product",
        )
        return redirect("catalog:product_detail", pk=product.pk)


class CategoryUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """
    Представление для редактирования категории.

    Доступно только роли «Модератор продуктов» и суперпользователю.
    После успешного редактирования перенаправляет на форму добавления
    товара и выводит сообщение об успехе.
    """

    model: type[Category] = Category
    form_class: type[CategoryForm] = CategoryForm
    permission_required = CATEGORY_CHANGE_PERMISSION

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


class CategoryDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """
    Представление для удаления категории.

    Доступно только роли «Модератор продуктов» и суперпользователю.
    После успешного удаления перенаправляет на список товаров и выводит
    сообщение об успехе.
    """

    model: type[Category] = Category
    success_url: str = reverse_lazy("catalog:product_list")
    permission_required = CATEGORY_DELETE_PERMISSION

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
    Количество неопубликованных товаров показывается только модераторам
    и суперпользователям. Доступно всем пользователям.
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
        queryset = super().get_queryset()
        if self.request.user.has_perm(UNPUBLISH_PERMISSION):
            return queryset.annotate(product_count=Count("products"))
        return queryset.annotate(product_count=Count("products", filter=Q(products__is_published=True)))
