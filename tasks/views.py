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


class ProjectView(LoginRequiredMixin, ListView):
    model = Project
    template_name = "tasks/projects.html"

    def get_queryset(self):
        projects = Project.objects.filter(owner=self.request.user)
        for project in projects:
            print(f"Project: {project.name}")
            print(f"is_completed: {project.is_completed}")
            print(f"is_overdue: {project.is_overdue}")  
            print(f"Condition 1 (completed): {project.is_completed}")
            print(f"Condition 2 (overdue & not completed): {project.is_overdue and not project.is_completed}")

            if project.is_completed:
                project.bg_color = "bg-green-50"
                project.border_color = "border-green-200"
                print(f"Applied GREEN background")
            elif project.is_overdue and not project.is_completed: 
                project.bg_color = "bg-red-50"
                project.border_color = "border-red-200"
                print(f"Applied RED background")
            else:  # Active projects
                project.bg_color = "bg-blue-50"
                project.border_color = "border-blue-200"
                print(f"Applied BLUE background")

            print(f"Final bg_color: {project.bg_color}")
            print("---")
        return projects


class CreateProjectView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = "tasks/project_form.html"
    success_url = reverse_lazy("projects")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = "tasks/project_detail.html"
    context_object_name = "project"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.get_object()
        completed = project.tasks.filter(is_completed=True).count()
        pending = project.tasks.filter(is_completed=False).count()
        context["completed_count"] = completed
        context["pending_count"] = pending
        return context


class UpdateProjectView(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy("projects")


class DeleteProjectView(LoginRequiredMixin, DeleteView):
    model = Project
    success_url = reverse_lazy("projects")


# Task related views>>>>>
"""class TaskListView(ListView):
    model = Task
    template_name = 'tasks/tasks_list.html'
    def get_queryset(self):
        return Project.objects.filter(owner = self.request.user)"""


class TaskCreateView(LoginRequiredMixin, CreateView):
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["project"] = get_object_or_404(Project, pk=self.kwargs["pk"])
        return context


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["project"] = get_object_or_404(Project, pk=self.kwargs["project_pk"])
        return context
