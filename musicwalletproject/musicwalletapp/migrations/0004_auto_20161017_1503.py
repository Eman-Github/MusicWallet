# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-17 15:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicwalletapp', '0003_user_favourite_musics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='favourite_musics',
            field=models.ManyToManyField(blank=True, to='musicwalletapp.Music'),
        ),
    ]
