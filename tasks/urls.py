from django.urls import path

from tasks.models import toggle_task
from .views import (
    HomeView,
    ProjectView,
    CreateProjectView,
    ProjectDetailView,
    UpdateProjectView,
    DeleteProjectView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
)

urlpatterns = [
    path("dashboard/", HomeView.as_view(), name="home"),
    path("projects/", ProjectView.as_view(), name="projects"),
    path("projects/new/", CreateProjectView.as_view(), name="create-project"),
    path("projects/<int:pk>/", ProjectDetailView.as_view(), name="project-detail"),
    path("projects/<int:pk>/edit/", UpdateProjectView.as_view(), name="project-update"),
    path(
        "projects/<int:pk>/delete/", DeleteProjectView.as_view(), name="project-delete"
    ),
    path("projects/<int:pk>/task/new", TaskCreateView.as_view(), name="create-task"),
    path(
        "projects/<int:project_pk>/task/<int:task_pk>/edit",
        TaskUpdateView.as_view(),
        name="edit-task",
    ),
    path("tasks/<int:pk>/toggle/", toggle_task, name="toggle-task"),
    path(
        "projects/<int:project_pk>/task/<int:task_pk>/delete/",
        TaskDeleteView.as_view(),
        name="delete-task",
    ),
]
