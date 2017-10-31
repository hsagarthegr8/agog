from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly


from feeds.models import Post
from .serializers import PostSerializer


class PostList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(posted_by=self.request.user)


class PostDetail(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class TimelinePosts(ListCreateAPIView):
    def get_queryset(self):
        return self.request.user.get_timeline_posts()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(posted_by=self.request.user,message=self.request.POST['message'],posted_on = self.request.user)



