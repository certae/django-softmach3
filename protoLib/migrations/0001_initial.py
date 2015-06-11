# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import uuid
import jsonfield2.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomDefinition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('smRegStatus', models.CharField(max_length=50, blank=True, editable=False, null=True)),
                ('smWflowStatus', models.CharField(max_length=50, blank=True, editable=False, null=True)),
                ('smCreatedOn', models.DateTimeField(auto_now_add=True, null=True)),
                ('smModifiedOn', models.DateTimeField(auto_now=True, null=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('code', models.CharField(max_length=200)),
                ('description', models.TextField(verbose_name='Descriptions', blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('overWrite', models.BooleanField(default=False)),
                ('metaDefinition', jsonfield2.fields.JSONField(default={})),
                ('smCreatedBy', models.ForeignKey(blank=True, null=True, editable=False, to=settings.AUTH_USER_MODEL, related_name='+')),
                ('smModifiedBy', models.ForeignKey(blank=True, null=True, editable=False, to=settings.AUTH_USER_MODEL, related_name='+')),
            ],
        ),
        migrations.CreateModel(
            name='EntityMap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('entityConfig', jsonfield2.fields.JSONField(default={})),
                ('entityBase', models.OneToOneField(to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='ProtoDefinition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField(verbose_name='Descriptions', blank=True, null=True)),
                ('site', models.IntegerField(blank=True, null=True)),
                ('parentNode', models.ForeignKey(blank=True, related_name='downHierachy', null=True, to='protoLib.TeamHierarchy')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language', models.CharField(max_length=500, blank=True, null=True)),
                ('userTree', models.CharField(max_length=500, blank=True, null=True)),
                ('userConfig', jsonfield2.fields.JSONField(default={})),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
                ('userTeam', models.ForeignKey(blank=True, related_name='userTeam', null=True, to='protoLib.TeamHierarchy')),
            ],
        ),
        migrations.AddField(
            model_name='customdefinition',
            name='smOwningTeam',
            field=models.ForeignKey(blank=True, null=True, editable=False, to='protoLib.TeamHierarchy', related_name='+'),
        ),
        migrations.AddField(
            model_name='customdefinition',
            name='smOwningUser',
            field=models.ForeignKey(blank=True, null=True, editable=False, to=settings.AUTH_USER_MODEL, related_name='+'),
        ),
        migrations.AlterUniqueTogether(
            name='customdefinition',
            unique_together=set([('smOwningTeam', 'code')]),
        ),
    ]
