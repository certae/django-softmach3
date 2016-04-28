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
            name='capacity',
            field=models.ForeignKey(to='rai01ref.Capacity', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='artefact',
            name='requirement',
            field=models.ForeignKey(to='rai01ref.Requirement', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='artefactcapacity',
            name='isMain',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='artefactrequirement',
            name='isMain',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='artefact',
            name='copyFrom',
            field=models.ForeignKey(to='rai01ref.Artefact', blank=True, related_name='copy_set', null=True),
        ),
        migrations.AlterField(
            model_name='artefact',
            name='refArtefact',
            field=models.ForeignKey(to='rai01ref.Artefact', blank=True, related_name='ref_set', null=True),
        ),
        migrations.AlterField(
            model_name='capacity',
            name='copyFrom',
            field=models.ForeignKey(to='rai01ref.Capacity', blank=True, related_name='copy_set', null=True),
        ),
        migrations.AlterField(
            model_name='capacity',
            name='refCapacity',
            field=models.ForeignKey(to='rai01ref.Capacity', blank=True, related_name='ref_set', null=True),
        ),
        migrations.AlterField(
            model_name='requirement',
            name='copyFrom',
            field=models.ForeignKey(to='rai01ref.Requirement', blank=True, related_name='copy_set', null=True),
        ),
        migrations.AlterField(
            model_name='requirement',
            name='refRequirement',
            field=models.ForeignKey(to='rai01ref.Requirement', blank=True, related_name='ref_set', null=True),
        ),
    ]
