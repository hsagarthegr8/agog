from django.views.generic import DetailView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404,redirect,reverse

User = get_user_model()


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