# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-08 10:55
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_auto_20181008_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=autoslug.fields.AutoSlugField(blank=True, editable=False, null=True, populate_from='full_name', unique=True, verbose_name='Slug'),
        ),
    ]
