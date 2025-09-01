from django.urls import path
from .views import UserProfileView, profile_edit

urlpatterns = [
    path("profile/", UserProfileView.as_view(), name="profile"),
    path("profile/edit-profile/", profile_edit, name="profile-edit"),
    
]
