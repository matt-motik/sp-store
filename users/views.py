"""Представления (views) приложения users."""

import smtplib

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.views import View
from django.views.generic import FormView

from users.forms import CustomAuthenticationForm, CustomUserCreationForm
from users.models import CustomUser


class RegisterView(FormView):
    """Регистрация нового пользователя.

    Создаёт неактивного пользователя (is_active=False) и отправляет
    письмо со ссылкой для активации. Автоматический вход не выполняется:
    пользователь должен сначала подтвердить email.
    """

    template_name = "users/register.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("users:activation_sent")

    def form_valid(self, form: CustomUserCreationForm) -> HttpResponse:
        """Сохраняет пользователя и отправляет письмо с токеном активации.

        Args:
            form: Валидная форма регистрации.

        Returns:
            HttpResponse: Редирект на страницу «проверьте почту».
        """
        user: CustomUser = form.save(commit=False)
        user.is_active = False
        user.save()

        self.send_activation_email(user)
        messages.success(
            self.request,
            "Регистрация прошла успешно. Проверьте почту и подтвердите аккаунт.",
            extra_tags="users",
        )
        return super().form_valid(form)

    def send_activation_email(self, user: CustomUser) -> None:
        """Отправляет письмо со ссылкой активации.

        Args:
            user: Только что созданный неактивный пользователь.
        """
        uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        activation_path = reverse(
            "users:activate",
            kwargs={"uidb64": uidb64, "token": token},
        )
        activation_url = self.request.build_absolute_uri(activation_path)

        subject = "Подтверждение регистрации"
        message = (
            f"Здравствуйте, {user.first_name or user.email}!\n\n"
            f"Для активации аккаунта перейдите по ссылке:\n{activation_url}\n\n"
            f"Ссылка действует {settings.PASSWORD_RESET_TIMEOUT // 3600} ч."
        )

        try:
            send_mail(
                subject=subject,
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
                fail_silently=False,
            )
            print(f"Письмо активации отправлено на {user.email}")
        except (smtplib.SMTPException, OSError) as exc:
            print(f"Ошибка отправки email: {exc}")


class ActivationSentView(View):
    """Страница «проверьте почту» после регистрации."""

    def get(self, request: HttpRequest) -> HttpResponse:
        """Отображает страницу с инструкцией.

        Args:
            request: HTTP-запрос.

        Returns:
            HttpResponse: Страница activation_sent.html.
        """
        return render(request, "users/activation_sent.html")


class ActivateView(View):
    """Активация аккаунта по ссылке из письма.

    Принимает uidb64 и token, проверяет их и, если всё корректно,
    устанавливает is_active=True.
    """

    def get(self, request: HttpRequest, uidb64: str, token: str) -> HttpResponse:
        """Обрабатывает переход по ссылке активации.

        Args:
            request: HTTP-запрос.
            uidb64: Закодированный в base64 первичный ключ пользователя.
            token: Токен активации.

        Returns:
            HttpResponse: Редирект на логин при успехе или страница ошибки.
        """
        user = self._get_user(uidb64)

        if user is None or not default_token_generator.check_token(user, token):
            return render(request, "users/activation_invalid.html", status=400)

        if not user.is_active:
            user.is_active = True
            user.save(update_fields=["is_active"])

        messages.success(
            request,
            "Аккаунт активирован. Теперь можно войти.",
            extra_tags="users",
        )
        return redirect("users:login")

    @staticmethod
    def _get_user(uidb64: str) -> CustomUser | None:
        """Декодирует uidb64 и возвращает пользователя.

        Args:
            uidb64: Закодированный первичный ключ пользователя.

        Returns:
            CustomUser | None: Пользователь или None, если декодирование не удалось.
        """
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            return CustomUser.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
            return None


class CustomLoginView(LoginView):
    """Авторизация пользователя по email и паролю.

    Использует CustomAuthenticationForm с понятным сообщением для
    неактивного пользователя.
    """

    template_name = "users/login.html"
    authentication_form = CustomAuthenticationForm
    redirect_authenticated_user = True


class CustomLogoutView(LogoutView):
    """Выход пользователя из системы."""

    next_page = reverse_lazy("users:login")
