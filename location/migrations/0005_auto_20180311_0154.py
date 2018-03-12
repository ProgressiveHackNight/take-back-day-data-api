# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-11 01:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0004_auto_20180311_0151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='location_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterUniqueTogether(
            name='place',
            unique_together=set([('location_name', 'street_address')]),
        ),
    ]