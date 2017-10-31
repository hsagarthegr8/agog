from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token,verify_jwt_token

urlpatterns = [
    url(r'^auth-token/', obtain_jwt_token, name='auth-token'),
    url(r'^token-refresh/', refresh_jwt_token, name='refresh_token'),
    url(r'^token-verify/', verify_jwt_token, name='verify_token'),
]