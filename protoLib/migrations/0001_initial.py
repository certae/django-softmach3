# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid
import jsonfield2.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntityMap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('entityConfig', jsonfield2.fields.JSONField(default={})),
                ('entityBase', models.OneToOneField(to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='TeamHierarchy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('code', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField(verbose_name='Descriptions', blank=True, null=True)),
                ('site', models.IntegerField(blank=True, null=True)),
                ('parentNode', models.ForeignKey(related_name='downHierachy', blank=True, null=True, to='protoLib.TeamHierarchy')),
            ],
        ),
        migrations.CreateModel(
            name='UserContext',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('smNaturalCode', models.CharField(blank=True, max_length=50, editable=False, null=True)),
                ('smRegStatus', models.CharField(blank=True, max_length=50, editable=False, null=True)),
                ('smWflowStatus', models.CharField(blank=True, max_length=50, editable=False, null=True)),
                ('smCreatedOn', models.DateTimeField(auto_now_add=True, null=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('propName', models.CharField(max_length=500)),
                ('propValue', models.CharField(max_length=200)),
                ('propDescription', models.TextField(blank=True, null=True)),
                ('isDefault', models.BooleanField(default=True)),
                ('isFilter', models.BooleanField(default=True)),
                ('modelCType', models.ForeignKey(to='contenttypes.ContentType')),
                ('smCreatedBy', models.ForeignKey(related_name='+', blank=True, null=True, to=settings.AUTH_USER_MODEL, editable=False)),
                ('smModifiedBy', models.ForeignKey(related_name='+', blank=True, null=True, to=settings.AUTH_USER_MODEL, editable=False)),
                ('smOwningTeam', models.ForeignKey(related_name='+', blank=True, null=True, to='protoLib.TeamHierarchy', editable=False)),
                ('smOwningUser', models.ForeignKey(related_name='+', blank=True, null=True, to=settings.AUTH_USER_MODEL, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('language', models.CharField(blank=True, max_length=500, null=True)),
                ('userTree', models.CharField(blank=True, max_length=500, null=True)),
                ('userConfig', jsonfield2.fields.JSONField(default={})),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
                ('userTeam', models.ForeignKey(related_name='userTeam', blank=True, null=True, to='protoLib.TeamHierarchy')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='usercontext',
            unique_together=set([('modelCType', 'propName', 'smOwningUser')]),
        ),
    ]
