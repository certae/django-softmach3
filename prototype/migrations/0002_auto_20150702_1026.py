# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prototype', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='prototype',
            unique_together=set([('entity', 'code', 'smOwningTeam')]),
        ),
    ]
