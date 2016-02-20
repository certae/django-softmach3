# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rai01ref', '0004_auto_20160220_1638'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='domain',
            unique_together=set([('code', 'smVersion')]),
        ),
    ]
