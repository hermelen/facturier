# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-08 11:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20181008_0753'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotation',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
