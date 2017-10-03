from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class UserRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rated_by_set')
    rating = models.SmallIntegerField()

    class Meta:
        unique_together = ('user', 'rated_by')