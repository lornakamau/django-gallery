# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-06-26 12:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20200626_1104'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='image',
            new_name='photo',
        ),
    ]
