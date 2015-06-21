# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('protoLib', '0002_auto_20150621_1241'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usercontext',
            old_name='entity',
            new_name='modelCType',
        ),
        migrations.RenameField(
            model_name='usercontext',
            old_name='property',
            new_name='propName',
        ),
        migrations.AlterUniqueTogether(
            name='usercontext',
            unique_together=set([('modelCType', 'propName', 'smOwningUser')]),
        ),
    ]
