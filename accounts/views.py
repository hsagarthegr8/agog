from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView as UserLoginView
from django.contrib.auth.views import LogoutView as UserLogoutView
from django.core.urlresolvers import reverse_lazy

from .forms import UserCreationForm

class UserCreateView(CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')


class LoginView(UserLoginView):
    template_name = 'accounts/login.html'


class LogoutView(UserLogoutView):
    next_page = '/accounts/login/'