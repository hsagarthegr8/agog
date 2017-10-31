from django.conf.urls import url,include

from .views import UserCreateView,LoginView,LogoutView,activation, loginit

app_name = 'accounts'

urlpatterns = [
    url('^register/$',UserCreateView.as_view(),name='register'),
    url('^login/$',LoginView.as_view(),name='login'),
    url('^loginit/$', loginit, name='loginit' ),
    url('^logout/$',LogoutView.as_view(), name='logout'),
    url('^activate/(?P<username>[a-z,0-9]+)/(?P<activation_key>[\w]+)/$', activation, name='activate'),
]