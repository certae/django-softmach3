# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prototype', '0002_auto_20160414_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='prototable',
            name='smVersion',
            field=models.ForeignKey(to='prototype.ProtoVersionTitle', default=1),
        ),
    ]
