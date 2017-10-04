from django.conf.urls import url

from .views import UserCreateView,LoginView,LogoutView,activation

app_name = 'accounts'

urlpatterns = [
    url('^register/$',UserCreateView.as_view(),name='register'),
    url('^login/$',LoginView.as_view(),name='login'),
    url('^logout/$',LogoutView.as_view(), name='logout'),
    url('^activate/(?P<username>[a-z,0-9]+)/(?P<activation_key>[\w]+)/$', activation, name='activate')
]