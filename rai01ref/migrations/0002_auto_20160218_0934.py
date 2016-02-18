# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rai01ref', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artefact',
            name='smVersion',
        ),
        migrations.RemoveField(
            model_name='artefactcapacity',
            name='smVersion',
        ),
        migrations.RemoveField(
            model_name='artefactcomposition',
            name='smVersion',
        ),
        migrations.RemoveField(
            model_name='artefactrequirement',
            name='smVersion',
        ),
        migrations.RemoveField(
            model_name='artefactsource',
            name='smVersion',
        ),
        migrations.RemoveField(
            model_name='capacity',
            name='smVersion',
        ),
        migrations.RemoveField(
            model_name='docattribute',
            name='smVersion',
        ),
        migrations.RemoveField(
            model_name='doctype',
            name='smVersion',
        ),
        migrations.RemoveField(
            model_name='domain',
            name='smVersion',
        ),
        migrations.RemoveField(
            model_name='projectartefact',
            name='smVersion',
        ),
        migrations.RemoveField(
            model_name='projectcapacity',
            name='smVersion',
        ),
        migrations.RemoveField(
            model_name='projectrequirement',
            name='smVersion',
        ),
        migrations.RemoveField(
            model_name='projet',
            name='smVersion',
        ),
        migrations.RemoveField(
            model_name='requirement',
            name='smVersion',
        ),
        migrations.RemoveField(
            model_name='source',
            name='smVersion',
        ),
    ]
