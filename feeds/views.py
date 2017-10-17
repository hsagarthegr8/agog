from django.shortcuts import redirect, reverse,get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model

from .models import Post, Comment

User = get_user_model()


def add_post(request,username):
    posted_by = request.user
    posted_on = User.objects.get(username=username)
    message = request.POST['message']
    Post.objects.create(posted_by=posted_by, posted_on=posted_on, message=message)
    next = request.POST.get('next', '/')
    return HttpResponseRedirect(next)


def delete_post(request):
    post_id = int(request.POST['post'])
    post = Post.objects.get(id=post_id)
    post.delete()
    next = request.POST.get('next', '/')
    return HttpResponseRedirect(next)


def add_comment(request):
    post_id = int(request.POST['post'])
    post = Post.objects.get(id=post_id)
    comment = request.POST['comment']
    Comment.objects.create(commented_by=request.user,post=post,comment=comment)
    next = request.POST.get('next', '/')
    return HttpResponseRedirect(next)


def delete_comment(request):
    comment_id = int(request.POST['comment'])
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    next = request.POST.get('next', '/')
    return HttpResponseRedirect(next)