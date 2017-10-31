from django.conf.urls import url
from .views import PostList, PostDetail, TimelinePosts

urlpatterns = [
    url(r'^posts/$', PostList.as_view()),
    url(r'^posts/(?P<pk>[0-9]+)/$', PostDetail.as_view()),
    url(r'^timeline-posts/$', TimelinePosts.as_view(),name='CR-timeline_post'),
]