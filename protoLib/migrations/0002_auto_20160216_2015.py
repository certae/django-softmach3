# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('protoLib', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contextvar',
            options={},
        ),
        migrations.AlterField(
            model_name='contextvar',
            name='modelCType',
            field=models.ForeignKey(to='contenttypes.ContentType'),
        ),
        migrations.AlterUniqueTogether(
            name='contextvar',
            unique_together=set([('modelCType',)]),
        ),
    ]
