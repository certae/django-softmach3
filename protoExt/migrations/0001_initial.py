# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield2.fields
from django.conf import settings
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('smRegStatus', models.CharField(max_length=50, blank=True, null=True, editable=False)),
                ('smWflowStatus', models.CharField(max_length=50, blank=True, null=True, editable=False)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('code', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, verbose_name='Descriptions', null=True)),
                ('active', models.BooleanField(default=True)),
                ('overWrite', models.BooleanField(default=False)),
                ('metaDefinition', jsonfield2.fields.JSONField(default={})),
                ('smCreatedBy', models.ForeignKey(blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True, related_name='+')),
                ('smModifiedBy', models.ForeignKey(blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True, related_name='+')),
                ('smOwningTeam', models.ForeignKey(blank=True, editable=False, to='protoLib.TeamHierarchy', null=True, related_name='+')),
                ('smOwningUser', models.ForeignKey(blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True, related_name='+')),
            ],
        ),
        migrations.CreateModel(
            name='ViewDefinition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
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
