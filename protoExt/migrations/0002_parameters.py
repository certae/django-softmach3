# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid
import jsonfield2.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('protoLib', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('protoExt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parameters',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('smNaturalCode', models.CharField(null=True, max_length=50, blank=True, editable=False)),
                ('smRegStatus', models.CharField(null=True, max_length=50, blank=True, editable=False)),
                ('smWflowStatus', models.CharField(null=True, max_length=50, blank=True, editable=False)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(auto_now=True, null=True)),
                ('smUUID', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('smInfo', jsonfield2.fields.JSONField(default={})),
                ('parameterKey', models.CharField(max_length=250)),
                ('parameterTag', models.CharField(null=True, blank=True, max_length=250)),
                ('parameterValue', models.CharField(max_length=250)),
                ('smCreatedBy', models.ForeignKey(related_name='+', null=True, blank=True, to=settings.AUTH_USER_MODEL, editable=False)),
                ('smModifiedBy', models.ForeignKey(related_name='+', null=True, blank=True, to=settings.AUTH_USER_MODEL, editable=False)),
                ('smOwningTeam', models.ForeignKey(related_name='+', null=True, blank=True, to='protoLib.TeamHierarchy', editable=False)),
                ('smOwningUser', models.ForeignKey(related_name='+', null=True, blank=True, to=settings.AUTH_USER_MODEL, editable=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
