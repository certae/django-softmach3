# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prototype', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagram',
            name='smVersion',
            field=models.CharField(blank=True, null=True, default='0', editable=False, max_length=50),
        ),
        migrations.AddField(
            model_name='diagramentity',
            name='smVersion',
            field=models.CharField(blank=True, null=True, default='0', editable=False, max_length=50),
        ),
        migrations.AddField(
            model_name='entity',
            name='smVersion',
            field=models.CharField(blank=True, null=True, default='0', editable=False, max_length=50),
        ),
        migrations.AddField(
            model_name='model',
            name='smVersion',
            field=models.CharField(blank=True, null=True, default='0', editable=False, max_length=50),
        ),
        migrations.AddField(
            model_name='project',
            name='smVersion',
            field=models.CharField(blank=True, null=True, default='0', editable=False, max_length=50),
        ),
        migrations.AddField(
            model_name='property',
            name='smVersion',
            field=models.CharField(blank=True, null=True, default='0', editable=False, max_length=50),
        ),
        migrations.AddField(
            model_name='propertyequivalence',
            name='smVersion',
            field=models.CharField(blank=True, null=True, default='0', editable=False, max_length=50),
        ),
        migrations.AddField(
            model_name='prototable',
            name='smVersion',
            field=models.CharField(blank=True, null=True, default='0', editable=False, max_length=50),
        ),
        migrations.AddField(
            model_name='prototype',
            name='smVersion',
            field=models.CharField(blank=True, null=True, default='0', editable=False, max_length=50),
        ),
    ]
