from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView as UserLoginView
from django.contrib.auth.views import LogoutView as UserLogoutView
from django.core.urlresolvers import reverse_lazy,reverse
from django.contrib.auth import authenticate, login

from .forms import UserCreationForm
from .models import Verification, User


class UserCreateView(CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')


class LoginView(UserLoginView):
    template_name = 'accounts/login.html'


class LogoutView(UserLogoutView):
    next_page = '/accounts/login/'

def activation(request,username,activation_key):
    user = get_object_or_404(User,username=username)
    obj = get_object_or_404(Verification,user= user)
    user.is_verified = True
    user.save()
    obj.delete()
    return redirect(reverse_lazy('accounts:login'))

def loginit(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request,user)
            return redirect(reverse('profiles:timeline'))

    return redirect(reverse('home'))