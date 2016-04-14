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
            name='ContextEntity',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('smNaturalCode', models.CharField(null=True, blank=True, editable=False, max_length=50)),
                ('smRegStatus', models.CharField(null=True, blank=True, editable=False, max_length=50)),
                ('smWflowStatus', models.CharField(null=True, blank=True, editable=False, max_length=50)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('propName', models.CharField(blank=True, null=True, max_length=200, default='')),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContextUser',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('smNaturalCode', models.CharField(null=True, blank=True, editable=False, max_length=50)),
                ('smRegStatus', models.CharField(null=True, blank=True, editable=False, max_length=50)),
                ('smWflowStatus', models.CharField(null=True, blank=True, editable=False, max_length=50)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('propValue', models.CharField(blank=True, null=True, max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContextVar',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('smNaturalCode', models.CharField(null=True, blank=True, editable=False, max_length=50)),
                ('smRegStatus', models.CharField(null=True, blank=True, editable=False, max_length=50)),
                ('smWflowStatus', models.CharField(null=True, blank=True, editable=False, max_length=50)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('propName', models.CharField(max_length=500, default='id')),
                ('description', models.TextField(blank=True, null=True)),
                ('modelCType', models.ForeignKey(to='contenttypes.ContentType')),
                ('smCreatedBy', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, editable=False, null=True, related_name='+')),
                ('smModifiedBy', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, editable=False, null=True, related_name='+')),
            ],
        ),
        migrations.CreateModel(
            name='EntityMap',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('entityConfig', jsonfield2.fields.JSONField(default={})),
                ('entityBase', models.OneToOneField(to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='Logger',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now=True)),
                ('logType', models.CharField(max_length=10, default='INF')),
                ('logObject', models.CharField(blank=True, null=True, max_length=250)),
                ('logNotes', models.CharField(blank=True, null=True, max_length=250)),
                ('logInfo', models.TextField(blank=True, null=True)),
                ('logKey', models.CharField(max_length=5, default='', choices=[('INF', 'INFO'), ('WAR', 'WARNING'), ('ERR', 'ERROR'), ('INS', 'INSERT'), ('UPD', 'UPDATE'), ('DEL', 'DELETE')])),
                ('smCreatedBy', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, editable=False, null=True, related_name='+')),
            ],
        ),
        migrations.CreateModel(
            name='TeamHierarchy',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('code', models.CharField(unique=True, max_length=200)),
                ('description', models.TextField(blank=True, verbose_name='Descriptions', null=True)),
                ('site', models.IntegerField(blank=True, null=True)),
                ('parentNode', models.ForeignKey(blank=True, to='protoLib.TeamHierarchy', related_name='downHierachy', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('language', models.CharField(blank=True, null=True, max_length=500)),
                ('userTree', models.CharField(blank=True, null=True, max_length=500)),
                ('userConfig', jsonfield2.fields.JSONField(default={})),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
                ('userTeam', models.ForeignKey(blank=True, to='protoLib.TeamHierarchy', related_name='userTeam', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='logger',
            name='smOwningTeam',
            field=models.ForeignKey(blank=True, to='protoLib.TeamHierarchy', editable=False, null=True, related_name='+'),
        ),
        migrations.AddField(
            model_name='contextvar',
            name='smOwningTeam',
            field=models.ForeignKey(blank=True, to='protoLib.TeamHierarchy', editable=False, null=True, related_name='+'),
        ),
        migrations.AddField(
            model_name='contextvar',
            name='smOwningUser',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, editable=False, null=True, related_name='+'),
        ),
        migrations.AddField(
            model_name='contextuser',
            name='contextVar',
            field=models.ForeignKey(to='protoLib.ContextVar'),
        ),
        migrations.AddField(
            model_name='contextuser',
            name='smCreatedBy',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, editable=False, null=True, related_name='+'),
        ),
        migrations.AddField(
            model_name='contextuser',
            name='smModifiedBy',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, editable=False, null=True, related_name='+'),
        ),
        migrations.AddField(
            model_name='contextuser',
            name='smOwningTeam',
            field=models.ForeignKey(blank=True, to='protoLib.TeamHierarchy', editable=False, null=True, related_name='+'),
        ),
        migrations.AddField(
            model_name='contextuser',
            name='smOwningUser',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, editable=False, null=True, related_name='+'),
        ),
        migrations.AddField(
            model_name='contextentity',
            name='contextVar',
            field=models.ForeignKey(to='protoLib.ContextVar'),
        ),
        migrations.AddField(
            model_name='contextentity',
            name='entity',
            field=models.ForeignKey(to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='contextentity',
            name='smCreatedBy',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, editable=False, null=True, related_name='+'),
        ),
        migrations.AddField(
            model_name='contextentity',
            name='smModifiedBy',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, editable=False, null=True, related_name='+'),
        ),
        migrations.AddField(
            model_name='contextentity',
            name='smOwningTeam',
            field=models.ForeignKey(blank=True, to='protoLib.TeamHierarchy', editable=False, null=True, related_name='+'),
        ),
        migrations.AddField(
            model_name='contextentity',
            name='smOwningUser',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, editable=False, null=True, related_name='+'),
        ),
        migrations.AlterUniqueTogether(
            name='contextvar',
            unique_together=set([('modelCType', 'propName')]),
        ),
        migrations.AlterUniqueTogether(
            name='contextuser',
            unique_together=set([('contextVar', 'smOwningUser')]),
        ),
        migrations.AlterUniqueTogether(
            name='contextentity',
            unique_together=set([('contextVar', 'entity')]),
        ),
    ]
