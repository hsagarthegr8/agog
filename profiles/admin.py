from django.contrib import admin

from .models import UserRating, Connections, Profile

admin.site.register(UserRating)
admin.site.register(Connections)
admin.site.register(Profile)