# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-16 17:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration_app', '0004_remove_profile_birth_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to='profile_image'),
        ),
    ]