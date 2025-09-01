# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import  CreateView
from .forms import SignUpForm, ChangePasswordForm
from django.contrib.auth import views as authviews

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"
class ChangePasswordView(authviews.PasswordChangeView):
    form_class = ChangePasswordForm
    template_name="registration/password_change_form.html"