from __future__ import unicode_literals
from ..login.models import User
from django.db import models

# Create your models here.
# class SecretManager(models.Manager):


class Secret(models.Model):
    content = models.CharField(max_length=325)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    likes = models.ManyToManyField(User)
    # object = SecretManager()
