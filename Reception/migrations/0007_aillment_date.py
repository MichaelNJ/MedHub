# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-16 06:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Reception', '0006_aillment'),
    ]

    operations = [
        migrations.AddField(
            model_name='aillment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 16, 6, 9, 6, 487809, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
