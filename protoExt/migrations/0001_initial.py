# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import jsonfield2.fields
import uuid


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
                ('smNaturalCode', models.CharField(max_length=50, blank=True, null=True, editable=False)),
                ('smRegStatus', models.CharField(max_length=50, blank=True, null=True, editable=False)),
                ('smWflowStatus', models.CharField(max_length=50, blank=True, null=True, editable=False)),
                ('smCreatedOn', models.DateTimeField(auto_now_add=True, null=True)),
                ('smModifiedOn', models.DateTimeField(auto_now=True, null=True)),
                ('smUUID', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('code', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, verbose_name='Descriptions', null=True)),
                ('active', models.BooleanField(default=True)),
                ('overWrite', models.BooleanField(default=False)),
                ('metaDefinition', jsonfield2.fields.JSONField(default={})),
                ('smCreatedBy', models.ForeignKey(related_name='+', null=True, editable=False, to=settings.AUTH_USER_MODEL, blank=True)),
                ('smModifiedBy', models.ForeignKey(related_name='+', null=True, editable=False, to=settings.AUTH_USER_MODEL, blank=True)),
                ('smOwningTeam', models.ForeignKey(related_name='+', null=True, editable=False, to='protoLib.TeamHierarchy', blank=True)),
                ('smOwningUser', models.ForeignKey(related_name='+', null=True, editable=False, to=settings.AUTH_USER_MODEL, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Parameters',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('smNaturalCode', models.CharField(max_length=50, blank=True, null=True, editable=False)),
                ('smRegStatus', models.CharField(max_length=50, blank=True, null=True, editable=False)),
                ('smWflowStatus', models.CharField(max_length=50, blank=True, null=True, editable=False)),
                ('smCreatedOn', models.DateTimeField(auto_now_add=True, null=True)),
                ('smModifiedOn', models.DateTimeField(auto_now=True, null=True)),
                ('smUUID', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('smInfo', jsonfield2.fields.JSONField(default={})),
                ('parameterKey', models.CharField(max_length=250)),
                ('parameterTag', models.CharField(max_length=250, blank=True, null=True)),
                ('parameterValue', models.CharField(max_length=250)),
                ('smCreatedBy', models.ForeignKey(related_name='+', null=True, editable=False, to=settings.AUTH_USER_MODEL, blank=True)),
                ('smModifiedBy', models.ForeignKey(related_name='+', null=True, editable=False, to=settings.AUTH_USER_MODEL, blank=True)),
                ('smOwningTeam', models.ForeignKey(related_name='+', null=True, editable=False, to='protoLib.TeamHierarchy', blank=True)),
                ('smOwningUser', models.ForeignKey(related_name='+', null=True, editable=False, to=settings.AUTH_USER_MODEL, blank=True)),
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
                ('description', models.TextField(blank=True, verbose_name='Description', null=True)),
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
