from django.shortcuts import redirect, reverse
from django.contrib.auth import get_user_model

from .models import Post, Comment

User = get_user_model()


def add_post(request,username):
    posted_by = request.user
    posted_on = User.objects.get(username=username)
    message = request.POST['message']
    redirect_to = request.POST['redirect_to']
    Post.objects.create(posted_by=posted_by, posted_on=posted_on, message=message)
    if redirect_to == 'profile':
        return redirect(reverse('profiles:profile', kwargs={'username': posted_on.username}))
    return redirect(reverse('profiles:timeline'))


def add_comment(request, username):
    post_id = int(request.POST['post'])
    post = Post.objects.get(id=post_id)
    comment = request.POST['comment']
    Comment.objects.create(commented_by=request.user,post=post,comment=comment)
    if request.POST['redirect_to'] == 'profile':
        return redirect(reverse('profiles:profile', kwargs={'username': username}))
    return redirect(reverse('profiles:timeline'))

