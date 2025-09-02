from django.utils import timezone
from django.db import models
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404, redirect

# Create your models here.

durationchoice = [
    ("default", "Select duration"),
    (
        "one ",
        "1 week",
    ),
    (
        "two",
        "2 weeks",
    ),
    (
        "three",
        "3 weeks",
    ),
    (
        "four",
        "1 Month",
    ),
]

User = get_user_model()


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True, null=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    @property
    def is_overdue(self):
        """Return True if project has a due date and it's already past."""
        return self.due_date and self.due_date < timezone.now().date()

    def check_completion(self):
        """Update project completion status based on its tasks"""
        if self.tasks.exists() and all(task.is_completed for task in self.tasks.all()):
            self.is_completed = True
            self.is_active = False
        else:
            self.is_completed = False
            self.is_active = True
        self.save()

    def progress_percentage(self):
        total_tasks = self.tasks.count()
        completed_tasks = self.tasks.filter(is_completed=True).count()
        return (completed_tasks / total_tasks) * 100 if total_tasks > 0 else 0


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    due_date = models.DateField(null=True, blank=True)
    project = models.ForeignKey(
        "Project", on_delete=models.CASCADE, related_name="tasks"
    )
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """Override save to auto-update project status"""
        super().save(*args, **kwargs)
        self.project.check_completion()


@require_POST
def toggle_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = not task.is_completed
    task.save()
    return redirect("project-detail", pk=task.project.pk)
