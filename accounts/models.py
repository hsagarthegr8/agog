from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


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
    username = models.CharField(max_length=40,unique=True)
    first_name = models.CharField(verbose_name='First Name',max_length=40,blank=False,null=False)
    last_name = models.CharField(verbose_name='Last Name',max_length=40,blank = True,)
    email = models.EmailField(verbose_name='email address',max_length=255,unique=True,)
    Gender = [('M','Male'),('F','Female')]
    gender = models.CharField(max_length=1,choices=Gender,null = False)
    date_of_birth = models.DateField()
    date_joined = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name','last_name','email','gender','date_of_birth']

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