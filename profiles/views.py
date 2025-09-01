from django.shortcuts import render, redirect
from django.views.generic import TemplateView, UpdateView
from .models import Profile
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
# Create your views here.
class UserProfileView(TemplateView):
    model = Profile
    template_name = 'profiles/profile.html'
class EditProfileView(UpdateView):
    model = Profile

@login_required
def profile_edit(request):
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("profile")  # go back to profile page
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, "profiles/profile_edit.html", {
        "user_form": user_form,
        "profile_form": profile_form,
    })