from __future__ import unicode_literals

from django.db import models

# Create your models here.
class SecretManage(models.Manager):


class Secret(models.Model):
    content = models.Charfield(max_length=325)
    created_at = models.DateTimeField(auto_add_now = True)
    updated_at = models.DateTimeField(auto_add = True)
    object = SecretManager()