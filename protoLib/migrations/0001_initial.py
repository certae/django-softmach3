# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid
import jsonfield2.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomDefinition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('smRegStatus', models.CharField(editable=False, blank=True, null=True, max_length=50)),
                ('smWflowStatus', models.CharField(editable=False, blank=True, null=True, max_length=50)),
                ('smCreatedOn', models.DateTimeField(auto_now_add=True, null=True)),
                ('smModifiedOn', models.DateTimeField(auto_now=True, null=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('code', models.CharField(max_length=200)),
                ('description', models.TextField(verbose_name='Descriptions', blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('overWrite', models.BooleanField(default=False)),
                ('metaDefinition', jsonfield2.fields.JSONField(default={})),
                ('smCreatedBy', models.ForeignKey(null=True, editable=False, to=settings.AUTH_USER_MODEL, blank=True, related_name='+')),
                ('smModifiedBy', models.ForeignKey(null=True, editable=False, to=settings.AUTH_USER_MODEL, blank=True, related_name='+')),
            ],
        ),
        migrations.CreateModel(
            name='ProtoDefinition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('code', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField(verbose_name='Description', blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('overWrite', models.BooleanField(default=False)),
                ('metaDefinition', jsonfield2.fields.JSONField(default={})),
            ],
        ),
        migrations.CreateModel(
            name='TeamHierarchy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('code', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField(verbose_name='Descriptions', blank=True, null=True)),
                ('site', models.IntegerField(blank=True, null=True)),
                ('parentNode', models.ForeignKey(null=True, to='protoLib.TeamHierarchy', blank=True, related_name='downHierachy')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('language', models.CharField(blank=True, null=True, max_length=500)),
                ('userTree', models.CharField(blank=True, null=True, max_length=500)),
                ('userConfig', jsonfield2.fields.JSONField(default={})),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
                ('userTeam', models.ForeignKey(null=True, to='protoLib.TeamHierarchy', blank=True, related_name='userTeam')),
            ],
        ),
        migrations.AddField(
            model_name='customdefinition',
            name='smOwningTeam',
            field=models.ForeignKey(null=True, editable=False, to='protoLib.TeamHierarchy', blank=True, related_name='+'),
        ),
        migrations.AddField(
            model_name='customdefinition',
            name='smOwningUser',
            field=models.ForeignKey(null=True, editable=False, to=settings.AUTH_USER_MODEL, blank=True, related_name='+'),
        ),
        migrations.AlterUniqueTogether(
            name='customdefinition',
            unique_together=set([('smOwningTeam', 'code')]),
        ),
    ]
