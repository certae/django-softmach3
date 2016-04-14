# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield2.fields
import uuid
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContextEntity',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('smNaturalCode', models.CharField(null=True, editable=False, max_length=50, blank=True)),
                ('smRegStatus', models.CharField(null=True, editable=False, max_length=50, blank=True)),
                ('smWflowStatus', models.CharField(null=True, editable=False, max_length=50, blank=True)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('propName', models.CharField(null=True, default='', max_length=200, blank=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContextUser',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('smNaturalCode', models.CharField(null=True, editable=False, max_length=50, blank=True)),
                ('smRegStatus', models.CharField(null=True, editable=False, max_length=50, blank=True)),
                ('smWflowStatus', models.CharField(null=True, editable=False, max_length=50, blank=True)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('propValue', models.CharField(null=True, max_length=200, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContextVar',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('smNaturalCode', models.CharField(null=True, editable=False, max_length=50, blank=True)),
                ('smRegStatus', models.CharField(null=True, editable=False, max_length=50, blank=True)),
                ('smWflowStatus', models.CharField(null=True, editable=False, max_length=50, blank=True)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('propName', models.CharField(default='id', max_length=500)),
                ('description', models.TextField(null=True, blank=True)),
                ('modelCType', models.ForeignKey(to='contenttypes.ContentType')),
                ('smCreatedBy', models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, related_name='+', null=True, editable=False)),
                ('smModifiedBy', models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, related_name='+', null=True, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='EntityMap',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('entityConfig', jsonfield2.fields.JSONField(default={})),
                ('entityBase', models.OneToOneField(to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='Logger',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now=True)),
                ('logType', models.CharField(default='INF', max_length=10)),
                ('logObject', models.CharField(null=True, max_length=250, blank=True)),
                ('logNotes', models.CharField(null=True, max_length=250, blank=True)),
                ('logInfo', models.TextField(null=True, blank=True)),
                ('logKey', models.CharField(choices=[('INF', 'INFO'), ('WAR', 'WARNING'), ('ERR', 'ERROR'), ('INS', 'INSERT'), ('UPD', 'UPDATE'), ('DEL', 'DELETE')], default='', max_length=5)),
                ('smCreatedBy', models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, related_name='+', null=True, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='TeamHierarchy',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('code', models.CharField(unique=True, max_length=200)),
                ('description', models.TextField(null=True, verbose_name='Descriptions', blank=True)),
                ('site', models.IntegerField(null=True, blank=True)),
                ('parentNode', models.ForeignKey(to='protoLib.TeamHierarchy', related_name='downHierachy', null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('language', models.CharField(null=True, max_length=500, blank=True)),
                ('userTree', models.CharField(null=True, max_length=500, blank=True)),
                ('userConfig', jsonfield2.fields.JSONField(default={})),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
                ('userTeam', models.ForeignKey(to='protoLib.TeamHierarchy', related_name='userTeam', null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='logger',
            name='smOwningTeam',
            field=models.ForeignKey(to='protoLib.TeamHierarchy', blank=True, related_name='+', null=True, editable=False),
        ),
        migrations.AddField(
            model_name='contextvar',
            name='smOwningTeam',
            field=models.ForeignKey(to='protoLib.TeamHierarchy', blank=True, related_name='+', null=True, editable=False),
        ),
        migrations.AddField(
            model_name='contextvar',
            name='smOwningUser',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, related_name='+', null=True, editable=False),
        ),
        migrations.AddField(
            model_name='contextuser',
            name='contextVar',
            field=models.ForeignKey(to='protoLib.ContextVar'),
        ),
        migrations.AddField(
            model_name='contextuser',
            name='smCreatedBy',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, related_name='+', null=True, editable=False),
        ),
        migrations.AddField(
            model_name='contextuser',
            name='smModifiedBy',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, related_name='+', null=True, editable=False),
        ),
        migrations.AddField(
            model_name='contextuser',
            name='smOwningTeam',
            field=models.ForeignKey(to='protoLib.TeamHierarchy', blank=True, related_name='+', null=True, editable=False),
        ),
        migrations.AddField(
            model_name='contextuser',
            name='smOwningUser',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, related_name='+', null=True, editable=False),
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
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, related_name='+', null=True, editable=False),
        ),
        migrations.AddField(
            model_name='contextentity',
            name='smModifiedBy',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, related_name='+', null=True, editable=False),
        ),
        migrations.AddField(
            model_name='contextentity',
            name='smOwningTeam',
            field=models.ForeignKey(to='protoLib.TeamHierarchy', blank=True, related_name='+', null=True, editable=False),
        ),
        migrations.AddField(
            model_name='contextentity',
            name='smOwningUser',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, related_name='+', null=True, editable=False),
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
