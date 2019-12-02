from __future__ import unicode_literals
from django.contrib import admin
from .models import *

admin.site.register(Hood)
admin.site.register(notifications)
admin.site.register(Business)
admin.site.register(Profile)
admin.site.register(Health)
admin.site.register(Authorities)