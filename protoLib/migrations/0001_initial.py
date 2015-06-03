# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield0.fields
import uuid
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomDefinition',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('smRegStatus', models.CharField(max_length=50, editable=False, blank=True, null=True)),
                ('smWflowStatus', models.CharField(max_length=50, editable=False, blank=True, null=True)),
                ('smCreatedOn', models.DateTimeField(auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(auto_now=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('code', models.CharField(max_length=200)),
                ('description', models.TextField(verbose_name='Descriptions', blank=True, null=True)),
                ('metaDefinition', models.TextField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('overWrite', models.BooleanField(default=False)),
                ('smCreatedBy', models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL, blank=True, related_name='+', null=True)),
                ('smModifiedBy', models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL, blank=True, related_name='+', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DiscreteValue',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('code', models.CharField(max_length=200)),
                ('value', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('title', models.ForeignKey(blank=True, to='protoLib.DiscreteValue', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EntityMap',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('appName', models.CharField(max_length=200)),
                ('modelName', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='FieldMap',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('fieldName', models.CharField(max_length=200)),
                ('entity', models.ForeignKey(to='protoLib.EntityMap')),
            ],
        ),
        migrations.CreateModel(
            name='JsonModel',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('code', models.CharField(max_length=20)),
                ('info', jsonfield0.fields.JSONField(default={})),
            ],
        ),
        migrations.CreateModel(
            name='Logger',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('smCreatedOn', models.DateTimeField(auto_now=True, null=True)),
                ('logType', models.CharField(max_length=10, default='INF')),
                ('logObject', models.CharField(max_length=250, blank=True, null=True)),
                ('logNotes', models.CharField(max_length=250, blank=True, null=True)),
                ('logInfo', models.TextField(blank=True, null=True)),
                ('logKey', models.CharField(max_length=5, default='', choices=[('INF', 'INFO'), ('WAR', 'WARNING'), ('ERR', 'ERROR'), ('INS', 'INSERT'), ('UPD', 'UPDATE'), ('DEL', 'DELETE')])),
                ('smCreatedBy', models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL, blank=True, related_name='+', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ParametersBase',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('smRegStatus', models.CharField(max_length=50, editable=False, blank=True, null=True)),
                ('smWflowStatus', models.CharField(max_length=50, editable=False, blank=True, null=True)),
                ('smCreatedOn', models.DateTimeField(auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(auto_now=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('parameterKey', models.CharField(max_length=250)),
                ('parameterTag', models.CharField(max_length=250)),
                ('parameterValue', models.CharField(max_length=250)),
                ('smCreatedBy', models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL, blank=True, related_name='+', null=True)),
                ('smModifiedBy', models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL, blank=True, related_name='+', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProtoDefinition',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('code', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField(verbose_name='Descriptions', blank=True, null=True)),
                ('metaDefinition', models.TextField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('overWrite', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PtFunction',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('code', models.CharField(max_length=200, unique=True)),
                ('modelName', models.CharField(max_length=200)),
                ('arguments', models.CharField(max_length=400)),
                ('functionBody', models.TextField(blank=True, null=True)),
                ('tag', models.CharField(max_length=200)),
                ('description', models.TextField(verbose_name='Descriptions', blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TeamHierarchy',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('code', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField(verbose_name='Descriptions', blank=True, null=True)),
                ('site', models.IntegerField(blank=True, null=True)),
                ('parentNode', models.ForeignKey(to='protoLib.TeamHierarchy', blank=True, related_name='downHierachy', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserFiles',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('docfile', models.FileField(upload_to='media/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('language', models.CharField(max_length=500, blank=True, null=True)),
                ('userTree', models.CharField(max_length=500, blank=True, null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
                ('userTeam', models.ForeignKey(to='protoLib.TeamHierarchy', blank=True, related_name='userTeam', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WflowAdminResume',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('smRegStatus', models.CharField(max_length=50, editable=False, blank=True, null=True)),
                ('smWflowStatus', models.CharField(max_length=50, editable=False, blank=True, null=True)),
                ('smCreatedOn', models.DateTimeField(auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(auto_now=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('viewEntity', models.CharField(max_length=250)),
                ('activityCount', models.IntegerField()),
                ('smCreatedBy', models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL, blank=True, related_name='+', null=True)),
                ('smModifiedBy', models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL, blank=True, related_name='+', null=True)),
                ('smOwningTeam', models.ForeignKey(editable=False, to='protoLib.TeamHierarchy', blank=True, related_name='+', null=True)),
                ('smOwningUser', models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL, blank=True, related_name='+', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WflowUserReponse',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('smRegStatus', models.CharField(max_length=50, editable=False, blank=True, null=True)),
                ('smWflowStatus', models.CharField(max_length=50, editable=False, blank=True, null=True)),
                ('smCreatedOn', models.DateTimeField(auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(auto_now=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('viewEntity', models.CharField(max_length=250)),
                ('wfAction', models.CharField(max_length=250)),
                ('strKey', models.CharField(max_length=250)),
                ('adminMsg', models.CharField(max_length=250)),
                ('smCreatedBy', models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL, blank=True, related_name='+', null=True)),
                ('smModifiedBy', models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL, blank=True, related_name='+', null=True)),
                ('smOwningTeam', models.ForeignKey(editable=False, to='protoLib.TeamHierarchy', blank=True, related_name='+', null=True)),
                ('smOwningUser', models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL, blank=True, related_name='+', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='parametersbase',
            name='smOwningTeam',
            field=models.ForeignKey(editable=False, to='protoLib.TeamHierarchy', blank=True, related_name='+', null=True),
        ),
        migrations.AddField(
            model_name='parametersbase',
            name='smOwningUser',
            field=models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL, blank=True, related_name='+', null=True),
        ),
        migrations.AddField(
            model_name='logger',
            name='smOwningTeam',
            field=models.ForeignKey(editable=False, to='protoLib.TeamHierarchy', blank=True, related_name='+', null=True),
        ),
        migrations.AlterUniqueTogether(
            name='entitymap',
            unique_together=set([('appName', 'modelName')]),
        ),
        migrations.AddField(
            model_name='customdefinition',
            name='smOwningTeam',
            field=models.ForeignKey(editable=False, to='protoLib.TeamHierarchy', blank=True, related_name='+', null=True),
        ),
        migrations.AddField(
            model_name='customdefinition',
            name='smOwningUser',
            field=models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL, blank=True, related_name='+', null=True),
        ),
        migrations.AlterUniqueTogether(
            name='fieldmap',
            unique_together=set([('entity', 'fieldName')]),
        ),
        migrations.AlterUniqueTogether(
            name='discretevalue',
            unique_together=set([('title', 'value')]),
        ),
        migrations.AlterUniqueTogether(
            name='customdefinition',
            unique_together=set([('smOwningTeam', 'code')]),
        ),
    ]
