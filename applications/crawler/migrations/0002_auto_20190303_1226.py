# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2019-03-03 12:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rawpoint',
            name='source',
            field=models.SmallIntegerField(choices=[(1, 'i.sf-express.com'), (2, 'submit')], default=1),
        ),
    ]
