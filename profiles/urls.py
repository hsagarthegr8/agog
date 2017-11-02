from django.conf.urls import url

from .views import TimelineView, ProfileView, SettingsView, CreateProfile

app_name = 'profiles'

urlpatterns = [
    url('^timeline/$',TimelineView.as_view(),name='timeline'),
    url(r'^profile/(?P<username>\w+)/$', ProfileView.as_view(), name='profile'),
    url(r'^profile/$', ProfileView.as_view(), name = 'profile'),
    url(r'^settings/$', SettingsView.as_view(), name='settings'),
    url(r'^create-profile/$', CreateProfile.as_view(), name='create_profile'),
]