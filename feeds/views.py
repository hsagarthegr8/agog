from django.shortcuts import redirect, reverse,get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model

from .models import Post, Response

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


def add_response(request):
    post_id = int(request.POST['post'])
    post = Post.objects.get(id=post_id)
    response = request.POST['response']
    Response.objects.create(responded_by=request.user,post=post,response=response)
    next = request.POST.get('next', '/')
    return HttpResponseRedirect(next)


def delete_response(request):
    response_id = int(request.POST['response'])
    response = Response.objects.get(id=response_id)
    response.delete()
    next = request.POST.get('next', '/')
    return HttpResponseRedirect(next)