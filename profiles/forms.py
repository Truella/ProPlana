# accounts/forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Profile
from common.form_helpers import INPUT_STYLE_ATTR


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]
        widgets = {
            "username": forms.TextInput(
                attrs={
                    **INPUT_STYLE_ATTR,
                    "placeholder": "Enter new username",
                }
            ),
            "first_name": forms.TextInput(
                attrs={
                    **INPUT_STYLE_ATTR,
                    "placeholder": "Enter new first name",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    **INPUT_STYLE_ATTR,
                    "placeholder": "Enter new last name",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    **INPUT_STYLE_ATTR,
                    "placeholder": "Enter email address",
                }
            ),
        }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [ "role", "contact"]
        widgets = {
            "role": forms.TextInput(
                attrs={
                    **INPUT_STYLE_ATTR,
                    "placeholder": "Enter your role",
                }
            ),
            "contact": forms.TextInput(
                attrs={
                    **INPUT_STYLE_ATTR,
                    "placeholder": "Enter contact information",
                }
            ),
        }
