from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class UserRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rated_by_set')
    rating = models.SmallIntegerField()

    class Meta:
        unique_together = ('user', 'rated_by')


class Connections(models.Model):
    user1= models.ForeignKey(User,on_delete=models.CASCADE)
    user2= models.ForeignKey(User,on_delete=models.CASCADE,related_name='connection2_set')
    connections = [('FR','Friends'),('CO','Colleague'),('BA','Batchmates'), ('FA','Family')]
    connection_type = models.CharField(max_length=2,choices=connections)
    timestamp = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-timestamp']
        verbose_name_plural='Connections'
        unique_together = ['user1','user2']