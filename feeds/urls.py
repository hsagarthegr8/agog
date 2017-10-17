
from django.conf.urls import url

from .views import add_post, add_comment, delete_post, delete_comment

app_name = 'feeds'

urlpatterns = [
    url(r'^post/(?P<username>[a-z,0-9]+)/new/$', add_post, name='add_post'),
    url(r'^comment/new/$', add_comment, name='add_comment'),
    url(r'^post-delete/$', delete_post, name='delete_post'),
    url(r'^comment-delete/$', delete_comment, name='delete_comment'),

]