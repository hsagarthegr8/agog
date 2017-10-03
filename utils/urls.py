from django.conf.urls import url
from .views import SearchView

app_name = 'utils'

urlpatterns = [
    url('^search/$',SearchView.as_view(),name='search'),
]