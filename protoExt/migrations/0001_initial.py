# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid
from django.conf import settings
import jsonfield2.fields


class Migration(migrations.Migration):

    dependencies = [
        ('protoLib', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomDefinition',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('smNaturalCode', models.CharField(max_length=50, null=True, blank=True, editable=False)),
                ('smRegStatus', models.CharField(max_length=50, null=True, blank=True, editable=False)),
                ('smWflowStatus', models.CharField(max_length=50, null=True, blank=True, editable=False)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('code', models.CharField(max_length=200)),
                ('description', models.TextField(null=True, blank=True, verbose_name='Descriptions')),
                ('active', models.BooleanField(default=True)),
                ('overWrite', models.BooleanField(default=False)),
                ('metaDefinition', jsonfield2.fields.JSONField(default={})),
                ('smCreatedBy', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, related_name='+', editable=False, blank=True)),
                ('smModifiedBy', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, related_name='+', editable=False, blank=True)),
                ('smOwningTeam', models.ForeignKey(to='protoLib.TeamHierarchy', null=True, related_name='+', editable=False, blank=True)),
                ('smOwningUser', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, related_name='+', editable=False, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Parameters',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('smNaturalCode', models.CharField(max_length=50, null=True, blank=True, editable=False)),
                ('smRegStatus', models.CharField(max_length=50, null=True, blank=True, editable=False)),
                ('smWflowStatus', models.CharField(max_length=50, null=True, blank=True, editable=False)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('smInfo', jsonfield2.fields.JSONField(default={})),
                ('parameterKey', models.CharField(max_length=250)),
                ('parameterTag', models.CharField(max_length=250, null=True, blank=True)),
                ('parameterValue', models.CharField(max_length=250)),
                ('smCreatedBy', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, related_name='+', editable=False, blank=True)),
                ('smModifiedBy', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, related_name='+', editable=False, blank=True)),
                ('smOwningTeam', models.ForeignKey(to='protoLib.TeamHierarchy', null=True, related_name='+', editable=False, blank=True)),
                ('smOwningUser', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, related_name='+', editable=False, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ViewDefinition',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('code', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField(null=True, blank=True, verbose_name='Description')),
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
