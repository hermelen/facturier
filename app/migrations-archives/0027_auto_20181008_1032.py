# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-08 10:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_auto_20181008_1028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quotation',
            name='creation_date',
        ),
        migrations.AlterField(
            model_name='quotation',
            name='status',
            field=models.IntegerField(blank=True, choices=[(1, 'devis en cours'), (2, 'devis annul\xe9'), (3, 'facture')], null=True),
        ),
    ]
