from datetime import timezone
from django.contrib.auth.models import AbstractUser
from datetime import timezone
from django.db import models


class CustomUser(models.Model):
    is_admin = models.BooleanField('Showroom status', default=False)
    is_user = models.BooleanField('user status', default=False)
    username = models.CharField(max_length=200, default='')
    password = models.CharField(max_length=200, default='')


class Compose(models.Model):
    to = models.CharField(max_length=200, default='')
    subject = models.CharField(max_length=200, default='')
    message = models.TextField(max_length=5000, default='')


class Inbox(models.Model):
    to = models.CharField(max_length=1000, default='')
    subject = models.CharField(max_length=200, default='')
    message = models.TextField(max_length=100000, default='')
    fromm = models.CharField(max_length=200, default='')


class Outbox(models.Model):
    fromm = models.CharField(max_length=200, default='')
    subject = models.CharField(max_length=200, default='')
    message = models.TextField(max_length=5000, default='')


class Draft(models.Model):
    to = models.CharField(max_length=200, default='')
    subject = models.CharField(max_length=200, default='')
    message = models.TextField(max_length=5000, default='')


class Customer(models.Model):
    first_name = models.CharField(max_length=200, default='')
    last_name = models.CharField(max_length=200, default='')
    contact = models.CharField(max_length=200, default='')
    email = models.CharField(max_length=200, default='')


class Notification(models.Model):
    note = models.IntegerField(default=0)
