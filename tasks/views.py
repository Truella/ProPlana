from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'tasks/index.html'
    login_url = 'accounts/login/'
    redirect_field_name = 'next'