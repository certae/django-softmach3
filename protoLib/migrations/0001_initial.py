# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import jsonfield2.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EntityMap',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('entityConfig', jsonfield2.fields.JSONField(default={})),
                ('entityBase', models.OneToOneField(to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='Logger',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('smCreatedOn', models.DateTimeField(auto_now=True, null=True)),
                ('logType', models.CharField(default='INF', max_length=10)),
                ('logObject', models.CharField(max_length=250, null=True, blank=True)),
                ('logNotes', models.CharField(max_length=250, null=True, blank=True)),
                ('logInfo', models.TextField(null=True, blank=True)),
                ('logKey', models.CharField(default='', choices=[('INF', 'INFO'), ('WAR', 'WARNING'), ('ERR', 'ERROR'), ('INS', 'INSERT'), ('UPD', 'UPDATE'), ('DEL', 'DELETE')], max_length=5)),
                ('smCreatedBy', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='+', null=True, editable=False, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='TeamHierarchy',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('code', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField(verbose_name='Descriptions', null=True, blank=True)),
                ('site', models.IntegerField(null=True, blank=True)),
                ('parentNode', models.ForeignKey(to='protoLib.TeamHierarchy', related_name='downHierachy', null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserContext',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('smNaturalCode', models.CharField(max_length=50, blank=True, null=True, editable=False)),
                ('smRegStatus', models.CharField(max_length=50, blank=True, null=True, editable=False)),
                ('smWflowStatus', models.CharField(max_length=50, blank=True, null=True, editable=False)),
                ('smCreatedOn', models.DateTimeField(auto_now_add=True, null=True)),
                ('smModifiedOn', models.DateTimeField(auto_now=True, null=True)),
                ('smUUID', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('propName', models.CharField(max_length=500)),
                ('propValue', models.CharField(max_length=200)),
                ('propDescription', models.TextField(null=True, blank=True)),
                ('isDefault', models.BooleanField(default=True)),
                ('isFilter', models.BooleanField(default=True)),
                ('modelCType', models.ForeignKey(to='contenttypes.ContentType')),
                ('smCreatedBy', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='+', null=True, editable=False, blank=True)),
                ('smModifiedBy', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='+', null=True, editable=False, blank=True)),
                ('smOwningTeam', models.ForeignKey(to='protoLib.TeamHierarchy', related_name='+', null=True, editable=False, blank=True)),
                ('smOwningUser', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='+', null=True, editable=False, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('language', models.CharField(max_length=500, null=True, blank=True)),
                ('userTree', models.CharField(max_length=500, null=True, blank=True)),
                ('userConfig', jsonfield2.fields.JSONField(default={})),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
                ('userTeam', models.ForeignKey(to='protoLib.TeamHierarchy', related_name='userTeam', null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='logger',
            name='smOwningTeam',
            field=models.ForeignKey(to='protoLib.TeamHierarchy', related_name='+', null=True, editable=False, blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='usercontext',
            unique_together=set([('modelCType', 'propName', 'smOwningUser')]),
        ),
    ]
