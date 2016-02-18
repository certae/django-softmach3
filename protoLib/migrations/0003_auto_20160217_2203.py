# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('protoLib', '0002_auto_20160216_2015'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contextvar',
            old_name='propDescription',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='contextvar',
            name='isDefault',
        ),
        migrations.RemoveField(
            model_name='contextvar',
            name='isFilter',
        ),
        migrations.AlterField(
            model_name='contextvar',
            name='propName',
            field=models.CharField(max_length=500, default='id'),
        ),
    ]
