# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-08 10:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_auto_20181008_1012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quotation',
            name='creation_date',
        ),
        migrations.RemoveField(
            model_name='quotation',
            name='limit_date',
        ),
        migrations.AlterField(
            model_name='quotation',
            name='status',
            field=models.IntegerField(blank=True, choices=[(1, 'devis en cours'), (2, 'devis annul\xe9'), (3, 'facture'), (4, 'facture r\xe9gl\xe9e')], null=True),
        ),
    ]
