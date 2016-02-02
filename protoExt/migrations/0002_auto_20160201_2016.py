# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('protoExt', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customdefinition',
            name='smVersion',
            field=models.CharField(editable=False, max_length=50, blank=True, default='0', null=True),
        ),
        migrations.AddField(
            model_name='parameters',
            name='smVersion',
            field=models.CharField(editable=False, max_length=50, blank=True, default='0', null=True),
        ),
    ]
