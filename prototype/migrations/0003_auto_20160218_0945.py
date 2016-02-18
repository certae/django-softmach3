# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prototype', '0002_auto_20160218_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagram',
            name='smVersion',
            field=models.ForeignKey(to='prototype.ProtoVersionTitle', default=1),
        ),
        migrations.AlterField(
            model_name='diagramentity',
            name='smVersion',
            field=models.ForeignKey(to='prototype.ProtoVersionTitle', default=1),
        ),
        migrations.AlterField(
            model_name='entity',
            name='smVersion',
            field=models.ForeignKey(to='prototype.ProtoVersionTitle', default=1),
        ),
        migrations.AlterField(
            model_name='model',
            name='smVersion',
            field=models.ForeignKey(to='prototype.ProtoVersionTitle', default=1),
        ),
        migrations.AlterField(
            model_name='project',
            name='smVersion',
            field=models.ForeignKey(to='prototype.ProtoVersionTitle', default=1),
        ),
        migrations.AlterField(
            model_name='property',
            name='smVersion',
            field=models.ForeignKey(to='prototype.ProtoVersionTitle', default=1),
        ),
        migrations.AlterField(
            model_name='propertyequivalence',
            name='smVersion',
            field=models.ForeignKey(to='prototype.ProtoVersionTitle', default=1),
        ),
        migrations.AlterField(
            model_name='prototable',
            name='smVersion',
            field=models.ForeignKey(to='prototype.ProtoVersionTitle', default=1),
        ),
        migrations.AlterField(
            model_name='prototype',
            name='smVersion',
            field=models.ForeignKey(to='prototype.ProtoVersionTitle', default=1),
        ),
    ]
