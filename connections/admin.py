from django.contrib import admin
from .models import Connections, BlockList

admin.site.register(Connections)
admin.site.register(BlockList)