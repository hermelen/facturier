# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-08 11:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_quotation_creation_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotation',
            name='edition_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='quotation',
            name='limit_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]