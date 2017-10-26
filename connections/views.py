from django.views.generic import DetailView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404,redirect,reverse
from django.db.models import Q

from .models import Connections, BlockList

User = get_user_model()


class ConnectionView(LoginRequiredMixin,DetailView):
    model = User
    template_name = 'connections/connections.html'

    def get_object(self, queryset=None):
        username = self.kwargs.get('username')
        if username:
            return get_object_or_404(User,username=username)
        return User.objects.get(username=self.request.user)


def accept_request(request):
    next = request.POST.get('next')
    id = request.POST.get('id')
    con = get_object_or_404(Connections,id=id)
    con.is_active = True
    con.save()
    return redirect(next)


def delete_request(request):
    next = request.POST.get('next')
    id = request.POST.get('id')
    con = get_object_or_404(Connections,id=id)
    con.delete()
    return redirect(next)


def new_request(request,username):
    user2 = get_object_or_404(User,username=username)
    user1 = request.user
    Connections.objects.create(user1=user1, user2=user2, connection_type='FR')
    return redirect(reverse('profiles:profile',kwargs={'username':username}))


def delete_connection(request):
    next = request.POST.get('next')
    id = request.POST.get('id')
    conn = get_object_or_404(Connections,id=id)
    conn.delete()
    return redirect(next)


def block_user(request):
    next = request.POST.get('next')
    user1 = get_object_or_404(User, username = request.POST.get('user1'))
    user2 = get_object_or_404(User, username = request.POST.get('user2'))
    try:
        conn = Connections.objects.get(Q(user1=user1, user2=user2) | Q(user1=user2, user2=user1))
        conn.delete()
    except:
        pass
    BlockList.objects.create(user1=user1, user2=user2)
    return redirect(next)


def unblock_user(request):
    next = request.POST.get('next')
    blockd = get_object_or_404(BlockList, id=request.POST.get('id'))
    blockd.delete()
    return redirect(next)
