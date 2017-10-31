from django.conf.urls import url
from .views import UserList, UserDetail, UserCreate

urlpatterns = [
    url(r'^users/$', UserList.as_view()),
    url(r'^users/new$',UserCreate.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', UserDetail.as_view()),
]