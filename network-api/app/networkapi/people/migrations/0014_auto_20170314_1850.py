# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-14 18:50
from __future__ import unicode_literals

from django.db import migrations, models
import networkapi.people.models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0013_auto_20170314_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='image',
            field=models.ImageField(max_length=2048, upload_to=networkapi.people.models.get_people_image_upload_path),
        ),
    ]