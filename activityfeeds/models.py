from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericForeignKey

from django.contrib.contenttypes.models import ContentType

import jsonfield

from .signals import event_logged


class Log(models.Model):

    user1 = models.ForeignKey(
        getattr(settings, "AUTH_USER_MODEL", "auth.User"),
        null=True,
        on_delete=models.CASCADE, related_name='user1'
    )
    user2 = models.ForeignKey(
        getattr(settings, "AUTH_USER_MODEL", "auth.User"),
        null=True,
        on_delete=models.CASCADE, related_name='user2'
    )
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)
    action = models.CharField(max_length=50, db_index=True)
    read = models.BooleanField(default=False)
    content_type = models.ForeignKey(ContentType, null=True)
    object_id = models.PositiveIntegerField(null=True)
    obj = GenericForeignKey("content_type", "object_id")
    extra = jsonfield.JSONField()

    @property
    def template_fragment_name(self):
        return "pinax/eventlog/{}.html".format(self.action.lower())

    class Meta:
        ordering = ["-timestamp"]


def log(user1, user2, action, extra=None, obj=None, dateof=None):
    if user1 is not None and not user1.is_authenticated():
        user1 = None
    if user2 is not None and not user2.is_authenticated():
        user2 = None
    if extra is None:
        extra = {}
    content_type = None
    object_id = None
    if obj is not None:
        content_type = ContentType.objects.get_for_model(obj)
        object_id = obj.pk
    if dateof is None:
        dateof = timezone.now()

    event = Log.objects.create(
        user1=user1,
        user2=user2,
        action=action,
        extra=extra,
        content_type=content_type,
        object_id=object_id,
        timestamp=dateof
    )
    event_logged.send(sender=Log, event=event)
    return event
