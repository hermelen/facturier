# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-05 13:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20181005_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotation',
            name='status',
            field=models.CharField(blank=True, choices=[('1', 'devis en cours'), ('2', 'devis annul\xe9'), ('3', 'facture')], max_length=1, null=True),
        ),
    ]
