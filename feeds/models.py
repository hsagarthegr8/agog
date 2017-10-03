from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Post(models.Model):
    posted_by = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='Posted By',related_name='post_set')
    posted_on = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='Posted On',related_name='posted_on_set')
    message = models.TextField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-timestamp','-updated']
    def __str__(self):
        return self.posted_by.username +' - '+ self.message

    def get_ratings(self):
        return self.postrating_set.aggregate(models.Avg('rating'))['rating__avg']

    def get_count(self):
        return self.postrating_set.all().count()


class Comment(models.Model):
    commented_by = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    comment = models.TextField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.post) +' - '+ self.commented_by.username +' - ' + self.comment


class PostRating(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    rated_by = models.ForeignKey(User,on_delete=models.CASCADE)
    rating = models.SmallIntegerField()

    class Meta:
        unique_together = ('post','rated_by')