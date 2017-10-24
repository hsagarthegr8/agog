from django.conf.urls import url

from .views import TimelineView, ProfileView

app_name = 'profiles'

urlpatterns = [
    url('^timeline/$',TimelineView.as_view(),name='timeline'),
    url(r'^profile/(?P<username>[a-z,0-9]+)/$', ProfileView.as_view(), name='profile'),
    url(r'^profile/$', ProfileView.as_view(), name = 'profile'),
]