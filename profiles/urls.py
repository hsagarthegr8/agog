from django.conf.urls import url

from .views import TimelineView

app_name = 'profiles'

urlpatterns = [
    url('^timeline/$',TimelineView.as_view(),name='timeline'),
]