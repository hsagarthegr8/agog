from django.db import models
from django.db.models import Q
from django.db.models.signals import post_save
from django.conf import settings
from django.shortcuts import reverse
from django.dispatch import receiver
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

from feeds.models import Post
from .emails import ActivationEmail


class MyUserManager(BaseUserManager):
    def create_user(self, username, first_name, last_name, email, gender, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username= username,
            first_name = first_name,
            last_name = last_name,
            email=self.normalize_email(email),
            gender = gender,
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, first_name, last_name, email, gender, date_of_birth, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            gender=gender,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=40, unique=True,
                                help_text = 'Username can only contains alphabets and numbers')
    first_name = models.CharField(verbose_name='First Name',max_length=40,blank=False,null=False)
    last_name = models.CharField(verbose_name='Last Name',max_length=40,blank = True,)
    full_name = models.CharField(verbose_name='Full Name', max_length=100, null=True, blank=True)
    email = models.EmailField(verbose_name='email address',max_length=255,unique=True,)
    contact_no = models.CharField(verbose_name='Contact Number', max_length=10, null=True,unique=True)
    Gender = [('M','Male'),('F','Female')]
    gender = models.CharField(max_length=1,choices=Gender,null = False)
    date_of_birth = models.DateField(help_text='Date of Birth in the format yyyy-mm-dd')
    date_joined = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name','last_name','email','gender','date_of_birth']

    def save(self, *args, **kwargs):
        self.full_name = self.first_name +' '+self.last_name
        super(User, self).save(*args, **kwargs)

    def get_full_name(self):
        # The user is identified by their email address
        return self.first_name + ' ' + self.last_name

    def get_short_name(self):
        # The user is identified by their email address
        return self.first_name

    def __str__(self):              # __unicode__ on Python 2
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    def get_ratings(self):
        return self.userrating_set.aggregate(models.Avg('rating'))['rating__avg']

    def get_count(self):
        return self.userrating_set.all().count()

    def get_posts(self):
        return (self.post_set.all() | self.posted_on_set.all()).distinct()

    def get_connections(self):
        my_connections = set()
        my_connections.add(self)
        for connection in (self.connections_set.filter(is_active=True) | self.connection2_set.filter(is_active=True)):
            my_connections.add(connection.user1)
            my_connections.add(connection.user2)
        return my_connections

    def get_requests(self):
        requests = self.connection2_set.filter(is_active=False)
        return requests

    def get_request_user(self):
        a = set()
        for conn in self.get_requests():
            a.add(conn.user1)
        return a


    def get_timeline_posts(self):
        my_connections = self.get_connections()
        return Post.objects.filter(Q(posted_by__in=my_connections), Q(posted_on__in=my_connections))

    def get_absolute_url(self):
        return '/profile/{}/'.format(self.username)

    def get_blocked_users(self):
        users = []
        for blocks in self.blocklist.all():
            users.append(blocks.user2)
        return users

from django.utils.crypto import get_random_string


class Verification(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    activation_key = models.CharField(max_length=100, null=True,blank=True)

    def __str__(self):
        return self.user.username

    def get_activation_key(self):
        return get_random_string(length=100)

    def save(self, *args, **kwargs):
        self.activation_key = self.get_activation_key()
        super(Verification, self).save(*args, **kwargs)

    def send(self):
        activation_url = reverse('accounts:activate', kwargs={'username': self.user.username,
                                                              'activation_key': self.activation_key})
        domain = None
        if settings.DEBUG:
            domain = 'http://127.0.0.1:8000'
        else:
            domain = 'http://hsagar1706.pythonanywhere.com'

        activation_url = domain + activation_url
        context = {'username':self.user.username, 'activation_url' : activation_url}
        ActivationEmail(to = [self.user.email], url=activation_url).send()


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    if not instance.is_verified:
        try:
            v = Verification.objects.create(user = instance)
        except:
            pass



@receiver(post_save, sender=Verification)
def send_activation_email(sender, instance, **kwargs):
    instance.send()

