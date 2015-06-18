# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid
import jsonfield2.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('protoLib', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomDefinition',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('smNaturalCode', models.CharField(max_length=50, blank=True, editable=False, null=True)),
                ('smRegStatus', models.CharField(max_length=50, blank=True, editable=False, null=True)),
                ('smWflowStatus', models.CharField(max_length=50, blank=True, editable=False, null=True)),
                ('smCreatedOn', models.DateTimeField(auto_now_add=True, null=True)),
                ('smModifiedOn', models.DateTimeField(auto_now=True, null=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('code', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, verbose_name='Descriptions', null=True)),
                ('active', models.BooleanField(default=True)),
                ('overWrite', models.BooleanField(default=False)),
                ('metaDefinition', jsonfield2.fields.JSONField(default={})),
                ('smCreatedBy', models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL, blank=True, related_name='+', null=True)),
                ('smModifiedBy', models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL, blank=True, related_name='+', null=True)),
                ('smOwningTeam', models.ForeignKey(editable=False, to='protoLib.TeamHierarchy', blank=True, related_name='+', null=True)),
                ('smOwningUser', models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL, blank=True, related_name='+', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ViewDefinition',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('code', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField(blank=True, verbose_name='Description', null=True)),
                ('active', models.BooleanField(default=True)),
                ('overWrite', models.BooleanField(default=False)),
                ('metaDefinition', jsonfield2.fields.JSONField(default={})),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='customdefinition',
            unique_together=set([('smOwningTeam', 'code')]),
        ),
    ]
