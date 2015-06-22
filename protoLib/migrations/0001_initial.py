# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import uuid
import jsonfield2.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntityMap',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('entityConfig', jsonfield2.fields.JSONField(default={})),
                ('entityBase', models.OneToOneField(to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='TeamHierarchy',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('code', models.CharField(unique=True, max_length=200)),
                ('description', models.TextField(verbose_name='Descriptions', blank=True, null=True)),
                ('site', models.IntegerField(blank=True, null=True)),
                ('parentNode', models.ForeignKey(to='protoLib.TeamHierarchy', blank=True, null=True, related_name='downHierachy')),
            ],
        ),
        migrations.CreateModel(
            name='UserContext',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('smNaturalCode', models.CharField(editable=False, blank=True, null=True, max_length=50)),
                ('smRegStatus', models.CharField(editable=False, blank=True, null=True, max_length=50)),
                ('smWflowStatus', models.CharField(editable=False, blank=True, null=True, max_length=50)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(auto_now=True, null=True)),
                ('smUUID', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('propName', models.CharField(max_length=500)),
                ('propValue', models.CharField(max_length=200)),
                ('propDescription', models.TextField(blank=True, null=True)),
                ('isDefault', models.BooleanField(default=True)),
                ('isFilter', models.BooleanField(default=True)),
                ('modelCType', models.ForeignKey(to='contenttypes.ContentType')),
                ('smCreatedBy', models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, null=True, related_name='+', editable=False)),
                ('smModifiedBy', models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, null=True, related_name='+', editable=False)),
                ('smOwningTeam', models.ForeignKey(to='protoLib.TeamHierarchy', blank=True, null=True, related_name='+', editable=False)),
                ('smOwningUser', models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, null=True, related_name='+', editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('language', models.CharField(blank=True, null=True, max_length=500)),
                ('userTree', models.CharField(blank=True, null=True, max_length=500)),
                ('userConfig', jsonfield2.fields.JSONField(default={})),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
                ('userTeam', models.ForeignKey(to='protoLib.TeamHierarchy', blank=True, null=True, related_name='userTeam')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='usercontext',
            unique_together=set([('modelCType', 'propName', 'smOwningUser')]),
        ),
    ]
