# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid
from django.conf import settings
import jsonfield2.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('protoLib', '0002_pruebas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pruebas2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smRegStatus', models.CharField(null=True, max_length=50, blank=True, editable=False)),
                ('smWflowStatus', models.CharField(null=True, max_length=50, blank=True, editable=False)),
                ('smCreatedOn', models.DateTimeField(auto_now_add=True, null=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('metaDefinition', jsonfield2.fields.JSONField(default={})),
                ('code', models.CharField(max_length=250)),
                ('smCreatedBy', models.ForeignKey(related_name='+', null=True, to=settings.AUTH_USER_MODEL, editable=False, blank=True)),
                ('smModifiedBy', models.ForeignKey(related_name='+', null=True, to=settings.AUTH_USER_MODEL, editable=False, blank=True)),
                ('smOwningTeam', models.ForeignKey(related_name='+', null=True, to='protoLib.TeamHierarchy', editable=False, blank=True)),
                ('smOwningUser', models.ForeignKey(related_name='+', null=True, to=settings.AUTH_USER_MODEL, editable=False, blank=True)),
            ],
            options={
            },
        ),
        migrations.RemoveField(
            model_name='pruebas',
            name='smCreatedBy',
        ),
        migrations.RemoveField(
            model_name='pruebas',
            name='smModifiedBy',
        ),
        migrations.RemoveField(
            model_name='pruebas',
            name='smOwningTeam',
        ),
        migrations.RemoveField(
            model_name='pruebas',
            name='smOwningUser',
        ),
        migrations.DeleteModel(
            name='Pruebas',
        ),
    ]
