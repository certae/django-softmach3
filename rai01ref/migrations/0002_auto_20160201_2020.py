# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rai01ref', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artefact',
            name='smVersion',
            field=models.CharField(default='0', max_length=50, null=True, blank=True, editable=False),
        ),
        migrations.AddField(
            model_name='artefactcapacity',
            name='smVersion',
            field=models.CharField(default='0', max_length=50, null=True, blank=True, editable=False),
        ),
        migrations.AddField(
            model_name='artefactcomposition',
            name='smVersion',
            field=models.CharField(default='0', max_length=50, null=True, blank=True, editable=False),
        ),
        migrations.AddField(
            model_name='artefactrequirement',
            name='smVersion',
            field=models.CharField(default='0', max_length=50, null=True, blank=True, editable=False),
        ),
        migrations.AddField(
            model_name='artefactsource',
            name='smVersion',
            field=models.CharField(default='0', max_length=50, null=True, blank=True, editable=False),
        ),
        migrations.AddField(
            model_name='capacity',
            name='smVersion',
            field=models.CharField(default='0', max_length=50, null=True, blank=True, editable=False),
        ),
        migrations.AddField(
            model_name='docattribute',
            name='smVersion',
            field=models.CharField(default='0', max_length=50, null=True, blank=True, editable=False),
        ),
        migrations.AddField(
            model_name='doctype',
            name='smVersion',
            field=models.CharField(default='0', max_length=50, null=True, blank=True, editable=False),
        ),
        migrations.AddField(
            model_name='domain',
            name='smVersion',
            field=models.CharField(default='0', max_length=50, null=True, blank=True, editable=False),
        ),
        migrations.AddField(
            model_name='projectartefact',
            name='smVersion',
            field=models.CharField(default='0', max_length=50, null=True, blank=True, editable=False),
        ),
        migrations.AddField(
            model_name='projectcapacity',
            name='smVersion',
            field=models.CharField(default='0', max_length=50, null=True, blank=True, editable=False),
        ),
        migrations.AddField(
            model_name='projectrequirement',
            name='smVersion',
            field=models.CharField(default='0', max_length=50, null=True, blank=True, editable=False),
        ),
        migrations.AddField(
            model_name='projet',
            name='smVersion',
            field=models.CharField(default='0', max_length=50, null=True, blank=True, editable=False),
        ),
        migrations.AddField(
            model_name='requirement',
            name='smVersion',
            field=models.CharField(default='0', max_length=50, null=True, blank=True, editable=False),
        ),
        migrations.AddField(
            model_name='source',
            name='smVersion',
            field=models.CharField(default='0', max_length=50, null=True, blank=True, editable=False),
        ),
    ]
