# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-08 10:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_quotation_creation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotation',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]