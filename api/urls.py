from django.conf.urls import url,include

app_name = 'api'

urlpatterns = [
    url(r'^auth/',include('api.auth.urls',namespace='auth')),
    url(r'^accounts/',include('api.accounts.urls',namespace='accounts')),
    url(r'^feeds/', include('api.feeds.urls',namespace='feeds')),
]