# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-02 10:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('area_app', '0004_hood_hood'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hood',
            name='hood',
            field=models.CharField(default='Nairobi', max_length=100),
        ),
    ]