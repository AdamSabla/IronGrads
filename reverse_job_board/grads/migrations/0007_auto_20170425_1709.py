# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-25 21:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grads', '0006_auto_20170425_1645'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='graduates',
            options={'ordering': ['first_name'], 'verbose_name': ['first_name']},
        ),
    ]
