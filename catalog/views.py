"""Представления (views) приложения catalog."""

from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from catalog.forms import CategoryForm, ProductForm
from catalog.models import Contact, Product

# Create your views here.


def home(request: HttpRequest) -> HttpResponse:
    """Отображает главную страницу магазина.

    Args:
        request: HTTP-запрос.

    Returns:
        Отрендеренный шаблон главной страницы.
    """
    last_products = Product.objects.all().order_by("-created_at")[:5]
    context = {"last_products": last_products}
    return render(request, "home.html", context)


def product_detail(request: HttpRequest, pk: int) -> HttpResponse:
    """Отображает подробную информацию о продукте.

    Args:
        request: HTTP-запрос (GET или POST).

    Returns:
        Отрендеренный шаблон страницы продукта.
    """
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, "product_detail.html", context)


def contacts(request: HttpRequest) -> HttpResponse:
    """Отображает страницу контактов и обрабатывает форму обратной связи.

    Args:
        request: HTTP-запрос (GET или POST).

    Returns:
        Отрендеренный шаблон страницы контактов.
        При успешной отправке формы — редирект на эту же страницу.
    """
    contact = Contact.objects.first()

    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        if all([name, phone, message]):
            print(f"You have new message from {name}({phone}): {message}")
            messages.success(request, "Сообщение успешно отправлено!", extra_tags="contact")
            return redirect("catalog:contacts")
        else:
            messages.error(request, "Пожалуйста, заполните все поля", extra_tags="contact")

    context = {
        "contact": contact,
    }
    return render(request, "contacts.html", context)


def add_product(request: HttpRequest) -> HttpResponse:
    """Отображает страницу добавления товара и обрабатывает форму добавления.

    Args:
        request: HTTP-запрос (GET или POST).

    Returns:
        Отрендеренный шаблон страницы добавления товара.
        При успешной отправке формы — редирект на страницу добавленного товара.
    """
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, f"Товар '{product.name}' успешно добавлен!", extra_tags="product")
            return redirect("catalog:product_detail", pk=product.pk)
    else:
        form = ProductForm()

    return render(request, "add_product.html", {"form": form})


def add_category(request: HttpRequest) -> HttpResponse:
    """Отображает страницу добавления категории и обрабатывает форму добавления.

    Args:
        request: HTTP-запрос (GET или POST).

    Returns:
        Отрендеренный шаблон страницы добавления категории.
        При успешной отправке формы — редирект на страницу добавления товара.
    """
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Категория успешно добавлена!", extra_tags="category")
            return redirect("catalog:add_product")
    else:
        form = CategoryForm()

    return render(request, "add_category.html", {"form": form})
