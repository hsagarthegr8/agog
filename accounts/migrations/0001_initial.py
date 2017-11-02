# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-02 04:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(help_text='Username can only contains alphabets and numbers', max_length=40, unique=True)),
                ('first_name', models.CharField(max_length=40, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=40, verbose_name='Last Name')),
                ('full_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Full Name')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('contact_no', models.CharField(max_length=10, unique=True, verbose_name='Contact Number')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('date_of_birth', models.DateField(help_text='Date of Birth in the format yyyy-mm-dd')),
                ('date_joined', models.DateField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_verified', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Verification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activation_key', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
