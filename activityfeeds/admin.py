from django.contrib import admin

from .models import Log


class LogAdmin(admin.ModelAdmin):

    raw_id_fields = ["user1","user2"]
    list_filter = ["action", "timestamp"]
    list_display = ["timestamp", "user1", "user2", "action", "extra"]
    search_fields = ["user1__username", "user1__email", "extra"]


admin.site.register(Log, LogAdmin)
from django.contrib import admin

# Register your models here.
