# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0004_auto_20151013_1146'),
    ]

    operations = [
        migrations.CreateModel(
            name='GymInfo',
            fields=[
                ('name', models.CharField(serialize=False, primary_key=True, max_length=250)),
                ('type', models.IntegerField()),
                ('address', models.CharField(max_length=300)),
                ('image', models.CharField(max_length=100)),
                ('open_time', models.CharField(max_length=100)),
                ('single_price', models.FloatField()),
                ('vip_price', models.FloatField()),
                ('discount', models.FloatField()),
                ('hardware_info', models.CharField(max_length=1000)),
                ('service_info', models.CharField(max_length=1000)),
                ('owner', models.ForeignKey(to='business.User')),
            ],
            options={
                'db_table': 'gym_info',
            },
        ),
    ]
