# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import uuid
import jsonfield2.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('protoLib', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pruebas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('smRegStatus', models.CharField(editable=False, max_length=50, null=True, blank=True)),
                ('smWflowStatus', models.CharField(editable=False, max_length=50, null=True, blank=True)),
                ('smCreatedOn', models.DateTimeField(auto_now_add=True, null=True)),
                ('smModifiedOn', models.DateTimeField(auto_now=True, null=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('metaDefinition', jsonfield2.fields.JSONField(default={})),
                ('code', models.CharField(max_length=250)),
                ('smCreatedBy', models.ForeignKey(related_name='+', null=True, to=settings.AUTH_USER_MODEL, editable=False, blank=True)),
                ('smModifiedBy', models.ForeignKey(related_name='+', null=True, to=settings.AUTH_USER_MODEL, editable=False, blank=True)),
                ('smOwningTeam', models.ForeignKey(related_name='+', null=True, to='protoLib.TeamHierarchy', editable=False, blank=True)),
                ('smOwningUser', models.ForeignKey(related_name='+', null=True, to=settings.AUTH_USER_MODEL, editable=False, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
