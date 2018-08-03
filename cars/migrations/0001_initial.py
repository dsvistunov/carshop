# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-05 15:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_mark', models.CharField(max_length=100)),
                ('car_model', models.CharField(max_length=100)),
                ('car_year', models.CharField(max_length=4)),
                ('slug', models.SlugField(unique=True)),
                ('car_description', models.TextField(max_length=10000)),
                ('car_public', models.DateTimeField(auto_now_add=True)),
                ('car_image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Image')),
            ],
            options={
                'db_table': 'cars',
            },
        ),
    ]
