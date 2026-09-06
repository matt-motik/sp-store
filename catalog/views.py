"""Представления (views) приложения catalog."""

from django.contrib import messages
from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.functional import Promise
from django.views import View
from django.views.generic import CreateView, DetailView, ListView

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
        Возвращает отсортированный список товаров.

        Returns:
            QuerySet[Product]: Набор товаров, отсортированный по created_at (по убыванию).
        """
        return super().get_queryset().order_by("-created_at")


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


# def contacts(request: HttpRequest) -> HttpResponse:
#     """Отображает страницу контактов и обрабатывает форму обратной связи.
#
#     Args:
#         request: HTTP-запрос (GET или POST).
#
#     Returns:
#         Отрендеренный шаблон страницы контактов.
#         При успешной отправке формы — редирект на эту же страницу.
#     """
#     contact = Contact.objects.first()
#
#     if request.method == "POST":
#         name = request.POST.get("name")
#         phone = request.POST.get("phone")
#         message = request.POST.get("message")
#
#         if all([name, phone, message]):
#             print(f"You have new message from {name}({phone}): {message}")
#             messages.success(request, "Сообщение успешно отправлено!", extra_tags="contact")
#             return redirect("catalog:contacts")
#         else:
#             messages.error(request, "Пожалуйста, заполните все поля", extra_tags="contact")
#
#     context = {
#         "contact": contact,
#     }
#     return render(request, "catalog/contacts.html", context)


class ProductCreateView(CreateView):
    """
    Представление для добавления товара.

    Добавляет товар и выводит сообщение об успехе.
    """

    model = Product
    form_class: type[ProductForm] = ProductForm
    # fields = ["name", "description", "image", "category", "price" ]
    # template_name = "catalog/product_form.html"

    def get_success_url(self) -> str | Promise:
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


class CategoryCreateView(CreateView):
    """
    Представление для добавления категории.

    Добавляет категорию и выводит сообщение об успехе.
    """

    model = Category
    form_class: type[CategoryForm] = CategoryForm

    def get_success_url(self) -> str | Promise:
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
