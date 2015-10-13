# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0002_auto_20151011_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_num',
            field=models.CharField(max_length=11),
        ),
    ]
