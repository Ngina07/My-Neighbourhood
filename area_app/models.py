from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models import Q
import datetime as dt

class Hood(models.Model):
    hood = models.CharField(max_length=100)

    def __str__(self):
        return self.hood

    def save_hood(self):
        self.save()

    @classmethod
    def hood(cls,Hood):
        cls.objects.filter(hood=hood).delete()

class Profile(models.Model):
    avatar = models.ImageField(upload_to='avatars/')
    description = HTMLField()
    hood = models.ForeignKey(Hood,on_delete=models.CASCADE)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name