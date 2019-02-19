# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2019-02-19 15:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RawPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.SmallIntegerField(choices=[(1, 'i.sf-express.com')], default=1)),
                ('identity', models.CharField(help_text='\u552f\u4e00\u6807\u8bc6', max_length=100)),
                ('address', models.CharField(help_text='\u5730\u5740', max_length=200)),
                ('raw_data', models.TextField(help_text='\u539f\u59cb\u4fe1\u606f')),
                ('status', models.SmallIntegerField(choices=[(0, '\u7981\u7528'), (1, '\u6b63\u5e38')], default=1)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='rawpoint',
            unique_together=set([('source', 'identity')]),
        ),
    ]
