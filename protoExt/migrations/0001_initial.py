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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('smNaturalCode', models.CharField(blank=True, max_length=50, editable=False, null=True)),
                ('smRegStatus', models.CharField(blank=True, max_length=50, editable=False, null=True)),
                ('smWflowStatus', models.CharField(blank=True, max_length=50, editable=False, null=True)),
                ('smCreatedOn', models.DateTimeField(auto_now_add=True, null=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('code', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descriptions')),
                ('active', models.BooleanField(default=True)),
                ('overWrite', models.BooleanField(default=False)),
                ('metaDefinition', jsonfield2.fields.JSONField(default={})),
                ('smCreatedBy', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL, null=True, blank=True, editable=False)),
                ('smModifiedBy', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL, null=True, blank=True, editable=False)),
                ('smOwningTeam', models.ForeignKey(related_name='+', to='protoLib.TeamHierarchy', null=True, blank=True, editable=False)),
                ('smOwningUser', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL, null=True, blank=True, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Parameters',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('smNaturalCode', models.CharField(blank=True, max_length=50, editable=False, null=True)),
                ('smRegStatus', models.CharField(blank=True, max_length=50, editable=False, null=True)),
                ('smWflowStatus', models.CharField(blank=True, max_length=50, editable=False, null=True)),
                ('smCreatedOn', models.DateTimeField(auto_now_add=True, null=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('smInfo', jsonfield2.fields.JSONField(default={})),
                ('parameterKey', models.CharField(max_length=250)),
                ('parameterTag', models.CharField(blank=True, max_length=250, null=True)),
                ('parameterValue', models.CharField(max_length=250)),
                ('smCreatedBy', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL, null=True, blank=True, editable=False)),
                ('smModifiedBy', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL, null=True, blank=True, editable=False)),
                ('smOwningTeam', models.ForeignKey(related_name='+', to='protoLib.TeamHierarchy', null=True, blank=True, editable=False)),
                ('smOwningUser', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL, null=True, blank=True, editable=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ViewDefinition',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
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
