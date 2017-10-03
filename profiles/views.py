from django.views.generic import DetailView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin

User = get_user_model()


class TimelineView(LoginRequiredMixin,DetailView):
    model = User
    template_name = 'profiles/timeline.html'

    def get_object(self, queryset=None):
        return User.objects.get(username = self.request.user)