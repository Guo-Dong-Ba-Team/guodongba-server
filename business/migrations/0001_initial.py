# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('user_name', models.CharField(max_length=100)),
                ('login_type', models.BooleanField(verbose_name='用手机登陆还是用邮箱登陆（0为手机）')),
                ('phone_num', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
