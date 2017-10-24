from django.conf.urls import url

from .views import ConnectionView, accept_request, delete_request, new_request

app_name = 'connections'

urlpatterns = [

    url(r'^connect/(?P<id>[0-9]+)/accept$', accept_request, name='accept_request'),
    url(r'^connect/(?P<id>[0-9]+)/delete$', delete_request, name='delete_request'),
    url(r'^connect/(?P<username>[a-z,0-9]+)/new$', new_request, name='new_request'),
    url(r'^connections/(?P<username>[a-z,0-9]+)/$', ConnectionView.as_view(), name='connection'),
    url(r'^connections/$', ConnectionView.as_view(), name = 'connection'),
]