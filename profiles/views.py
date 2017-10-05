from django.views.generic import DetailView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404,redirect,reverse

User = get_user_model()

from .models import Connections


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


def accept_request(request,id):
    con = get_object_or_404(Connections,id=id)
    con.is_active = True
    con.save()
    return redirect(reverse('profiles:profile'))


def delete_request(request,id):
    con = get_object_or_404(Connections,id=id)
    con.delete()
    return redirect(reverse('profiles:profile'))

def new_request(request,username):
    user2 = get_object_or_404(User,username=username)
    user1 = request.user
    Connections.objects.create(user1=user1, user2=user2, connection_type='FR')
    return redirect(reverse('profiles:profile',kwargs={'username':username}))
