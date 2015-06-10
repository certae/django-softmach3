# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import uuid
import jsonfield2.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomDefinition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('smRegStatus', models.CharField(editable=False, blank=True, null=True, max_length=50)),
                ('smWflowStatus', models.CharField(editable=False, blank=True, null=True, max_length=50)),
                ('smCreatedOn', models.DateTimeField(auto_now_add=True, null=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('code', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descriptions')),
                ('active', models.BooleanField(default=True)),
                ('overWrite', models.BooleanField(default=False)),
                ('metaDefinition', jsonfield2.fields.JSONField(default={})),
                ('smCreatedBy', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, editable=False, related_name='+', blank=True)),
                ('smModifiedBy', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, editable=False, related_name='+', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DiscreteValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('code', models.CharField(max_length=200)),
                ('value', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('title', models.ForeignKey(to='protoLib.DiscreteValue', null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Logger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now=True)),
                ('logType', models.CharField(default='INF', max_length=10)),
                ('logObject', models.CharField(blank=True, null=True, max_length=250)),
                ('logNotes', models.CharField(blank=True, null=True, max_length=250)),
                ('logInfo', models.TextField(blank=True, null=True)),
                ('logKey', models.CharField(default='', max_length=5, choices=[('INF', 'INFO'), ('WAR', 'WARNING'), ('ERR', 'ERROR'), ('INS', 'INSERT'), ('UPD', 'UPDATE'), ('DEL', 'DELETE')])),
                ('smCreatedBy', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, editable=False, related_name='+', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ParametersBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('smRegStatus', models.CharField(editable=False, blank=True, null=True, max_length=50)),
                ('smWflowStatus', models.CharField(editable=False, blank=True, null=True, max_length=50)),
                ('smCreatedOn', models.DateTimeField(auto_now_add=True, null=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('metaDefinition', jsonfield2.fields.JSONField(default={})),
                ('parameterKey', models.CharField(max_length=250)),
                ('parameterTag', models.CharField(max_length=250)),
                ('parameterValue', models.CharField(max_length=250)),
                ('smCreatedBy', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, editable=False, related_name='+', blank=True)),
                ('smModifiedBy', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, editable=False, related_name='+', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProtoDefinition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('code', models.CharField(unique=True, max_length=200)),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('active', models.BooleanField(default=True)),
                ('overWrite', models.BooleanField(default=False)),
                ('metaDefinition', jsonfield2.fields.JSONField(default={})),
            ],
        ),
        migrations.CreateModel(
            name='PtFunction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('code', models.CharField(unique=True, max_length=200)),
                ('modelName', models.CharField(max_length=200)),
                ('arguments', models.CharField(max_length=400)),
                ('functionBody', models.TextField(blank=True, null=True)),
                ('tag', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descriptions')),
            ],
        ),
        migrations.CreateModel(
            name='TeamHierarchy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('code', models.CharField(unique=True, max_length=200)),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descriptions')),
                ('site', models.IntegerField(blank=True, null=True)),
                ('parentNode', models.ForeignKey(to='protoLib.TeamHierarchy', null=True, related_name='downHierachy', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('smRegStatus', models.CharField(editable=False, blank=True, null=True, max_length=50)),
                ('smWflowStatus', models.CharField(editable=False, blank=True, null=True, max_length=50)),
                ('smCreatedOn', models.DateTimeField(auto_now_add=True, null=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('metaDefinition', jsonfield2.fields.JSONField(default={})),
                ('docfile', models.FileField(upload_to='media/%Y/%m/%d')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('smCreatedBy', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, editable=False, related_name='+', blank=True)),
                ('smModifiedBy', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, editable=False, related_name='+', blank=True)),
                ('smOwningTeam', models.ForeignKey(to='protoLib.TeamHierarchy', null=True, editable=False, related_name='+', blank=True)),
                ('smOwningUser', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, editable=False, related_name='+', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('language', models.CharField(blank=True, null=True, max_length=500)),
                ('userTree', models.CharField(blank=True, null=True, max_length=500)),
                ('userConfig', jsonfield2.fields.JSONField(default={})),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
                ('userTeam', models.ForeignKey(to='protoLib.TeamHierarchy', null=True, related_name='userTeam', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='WflowAdminResume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('smRegStatus', models.CharField(editable=False, blank=True, null=True, max_length=50)),
                ('smWflowStatus', models.CharField(editable=False, blank=True, null=True, max_length=50)),
                ('smCreatedOn', models.DateTimeField(auto_now_add=True, null=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('metaDefinition', jsonfield2.fields.JSONField(default={})),
                ('viewEntity', models.CharField(max_length=250)),
                ('activityCount', models.IntegerField()),
                ('smCreatedBy', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, editable=False, related_name='+', blank=True)),
                ('smModifiedBy', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, editable=False, related_name='+', blank=True)),
                ('smOwningTeam', models.ForeignKey(to='protoLib.TeamHierarchy', null=True, editable=False, related_name='+', blank=True)),
                ('smOwningUser', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, editable=False, related_name='+', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WflowUserReponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('smRegStatus', models.CharField(editable=False, blank=True, null=True, max_length=50)),
                ('smWflowStatus', models.CharField(editable=False, blank=True, null=True, max_length=50)),
                ('smCreatedOn', models.DateTimeField(auto_now_add=True, null=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('metaDefinition', jsonfield2.fields.JSONField(default={})),
                ('viewEntity', models.CharField(max_length=250)),
                ('wfAction', models.CharField(max_length=250)),
                ('strKey', models.CharField(max_length=250)),
                ('adminMsg', models.CharField(max_length=250)),
                ('smCreatedBy', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, editable=False, related_name='+', blank=True)),
                ('smModifiedBy', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, editable=False, related_name='+', blank=True)),
                ('smOwningTeam', models.ForeignKey(to='protoLib.TeamHierarchy', null=True, editable=False, related_name='+', blank=True)),
                ('smOwningUser', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, editable=False, related_name='+', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='parametersbase',
            name='smOwningTeam',
            field=models.ForeignKey(to='protoLib.TeamHierarchy', null=True, editable=False, related_name='+', blank=True),
        ),
        migrations.AddField(
            model_name='parametersbase',
            name='smOwningUser',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, editable=False, related_name='+', blank=True),
        ),
        migrations.AddField(
            model_name='logger',
            name='smOwningTeam',
            field=models.ForeignKey(to='protoLib.TeamHierarchy', null=True, editable=False, related_name='+', blank=True),
        ),
        migrations.AddField(
            model_name='customdefinition',
            name='smOwningTeam',
            field=models.ForeignKey(to='protoLib.TeamHierarchy', null=True, editable=False, related_name='+', blank=True),
        ),
        migrations.AddField(
            model_name='customdefinition',
            name='smOwningUser',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, editable=False, related_name='+', blank=True),
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
