# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-27 18:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0002_add_latitude_longitude_fields'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='communityenergygroup',
            options={'ordering': ('name',)},
        ),
    ]
