from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    image = models.ImageField(blank=True)
    lives_in = models.CharField(max_length=120,blank=True)
    hometown = models.CharField(max_length=120,blank=True)
    RELATIONSHIP = [('S','Single'),('I','In a Relationship')]
    relationship = models.CharField(max_length=1, choices=RELATIONSHIP,blank=True)
    interests = models.TextField(max_length=300,blank=True)
    about = models.TextField(max_length=500,blank=True)

    def __str__(self):
        return self.user.username


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