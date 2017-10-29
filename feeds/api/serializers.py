from rest_framework import serializers
from feeds.models import Post


class PostSerializer(serializers.ModelSerializer):
    posted_by = serializers.ReadOnlyField(source='posted_by.username')

    class Meta:
        model = Post
        fields = ('id','posted_by','posted_on','message','comment_set')
        depth = 2


