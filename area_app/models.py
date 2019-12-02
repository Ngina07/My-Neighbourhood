from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models import Q
import datetime as dt


# Priority=(
#     ('Informational','Informational'),
#     ('High Priority','High Priority'),
# )

class Hood(models.Model):
    hood = models.CharField (max_length= 100, default= 'Nairobi')

    def __str__(self):
        return self.hood

    

class Profile(models.Model):
    avatar = models.ImageField(upload_to='avatars/')
    description = HTMLField()
    hood = models.ForeignKey(Hood,on_delete=models.CASCADE)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class notifications(models.Model):
    title = models.CharField(max_length=100)
    notification = HTMLField()
    # priority = models.CharField(max_length=15,choices=Priority,default="Informational")
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    hood = models.ForeignKey(Hood,on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Business(models.Model):
    logo = models.ImageField(upload_to='businesslogo/')
    description = HTMLField()
    hood = models.ForeignKey(Hood,on_delete=models.CASCADE)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    email = models.EmailField()
    address =models.CharField(max_length=100)
    contact = models.CharField()

    def __str__(self):
        return self.name

class Authorities(models.Model):
    hood = models.ForeignKey(Hood,on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField()
    address =models.CharField(max_length=100)

    def __str__(self):
        return self.name
