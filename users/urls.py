"""URL-маршрутизация приложения users."""

from django.urls import path

from .views import (
    ActivateView,
    ActivationSentView,
    CustomLoginView,
    CustomLogoutView,
    RegisterView,
)

app_name = "users"

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("activation-sent/", ActivationSentView.as_view(), name="activation_sent"),
    path("activate/<uidb64>/<token>/", ActivateView.as_view(), name="activate"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
]
