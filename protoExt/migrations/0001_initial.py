# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import jsonfield2.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('protoLib', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomDefinition',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('smNaturalCode', models.CharField(null=True, editable=False, max_length=50, blank=True)),
                ('smRegStatus', models.CharField(null=True, editable=False, max_length=50, blank=True)),
                ('smWflowStatus', models.CharField(null=True, editable=False, max_length=50, blank=True)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('code', models.CharField(max_length=200)),
                ('description', models.TextField(null=True, verbose_name='Descriptions', blank=True)),
                ('active', models.BooleanField(default=True)),
                ('overWrite', models.BooleanField(default=False)),
                ('metaDefinition', jsonfield2.fields.JSONField(default={})),
                ('smCreatedBy', models.ForeignKey(null=True, editable=False, blank=True, to=settings.AUTH_USER_MODEL, related_name='+')),
                ('smModifiedBy', models.ForeignKey(null=True, editable=False, blank=True, to=settings.AUTH_USER_MODEL, related_name='+')),
                ('smOwningTeam', models.ForeignKey(null=True, editable=False, blank=True, to='protoLib.TeamHierarchy', related_name='+')),
                ('smOwningUser', models.ForeignKey(null=True, editable=False, blank=True, to=settings.AUTH_USER_MODEL, related_name='+')),
            ],
        ),
        migrations.CreateModel(
            name='Parameters',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('smNaturalCode', models.CharField(null=True, editable=False, max_length=50, blank=True)),
                ('smRegStatus', models.CharField(null=True, editable=False, max_length=50, blank=True)),
                ('smWflowStatus', models.CharField(null=True, editable=False, max_length=50, blank=True)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('smInfo', jsonfield2.fields.JSONField(default={})),
                ('parameterKey', models.CharField(max_length=250)),
                ('parameterTag', models.CharField(null=True, max_length=250, blank=True)),
                ('parameterValue', models.CharField(max_length=250)),
                ('smCreatedBy', models.ForeignKey(null=True, editable=False, blank=True, to=settings.AUTH_USER_MODEL, related_name='+')),
                ('smModifiedBy', models.ForeignKey(null=True, editable=False, blank=True, to=settings.AUTH_USER_MODEL, related_name='+')),
                ('smOwningTeam', models.ForeignKey(null=True, editable=False, blank=True, to='protoLib.TeamHierarchy', related_name='+')),
                ('smOwningUser', models.ForeignKey(null=True, editable=False, blank=True, to=settings.AUTH_USER_MODEL, related_name='+')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ViewDefinition',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('code', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField(null=True, verbose_name='Description', blank=True)),
                ('active', models.BooleanField(default=True)),
                ('overWrite', models.BooleanField(default=False)),
                ('metaDefinition', jsonfield2.fields.JSONField(default={})),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='customdefinition',
            unique_together=set([('code', 'smOwningUser')]),
        ),
    ]
