# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import uuid
import jsonfield2.fields


class Migration(migrations.Migration):

    dependencies = [
        ('protoLib', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomDefinition',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('smNaturalCode', models.CharField(null=True, blank=True, max_length=50)),
                ('smRegStatus', models.CharField(null=True, blank=True, max_length=50, editable=False)),
                ('smWflowStatus', models.CharField(null=True, blank=True, max_length=50, editable=False)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('code', models.CharField(max_length=200)),
                ('description', models.TextField(null=True, blank=True, verbose_name='Descriptions')),
                ('active', models.BooleanField(default=True)),
                ('overWrite', models.BooleanField(default=False)),
                ('metaDefinition', jsonfield2.fields.JSONField(default={})),
                ('smCreatedBy', models.ForeignKey(null=True, blank=True, related_name='+', editable=False, to=settings.AUTH_USER_MODEL)),
                ('smModifiedBy', models.ForeignKey(null=True, blank=True, related_name='+', editable=False, to=settings.AUTH_USER_MODEL)),
                ('smOwningTeam', models.ForeignKey(null=True, blank=True, related_name='+', editable=False, to='protoLib.TeamHierarchy')),
                ('smOwningUser', models.ForeignKey(null=True, blank=True, related_name='+', editable=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ViewDefinition',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('code', models.CharField(unique=True, max_length=200)),
                ('description', models.TextField(null=True, blank=True, verbose_name='Description')),
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
