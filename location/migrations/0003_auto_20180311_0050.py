# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-11 00:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_auto_20180311_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='phone',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
