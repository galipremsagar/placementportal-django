# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-06 04:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20160605_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='auth1',
            name='password',
            field=models.CharField(default='', max_length=250),
        ),
    ]