# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prototype', '0003_auto_20160218_0945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='protoversionheader',
            name='modelCType',
        ),
        migrations.RemoveField(
            model_name='protoversionheader',
            name='smCreatedBy',
        ),
        migrations.RemoveField(
            model_name='protoversionheader',
            name='smModifiedBy',
        ),
        migrations.RemoveField(
            model_name='protoversionheader',
            name='smOwningTeam',
        ),
        migrations.RemoveField(
            model_name='protoversionheader',
            name='smOwningUser',
        ),
        migrations.DeleteModel(
            name='ProtoVersionHeader',
        ),
    ]
