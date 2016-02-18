# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('protoExt', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parameters',
            name='smVersion',
        ),
        migrations.AlterUniqueTogether(
            name='customdefinition',
            unique_together=set([('code', 'smOwningUser')]),
        ),
        migrations.RemoveField(
            model_name='customdefinition',
            name='smVersion',
        ),
    ]
