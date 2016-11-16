from __future__ import unicode_literals
from ..login.models import User
from django.db import models

class SecretManager(models.Manager):
    def post_secret(self, request):
        errors = []

        if not request.POST['new_secret']:
            errors.append('Please write a secret!')

        else:
            creator = User.objects.get(id=request.session['user']['user_id'])
            self.create(content=request.POST['new_secret'], secret_creator=creator)

        return errors

    def destroy_secret(self, request, id):
        putitin = Secret.objects.filter(id=id).delete()

    def like_secret(self,request, id):
        user = User.objects.get(id=request.session['user']['user_id'])
        secret = Secret.objects.get(id=id)
        secret.likes.add(user)

class Secret(models.Model):
    content = models.CharField(max_length=325)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    secret_creator = models.ForeignKey(User, related_name = 'user_secret')
    likes = models.ManyToManyField(User, related_name = 'user_likes')
    objects = SecretManager()
