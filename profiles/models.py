from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from pyuploadcare.dj.models import ImageField


from utils.utils import get_image_path

User = settings.AUTH_USER_MODEL


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = ImageField(blank=True, manual_crop="1:1")
    lives_in = models.CharField(max_length=120,blank=True)
    hometown = models.CharField(max_length=120,blank=True)
    RELATIONSHIP = [('S','Single'),('I','In a Relationship')]
    relationship = models.CharField(max_length=1, choices=RELATIONSHIP,blank=True)
    interests = models.TextField(max_length=300,blank=True)
    about = models.TextField(max_length=500,blank=True)

    def __str__(self):
        return self.user.username




