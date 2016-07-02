# -*- coding: utf-8 -*-
# Generated by Django 1.9.3.dev20160206142456 on 2016-02-13 22:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('degrees', '0001_initial'),
        ('students', '0008_auto_20160112_0403'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='degree',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='degrees.Degree'),
        ),
    ]
