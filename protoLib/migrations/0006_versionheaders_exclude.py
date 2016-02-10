# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('protoLib', '0005_auto_20160204_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='versionheaders',
            name='exclude',
            field=models.BooleanField(default=False),
        ),
    ]
