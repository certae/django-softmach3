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
            name='CustomDefinition',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('smRegStatus', models.CharField(editable=False, blank=True, max_length=50, null=True)),
                ('smWflowStatus', models.CharField(editable=False, blank=True, max_length=50, null=True)),
                ('smCreatedOn', models.DateTimeField(auto_now_add=True, null=True)),
                ('smModifiedOn', models.DateTimeField(auto_now=True, null=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('code', models.CharField(max_length=200)),
                ('description', models.TextField(null=True, verbose_name='Descriptions', blank=True)),
                ('active', models.BooleanField(default=True)),
                ('overWrite', models.BooleanField(default=False)),
                ('metaDefinition', jsonfield2.fields.JSONField(default={})),
                ('smCreatedBy', models.ForeignKey(related_name='+', null=True, editable=False, blank=True, to=settings.AUTH_USER_MODEL)),
                ('smModifiedBy', models.ForeignKey(related_name='+', null=True, editable=False, blank=True, to=settings.AUTH_USER_MODEL)),
                ('smOwningTeam', models.ForeignKey(related_name='+', null=True, editable=False, blank=True, to='protoLib.TeamHierarchy')),
                ('smOwningUser', models.ForeignKey(related_name='+', null=True, editable=False, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ViewDefinition',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('code', models.CharField(unique=True, max_length=200)),
                ('description', models.TextField(null=True, verbose_name='Description', blank=True)),
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
