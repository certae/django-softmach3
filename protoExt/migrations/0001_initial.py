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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('smNaturalCode', models.CharField(blank=True, max_length=50, editable=False, null=True)),
                ('smRegStatus', models.CharField(blank=True, max_length=50, editable=False, null=True)),
                ('smWflowStatus', models.CharField(blank=True, max_length=50, editable=False, null=True)),
                ('smCreatedOn', models.DateTimeField(auto_now_add=True, null=True)),
                ('smModifiedOn', models.DateTimeField(auto_now=True, null=True)),
                ('smUUID', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('code', models.CharField(max_length=200)),
                ('description', models.TextField(verbose_name='Descriptions', null=True, blank=True)),
                ('active', models.BooleanField(default=True)),
                ('overWrite', models.BooleanField(default=False)),
                ('metaDefinition', jsonfield2.fields.JSONField(default={})),
                ('smCreatedBy', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, related_name='+', null=True, editable=False)),
                ('smModifiedBy', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, related_name='+', null=True, editable=False)),
                ('smOwningTeam', models.ForeignKey(blank=True, to='protoLib.TeamHierarchy', related_name='+', null=True, editable=False)),
                ('smOwningUser', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, related_name='+', null=True, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='ViewDefinition',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('code', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField(verbose_name='Description', null=True, blank=True)),
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
