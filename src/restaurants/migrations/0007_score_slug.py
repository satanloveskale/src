# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-04 14:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0006_score_score_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]