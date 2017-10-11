from django.contrib import admin

from .models import Post, Comment, PostReactions, CommentReactions

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(PostReactions)
admin.site.register(CommentReactions)
