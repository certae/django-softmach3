# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('protoLib', '0003_auto_20160217_2203'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='contextvar',
            unique_together=set([('modelCType', 'propName')]),
        ),
    ]
