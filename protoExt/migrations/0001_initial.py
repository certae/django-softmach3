# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield2.fields
import uuid
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('protoLib', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomDefinition',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('smNaturalCode', models.CharField(editable=False, null=True, max_length=50, blank=True)),
                ('smRegStatus', models.CharField(editable=False, null=True, max_length=50, blank=True)),
                ('smWflowStatus', models.CharField(editable=False, null=True, max_length=50, blank=True)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('smVersion', models.CharField(editable=False, null=True, default='0', max_length=50, blank=True)),
                ('code', models.CharField(max_length=200)),
                ('description', models.TextField(null=True, verbose_name='Descriptions', blank=True)),
                ('active', models.BooleanField(default=True)),
                ('overWrite', models.BooleanField(default=False)),
                ('metaDefinition', jsonfield2.fields.JSONField(default={})),
                ('smCreatedBy', models.ForeignKey(editable=False, null=True, blank=True, to=settings.AUTH_USER_MODEL, related_name='+')),
                ('smModifiedBy', models.ForeignKey(editable=False, null=True, blank=True, to=settings.AUTH_USER_MODEL, related_name='+')),
                ('smOwningTeam', models.ForeignKey(editable=False, null=True, blank=True, to='protoLib.TeamHierarchy', related_name='+')),
                ('smOwningUser', models.ForeignKey(editable=False, null=True, blank=True, to=settings.AUTH_USER_MODEL, related_name='+')),
            ],
        ),
        migrations.CreateModel(
            name='Parameters',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('smNaturalCode', models.CharField(editable=False, null=True, max_length=50, blank=True)),
                ('smRegStatus', models.CharField(editable=False, null=True, max_length=50, blank=True)),
                ('smWflowStatus', models.CharField(editable=False, null=True, max_length=50, blank=True)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('smVersion', models.CharField(editable=False, null=True, default='0', max_length=50, blank=True)),
                ('smInfo', jsonfield2.fields.JSONField(default={})),
                ('parameterKey', models.CharField(max_length=250)),
                ('parameterTag', models.CharField(null=True, max_length=250, blank=True)),
                ('parameterValue', models.CharField(max_length=250)),
                ('smCreatedBy', models.ForeignKey(editable=False, null=True, blank=True, to=settings.AUTH_USER_MODEL, related_name='+')),
                ('smModifiedBy', models.ForeignKey(editable=False, null=True, blank=True, to=settings.AUTH_USER_MODEL, related_name='+')),
                ('smOwningTeam', models.ForeignKey(editable=False, null=True, blank=True, to='protoLib.TeamHierarchy', related_name='+')),
                ('smOwningUser', models.ForeignKey(editable=False, null=True, blank=True, to=settings.AUTH_USER_MODEL, related_name='+')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ViewDefinition',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('code', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField(null=True, verbose_name='Description', blank=True)),
                ('active', models.BooleanField(default=True)),
                ('overWrite', models.BooleanField(default=False)),
                ('metaDefinition', jsonfield2.fields.JSONField(default={})),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='customdefinition',
            unique_together=set([('code', 'smOwningUser', 'smVersion')]),
        ),
    ]
