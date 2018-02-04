# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-04 10:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Call_number', models.CharField(blank=True, max_length=20)),
                ('collection', models.CharField(blank=True, max_length=60, null=True)),
                ('author', models.CharField(blank=True, max_length=60, null=True)),
                ('arranger', models.CharField(blank=True, max_length=120, null=True)),
                ('editor', models.CharField(blank=True, max_length=120, null=True)),
                ('title', models.CharField(blank=True, max_length=120)),
                ('Uniform_Title', models.CharField(blank=True, max_length=120, null=True)),
                ('publisher', models.CharField(blank=True, max_length=120, null=True)),
                ('place_of_publication', models.CharField(blank=True, max_length=120, null=True)),
                ('date_of_publication', models.CharField(blank=True, max_length=120, null=True)),
                ('Plate_Number', models.CharField(blank=True, max_length=120, null=True)),
                ('ISSN', models.CharField(blank=True, max_length=120, null=True)),
                ('Subject', models.CharField(blank=True, max_length=120, null=True)),
                ('collation', models.CharField(blank=True, max_length=120, null=True)),
                ('holdings', models.CharField(blank=True, max_length=120, null=True)),
                ('medium', models.CharField(blank=True, max_length=120, null=True)),
                ('key_signature', models.CharField(blank=True, max_length=20, null=True)),
                ('duration', models.CharField(blank=True, max_length=20, null=True)),
                ('condition', models.CharField(blank=True, max_length=20, null=True)),
                ('cost', models.CharField(blank=True, max_length=20, null=True)),
                ('acquisition_date', models.CharField(blank=True, max_length=20, null=True)),
                ('notes', models.TextField(blank=True, help_text='Enter a brief note', max_length=1000, null=True)),
            ],
        ),
    ]