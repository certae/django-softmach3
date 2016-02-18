# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('protoLib', '0004_auto_20160217_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contextuser',
            name='propValue',
            field=models.CharField(blank=True, null=True, max_length=200),
        ),
    ]
