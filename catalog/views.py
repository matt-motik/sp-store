"""Представления (views) приложения catalog."""

from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

# Create your views here.


def home(request: HttpRequest) -> HttpResponse:
    """Отображает главную страницу магазина.

    Args:
        request: HTTP-запрос.

    Returns:
        Отрендеренный шаблон главной страницы.
    """
    return render(request, "home.html")


def contacts(request: HttpRequest) -> HttpResponse:
    """Отображает страницу контактов и обрабатывает форму обратной связи.

    Args:
        request: HTTP-запрос (GET или POST).

    Returns:
        Отрендеренный шаблон страницы контактов.
        При успешной отправке формы — редирект на эту же страницу.
    """
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

    return render(request, "contacts.html")
