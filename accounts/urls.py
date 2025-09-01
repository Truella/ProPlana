from django.urls import path, include
from django.contrib.auth.views import (
    LoginView,
    PasswordChangeDoneView,
)
from .views import SignUpView, ChangePasswordView
from .forms import LoginForm

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path(
        "login/",
        LoginView.as_view(
            template_name="registration/login.html", authentication_form=LoginForm
        ),
        name="login",
    ),
    path(
        "password_change/",
        ChangePasswordView.as_view(),
        name="password-change",
    ),
    path(
        "password_change/done/",
        PasswordChangeDoneView.as_view(
            template_name="registration/password_change_done.html"
        ),
        name="password-change-done",
    ),
    path("", include("django.contrib.auth.urls")),
]
