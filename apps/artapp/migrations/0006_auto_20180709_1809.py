# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-09 10:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artapp', '0005_auto_20180709_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='文章的图片'),
        ),
    ]
