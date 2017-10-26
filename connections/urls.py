from django.conf.urls import url

from .views import (ConnectionView, accept_request, delete_request,
                    new_request, delete_connection, block_user,
                    unblock_user)

app_name = 'connections'

urlpatterns = [

    url(r'^connections/accept$', accept_request, name='accept_request'),
    url(r'^connect/delete$', delete_request, name='delete_request'),
    url(r'^connect/(?P<username>[a-z,0-9]+)/new$', new_request, name='new_request'),
    url(r'^connections/(?P<username>[a-z,0-9]+)/$', ConnectionView.as_view(), name='connection'),
    url(r'^connections/$', ConnectionView.as_view(), name = 'connection'),
    url(r'^connections/delete$', delete_connection, name = 'delete_connection'),
    url(r'^connections/block$', block_user, name='block_user'),
    url(r'^connections/unblock', unblock_user, name='unblock_user')
]