# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-29 10:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20171229_0918'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio_list',
            name='posted_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='portfolio_list',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
