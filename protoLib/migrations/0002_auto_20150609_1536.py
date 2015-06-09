# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield2.fields


class Migration(migrations.Migration):

    dependencies = [
        ('protoLib', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parametersbase',
            old_name='smInfo',
            new_name='metaDefinition',
        ),
        migrations.RenameField(
            model_name='userfiles',
            old_name='smInfo',
            new_name='metaDefinition',
        ),
        migrations.RemoveField(
            model_name='customdefinition',
            name='smInfo',
        ),
        migrations.RemoveField(
            model_name='wflowadminresume',
            name='smInfo',
        ),
        migrations.RemoveField(
            model_name='wflowuserreponse',
            name='smInfo',
        ),
        migrations.AddField(
            model_name='wflowadminresume',
            name='metaDefinition',
            field=jsonfield2.fields.JSONField(default={}),
        ),
        migrations.AddField(
            model_name='wflowuserreponse',
            name='metaDefinition',
            field=jsonfield2.fields.JSONField(default={}),
        ),
        migrations.AlterField(
            model_name='customdefinition',
            name='metaDefinition',
            field=jsonfield2.fields.JSONField(default={}),
        ),
    ]
