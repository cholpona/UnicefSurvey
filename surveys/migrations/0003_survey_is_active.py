# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-27 06:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0002_remove_poll_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]