# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-27 11:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0003_survey_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer',
            field=models.CharField(choices=[(b'yes', b'Yes'), (b'no', b'No'), (b'maybe', b'Maybe')], max_length=120),
        ),
    ]
