from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Project, Task
from django.urls import reverse, reverse_lazy
from .forms import ProjectForm, TaskForm


# Create your views here.
class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "tasks/index.html"
    login_url = "/accounts/login/"
    redirect_field_name = "next"


class ProjectView(ListView):
    model = Project
    template_name = "tasks/projects.html"

    COLORS = [
        ("bg-yellow-100", "bg-yellow-600"),
        ("bg-green-100", "bg-green-600"),
        ("bg-blue-100", "bg-blue-600"),
        ("bg-pink-100", "bg-pink-600"),
        ("bg-purple-100", "bg-purple-600"),
        ("bg-orange-100", "bg-orange-600"),
    ]

    def get_queryset(self):
        projects = Project.objects.filter(owner=self.request.user)
        for i, project in enumerate(projects):
            bg_card, btn_color = self.COLORS[i % len(self.COLORS)]
            project.bg_color = bg_card      # pastel card color
            project.btn_color = btn_color   # solid button color
        return projects


class CreateProjectView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = "tasks/project_form.html"
    success_url = reverse_lazy("projects")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProjectDetailView(DetailView):
    model = Project
    template_name = "tasks/project_detail.html"


class UpdateProjectView(UpdateView):
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy("projects")


class DeleteProjectView(DeleteView):
    model = Project
    success_url = reverse_lazy("projects")


# Task related views>>>>>
"""class TaskListView(ListView):
    model = Task
    template_name = 'tasks/tasks_list.html'
    def get_queryset(self):
        return Project.objects.filter(owner = self.request.user)"""


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        project = Project.objects.get(pk=self.kwargs["pk"])
        form.instance.project = project
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("project-detail", kwargs={"pk": self.kwargs["pk"]})


class TaskUpdateView(UpdateView):
    model = Task
    fields = ["title", "description", "due_date"]
    template_name = "tasks/task_form.html"
    
    
    def get_object(self, queryset=None):
        """
        Override default behavior:
        Only return the task if it belongs to the given project.
        """
        project_id = self.kwargs.get("project_pk")
        task_id = self.kwargs.get("task_pk")
        return get_object_or_404(Task, pk=task_id, project__pk=project_id)
    def get_success_url(self):
        return reverse("project-detail", kwargs={"pk": self.kwargs["project_pk"]})

