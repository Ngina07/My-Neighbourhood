# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-02 10:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('area_app', '0002_business_notifications'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifications',
            name='priority',
            field=models.CharField(choices=[('Informational', 'Informational'), ('High Priority', 'High Priority')], default='Informational', max_length=15),
        ),
    ]