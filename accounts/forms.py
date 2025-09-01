# accounts/forms.py
from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    PasswordChangeForm,
)
from django.contrib.auth.models import User
from common.form_helpers import INPUT_STYLE_ATTR


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                **INPUT_STYLE_ATTR,
                "placeholder": "Username",
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={**INPUT_STYLE_ATTR, "placeholder": "Password"}
        )
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                **INPUT_STYLE_ATTR,
                "placeholder": "Username",
            }
        )
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                **INPUT_STYLE_ATTR,
                "placeholder": "Email address",
            }
        ),
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={**INPUT_STYLE_ATTR, "placeholder": "Password"}
        ),
        label="Enter Password",
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={**INPUT_STYLE_ATTR, "placeholder": "Confirm Password"}
        ),
        label="Confirm Password",
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                **INPUT_STYLE_ATTR,
                "placeholder": "Enter old password",
            }
        ),
        label="Old Password",
    )

    new_password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={**INPUT_STYLE_ATTR, "placeholder": "Enter new password"}
        ),
        label="New Password",
    )

    new_password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={**INPUT_STYLE_ATTR, "placeholder": "Confirm new password"}
        ),
        label="Confirm new Password",
    )
