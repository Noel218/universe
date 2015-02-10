#-*- coding:utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from registration.signals import user_registered

class ExUserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    is_human = models.BooleanField()

    def __unicode__(self):
        return self.user

def user_registered_callback(sender, user, request, **kwargs):
    profile = ExUserProfile(user = user)
    profile.is_human = bool(request.POST["is_human"])
    profile.save()

user_registered.connect(user_registered_callback)