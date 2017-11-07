
from django.conf.urls import url,include

from .views import add_post, add_response, delete_post, delete_response

app_name = 'feeds'

urlpatterns = [
    url(r'^post/(?P<username>[a-z,0-9]+)/new/$', add_post, name='add_post'),
    url(r'^response/new/$', add_response, name='add_response'),
    url(r'^post-delete/$', delete_post, name='delete_post'),
    url(r'^response-delete/$', delete_response, name='delete_response'),
]