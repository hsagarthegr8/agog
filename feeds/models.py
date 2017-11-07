from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

from activityfeeds.models import log


class Post(models.Model):
    posted_by = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='Posted By',related_name='post_set')
    posted_on = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='Posted On',related_name='posted_on_set')
    message = models.TextField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-timestamp','-updated']

    def save(self, *args, **kwargs):
        if not self.id:
            log(user1=self.posted_by, user2=self.posted_on, action='Posted')
        else:
            log(user1=self.posted_by, user2=self.posted_on, action='Updated Post')
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.posted_by.username +' - '+ self.message


class Response(models.Model):
    responded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    response = models.TextField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.id:
            log(user1=self.responded_by, user2=self.post.posted_on, action='Responded')
        else:
            log(user1=self.responded_by, user2=self.post.posted_on, action='Updated Response')
        super(Response, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.post) +' - '+ self.responded_by.username +' - ' + self.response


class PostReactions(models.Model):
    CHOICES = (('A','Angry'),
               ('S','Sad'),
               ('W','Wow'),
               ('H','Haha'),
               ('L','Love'))
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    reacted_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['post','reacted_by']
        verbose_name_plural='Post Reactions'


class ResponseReactions(models.Model):
    CHOICES = (('A','Angry'),
               ('S','Sad'),
               ('W','Wow'),
               ('H','Haha'),
               ('L','Love'))
    response = models.ForeignKey(Response, on_delete=models.CASCADE)
    reacted_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['response','reacted_by']
        verbose_name_plural = 'Response Reactions'
