# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-07 06:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20171007_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='./covers/%Y/%m'),
        ),
    ]
