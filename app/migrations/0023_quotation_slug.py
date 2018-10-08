# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-08 11:59
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_auto_20181008_1150'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotation',
            name='slug',
            field=autoslug.fields.AutoSlugField(blank=True, editable=False, null=True, populate_from='full_name', unique=True, verbose_name='Slug'),
        ),
    ]
