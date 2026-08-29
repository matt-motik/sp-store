"""Представления (views) приложения catalog."""

from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

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
            messages.success(request, "Сообщение успешно отправлено!")
            return redirect("catalog:contacts")  # PRG-паттерн
        else:
            messages.error(request, "Пожалуйста, заполните все поля")

    context = {
        "contact": contact,
    }
    return render(request, "contacts.html", context)
