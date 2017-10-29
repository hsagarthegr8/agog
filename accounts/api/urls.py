from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token,verify_jwt_token
from .views import UserList, UserDetail, UserCreate

urlpatterns = [
    url(r'^users/$', UserList.as_view()),
    url(r'^users/new$',UserCreate.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', UserDetail.as_view()),
    url(r'^auth-token/', obtain_jwt_token),
    url(r'^token-refresh/', refresh_jwt_token),
    url(r'^token-verify/', verify_jwt_token),
]