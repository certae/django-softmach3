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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('smNaturalCode', models.CharField(editable=False, blank=True, max_length=50, null=True)),
                ('smRegStatus', models.CharField(editable=False, blank=True, max_length=50, null=True)),
                ('smWflowStatus', models.CharField(editable=False, blank=True, max_length=50, null=True)),
                ('smCreatedOn', models.DateTimeField(auto_now_add=True, null=True)),
                ('smModifiedOn', models.DateTimeField(auto_now=True, null=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('code', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descriptions')),
                ('active', models.BooleanField(default=True)),
                ('overWrite', models.BooleanField(default=False)),
                ('metaDefinition', jsonfield2.fields.JSONField(default={})),
                ('smCreatedBy', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, editable=False, null=True, related_name='+')),
                ('smModifiedBy', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, editable=False, null=True, related_name='+')),
                ('smOwningTeam', models.ForeignKey(blank=True, to='protoLib.TeamHierarchy', editable=False, null=True, related_name='+')),
                ('smOwningUser', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, editable=False, null=True, related_name='+')),
            ],
        ),
        migrations.CreateModel(
            name='ViewDefinition',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('code', models.CharField(unique=True, max_length=200)),
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
