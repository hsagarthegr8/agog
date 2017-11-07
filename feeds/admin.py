from django.contrib import admin

from .models import Post, Response, PostReactions, ResponseReactions

admin.site.register(Post)
admin.site.register(Response)
admin.site.register(PostReactions)
admin.site.register(ResponseReactions)
