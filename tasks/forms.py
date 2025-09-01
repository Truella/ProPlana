# tasks/forms.py
from django import forms
from .models import Project, Task
from common.form_helpers import INPUT_STYLE_ATTR


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            "name",
            "description",
            "due_date",
        ]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    **INPUT_STYLE_ATTR,
                    "placeholder": "Enter project name",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    **INPUT_STYLE_ATTR,
                    "rows": 4,
                    "style":"resize:none",
                    "placeholder": "Enter description",
                }
            ),
            "due_date": forms.DateInput(
                attrs={
                    "type": "date",
                    **INPUT_STYLE_ATTR,
                }
            ),
        }


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "title",
            "description",
            "due_date",
        ]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    **INPUT_STYLE_ATTR,
                    "placeholder": "Enter task name",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    **INPUT_STYLE_ATTR,
                    "rows": 4,
                    "placeholder": "Enter description",
                }
            ),
            "due_date": forms.DateInput(
                attrs={
                    "type": "date",
                    **INPUT_STYLE_ATTR,
                }
            ),
        }
