from django.views.generic import DetailView, CreateView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404,redirect
from django.urls import reverse_lazy

User = get_user_model()
from .forms import ProfileForm


class TimelineView(LoginRequiredMixin,DetailView):
    model = User
    template_name = 'profiles/timeline.html'

    def get_object(self, queryset=None):
        return User.objects.get(username = self.request.user)


class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'profiles/profile.html'

    def get_object(self, queryset=None):
        username = self.kwargs.get('username')
        if username:
            return get_object_or_404(User,username=username)
        return User.objects.get(username=self.request.user)


class SettingsView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'profiles/settings.html'

    def get_object(self, queryset=None):
        return User.objects.get(username=self.request.user)


class CreateProfile(CreateView):
    form_class = ProfileForm
    success_url = reverse_lazy('profiles:timeline')
    template_name = 'profiles/createprofile.html'
