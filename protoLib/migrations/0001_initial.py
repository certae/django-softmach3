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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('smRegStatus', models.CharField(blank=True, editable=False, max_length=50, null=True)),
                ('smWflowStatus', models.CharField(blank=True, editable=False, max_length=50, null=True)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(auto_now=True, null=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('smInfo', jsonfield2.fields.JSONField(default={})),
                ('code', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, verbose_name='Descriptions', null=True)),
                ('metaDefinition', models.TextField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('overWrite', models.BooleanField(default=False)),
                ('smCreatedBy', models.ForeignKey(blank=True, related_name='+', editable=False, null=True, to=settings.AUTH_USER_MODEL)),
                ('smModifiedBy', models.ForeignKey(blank=True, related_name='+', editable=False, null=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DiscreteValue',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('code', models.CharField(max_length=200)),
                ('value', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('title', models.ForeignKey(blank=True, null=True, to='protoLib.DiscreteValue')),
            ],
        ),
        migrations.CreateModel(
            name='Logger',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('smCreatedOn', models.DateTimeField(auto_now=True, null=True)),
                ('logType', models.CharField(max_length=10, default='INF')),
                ('logObject', models.CharField(blank=True, max_length=250, null=True)),
                ('logNotes', models.CharField(blank=True, max_length=250, null=True)),
                ('logInfo', models.TextField(blank=True, null=True)),
                ('logKey', models.CharField(choices=[('INF', 'INFO'), ('WAR', 'WARNING'), ('ERR', 'ERROR'), ('INS', 'INSERT'), ('UPD', 'UPDATE'), ('DEL', 'DELETE')], max_length=5, default='')),
                ('smCreatedBy', models.ForeignKey(blank=True, related_name='+', editable=False, null=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ParametersBase',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('smRegStatus', models.CharField(blank=True, editable=False, max_length=50, null=True)),
                ('smWflowStatus', models.CharField(blank=True, editable=False, max_length=50, null=True)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(auto_now=True, null=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('smInfo', jsonfield2.fields.JSONField(default={})),
                ('parameterKey', models.CharField(max_length=250)),
                ('parameterTag', models.CharField(max_length=250)),
                ('parameterValue', models.CharField(max_length=250)),
                ('smCreatedBy', models.ForeignKey(blank=True, related_name='+', editable=False, null=True, to=settings.AUTH_USER_MODEL)),
                ('smModifiedBy', models.ForeignKey(blank=True, related_name='+', editable=False, null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProtoDefinition',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('code', models.CharField(unique=True, max_length=200)),
                ('description', models.TextField(blank=True, verbose_name='Description', null=True)),
                ('active', models.BooleanField(default=True)),
                ('overWrite', models.BooleanField(default=False)),
                ('metaDefinition', jsonfield2.fields.JSONField(default={})),
            ],
        ),
        migrations.CreateModel(
            name='PtFunction',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('code', models.CharField(unique=True, max_length=200)),
                ('modelName', models.CharField(max_length=200)),
                ('arguments', models.CharField(max_length=400)),
                ('functionBody', models.TextField(blank=True, null=True)),
                ('tag', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, verbose_name='Descriptions', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TeamHierarchy',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('code', models.CharField(unique=True, max_length=200)),
                ('description', models.TextField(blank=True, verbose_name='Descriptions', null=True)),
                ('site', models.IntegerField(blank=True, null=True)),
                ('parentNode', models.ForeignKey(blank=True, related_name='downHierachy', null=True, to='protoLib.TeamHierarchy')),
            ],
        ),
        migrations.CreateModel(
            name='UserFiles',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('smRegStatus', models.CharField(blank=True, editable=False, max_length=50, null=True)),
                ('smWflowStatus', models.CharField(blank=True, editable=False, max_length=50, null=True)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(auto_now=True, null=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('smInfo', jsonfield2.fields.JSONField(default={})),
                ('docfile', models.FileField(upload_to='media/%Y/%m/%d')),
                ('description', models.TextField(blank=True, verbose_name='Description', null=True)),
                ('smCreatedBy', models.ForeignKey(blank=True, related_name='+', editable=False, null=True, to=settings.AUTH_USER_MODEL)),
                ('smModifiedBy', models.ForeignKey(blank=True, related_name='+', editable=False, null=True, to=settings.AUTH_USER_MODEL)),
                ('smOwningTeam', models.ForeignKey(blank=True, related_name='+', editable=False, null=True, to='protoLib.TeamHierarchy')),
                ('smOwningUser', models.ForeignKey(blank=True, related_name='+', editable=False, null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('language', models.CharField(blank=True, max_length=500, null=True)),
                ('userTree', models.CharField(blank=True, max_length=500, null=True)),
                ('userConfig', jsonfield2.fields.JSONField(default={})),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
                ('userTeam', models.ForeignKey(blank=True, related_name='userTeam', null=True, to='protoLib.TeamHierarchy')),
            ],
        ),
        migrations.CreateModel(
            name='WflowAdminResume',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('smRegStatus', models.CharField(blank=True, editable=False, max_length=50, null=True)),
                ('smWflowStatus', models.CharField(blank=True, editable=False, max_length=50, null=True)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(auto_now=True, null=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('smInfo', jsonfield2.fields.JSONField(default={})),
                ('viewEntity', models.CharField(max_length=250)),
                ('activityCount', models.IntegerField()),
                ('smCreatedBy', models.ForeignKey(blank=True, related_name='+', editable=False, null=True, to=settings.AUTH_USER_MODEL)),
                ('smModifiedBy', models.ForeignKey(blank=True, related_name='+', editable=False, null=True, to=settings.AUTH_USER_MODEL)),
                ('smOwningTeam', models.ForeignKey(blank=True, related_name='+', editable=False, null=True, to='protoLib.TeamHierarchy')),
                ('smOwningUser', models.ForeignKey(blank=True, related_name='+', editable=False, null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WflowUserReponse',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('smRegStatus', models.CharField(blank=True, editable=False, max_length=50, null=True)),
                ('smWflowStatus', models.CharField(blank=True, editable=False, max_length=50, null=True)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(auto_now=True, null=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('smInfo', jsonfield2.fields.JSONField(default={})),
                ('viewEntity', models.CharField(max_length=250)),
                ('wfAction', models.CharField(max_length=250)),
                ('strKey', models.CharField(max_length=250)),
                ('adminMsg', models.CharField(max_length=250)),
                ('smCreatedBy', models.ForeignKey(blank=True, related_name='+', editable=False, null=True, to=settings.AUTH_USER_MODEL)),
                ('smModifiedBy', models.ForeignKey(blank=True, related_name='+', editable=False, null=True, to=settings.AUTH_USER_MODEL)),
                ('smOwningTeam', models.ForeignKey(blank=True, related_name='+', editable=False, null=True, to='protoLib.TeamHierarchy')),
                ('smOwningUser', models.ForeignKey(blank=True, related_name='+', editable=False, null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='parametersbase',
            name='smOwningTeam',
            field=models.ForeignKey(blank=True, related_name='+', editable=False, null=True, to='protoLib.TeamHierarchy'),
        ),
        migrations.AddField(
            model_name='parametersbase',
            name='smOwningUser',
            field=models.ForeignKey(blank=True, related_name='+', editable=False, null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='logger',
            name='smOwningTeam',
            field=models.ForeignKey(blank=True, related_name='+', editable=False, null=True, to='protoLib.TeamHierarchy'),
        ),
        migrations.AddField(
            model_name='customdefinition',
            name='smOwningTeam',
            field=models.ForeignKey(blank=True, related_name='+', editable=False, null=True, to='protoLib.TeamHierarchy'),
        ),
        migrations.AddField(
            model_name='customdefinition',
            name='smOwningUser',
            field=models.ForeignKey(blank=True, related_name='+', editable=False, null=True, to=settings.AUTH_USER_MODEL),
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
