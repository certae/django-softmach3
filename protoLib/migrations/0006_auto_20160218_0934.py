# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('protoLib', '0005_auto_20160217_2219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='versionheaders',
            name='modelCType',
        ),
        migrations.RemoveField(
            model_name='versiontitle',
            name='smCreatedBy',
        ),
        migrations.RemoveField(
            model_name='versiontitle',
            name='smModifiedBy',
        ),
        migrations.RemoveField(
            model_name='versiontitle',
            name='versionBase',
        ),
        migrations.AlterUniqueTogether(
            name='versionuser',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='versionuser',
            name='user',
        ),
        migrations.RemoveField(
            model_name='versionuser',
            name='version',
        ),
        migrations.RemoveField(
            model_name='contextentity',
            name='smVersion',
        ),
        migrations.RemoveField(
            model_name='contextuser',
            name='smVersion',
        ),
        migrations.RemoveField(
            model_name='contextvar',
            name='smVersion',
        ),
        migrations.DeleteModel(
            name='VersionHeaders',
        ),
        migrations.DeleteModel(
            name='VersionTitle',
        ),
        migrations.DeleteModel(
            name='VersionUser',
        ),
    ]
