# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-26 13:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_auto_20160326_1145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='city',
        ),
        migrations.DeleteModel(
            name='Location',
        ),
    ]