# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-30 11:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='extendeduser',
            name='is_manager',
            field=models.BooleanField(default=False),
        ),
    ]