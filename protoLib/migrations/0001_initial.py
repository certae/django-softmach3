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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('entityConfig', jsonfield2.fields.JSONField(default={})),
                ('entityBase', models.OneToOneField(to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='Logger',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('smCreatedOn', models.DateTimeField(auto_now=True, null=True)),
                ('logType', models.CharField(default='INF', max_length=10)),
                ('logObject', models.CharField(max_length=250, blank=True, null=True)),
                ('logNotes', models.CharField(max_length=250, blank=True, null=True)),
                ('logInfo', models.TextField(blank=True, null=True)),
                ('logKey', models.CharField(default='', max_length=5, choices=[('INF', 'INFO'), ('WAR', 'WARNING'), ('ERR', 'ERROR'), ('INS', 'INSERT'), ('UPD', 'UPDATE'), ('DEL', 'DELETE')])),
                ('smCreatedBy', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL, blank=True, null=True, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='TeamHierarchy',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('code', models.CharField(unique=True, max_length=200)),
                ('description', models.TextField(blank=True, verbose_name='Descriptions', null=True)),
                ('site', models.IntegerField(blank=True, null=True)),
                ('parentNode', models.ForeignKey(related_name='downHierachy', blank=True, to='protoLib.TeamHierarchy', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserContext',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('smNaturalCode', models.CharField(editable=False, max_length=50, blank=True, null=True)),
                ('smRegStatus', models.CharField(editable=False, max_length=50, blank=True, null=True)),
                ('smWflowStatus', models.CharField(editable=False, max_length=50, blank=True, null=True)),
                ('smCreatedOn', models.DateTimeField(auto_now_add=True, null=True)),
                ('smModifiedOn', models.DateTimeField(auto_now=True, null=True)),
                ('smUUID', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('propName', models.CharField(max_length=500)),
                ('propValue', models.CharField(max_length=200)),
                ('propDescription', models.TextField(blank=True, null=True)),
                ('isDefault', models.BooleanField(default=True)),
                ('isFilter', models.BooleanField(default=True)),
                ('modelCType', models.ForeignKey(to='contenttypes.ContentType')),
                ('smCreatedBy', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL, blank=True, null=True, editable=False)),
                ('smModifiedBy', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL, blank=True, null=True, editable=False)),
                ('smOwningTeam', models.ForeignKey(related_name='+', to='protoLib.TeamHierarchy', blank=True, null=True, editable=False)),
                ('smOwningUser', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL, blank=True, null=True, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('language', models.CharField(max_length=500, blank=True, null=True)),
                ('userTree', models.CharField(max_length=500, blank=True, null=True)),
                ('userConfig', jsonfield2.fields.JSONField(default={})),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
                ('userTeam', models.ForeignKey(related_name='userTeam', blank=True, to='protoLib.TeamHierarchy', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='logger',
            name='smOwningTeam',
            field=models.ForeignKey(related_name='+', to='protoLib.TeamHierarchy', blank=True, null=True, editable=False),
        ),
        migrations.AlterUniqueTogether(
            name='usercontext',
            unique_together=set([('modelCType', 'propName', 'smOwningUser')]),
        ),
    ]
