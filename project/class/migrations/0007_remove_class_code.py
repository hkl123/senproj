# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-05-01 13:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('class', '0006_item_redemptionpage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='code',
        ),
    ]