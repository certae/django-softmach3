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
            name='ContextEntity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('smNaturalCode', models.CharField(blank=True, null=True, max_length=50, editable=False)),
                ('smRegStatus', models.CharField(blank=True, null=True, max_length=50, editable=False)),
                ('smWflowStatus', models.CharField(blank=True, null=True, max_length=50, editable=False)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('smVersion', models.CharField(blank=True, null=True, default='0', max_length=50, editable=False)),
                ('propName', models.CharField(blank=True, null=True, default='', max_length=200)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContextUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('smNaturalCode', models.CharField(blank=True, null=True, max_length=50, editable=False)),
                ('smRegStatus', models.CharField(blank=True, null=True, max_length=50, editable=False)),
                ('smWflowStatus', models.CharField(blank=True, null=True, max_length=50, editable=False)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('smVersion', models.CharField(blank=True, null=True, default='0', max_length=50, editable=False)),
                ('propValue', models.CharField(max_length=200)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContextVar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('smNaturalCode', models.CharField(blank=True, null=True, max_length=50, editable=False)),
                ('smRegStatus', models.CharField(blank=True, null=True, max_length=50, editable=False)),
                ('smWflowStatus', models.CharField(blank=True, null=True, max_length=50, editable=False)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('smVersion', models.CharField(blank=True, null=True, default='0', max_length=50, editable=False)),
                ('propName', models.CharField(default='', max_length=500)),
                ('propDescription', models.TextField(blank=True, null=True)),
                ('isDefault', models.BooleanField(default=True)),
                ('isFilter', models.BooleanField(default=True)),
                ('modelCType', models.OneToOneField(to='contenttypes.ContentType')),
                ('smCreatedBy', models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('smModifiedBy', models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('list_%(class)', 'Can list available %(class)s'),),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EntityMap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('entityConfig', jsonfield2.fields.JSONField(default={})),
                ('entityBase', models.OneToOneField(to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='Logger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now=True)),
                ('logType', models.CharField(default='INF', max_length=10)),
                ('logObject', models.CharField(blank=True, null=True, max_length=250)),
                ('logNotes', models.CharField(blank=True, null=True, max_length=250)),
                ('logInfo', models.TextField(blank=True, null=True)),
                ('logKey', models.CharField(default='', max_length=5, choices=[('INF', 'INFO'), ('WAR', 'WARNING'), ('ERR', 'ERROR'), ('INS', 'INSERT'), ('UPD', 'UPDATE'), ('DEL', 'DELETE')])),
                ('smCreatedBy', models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TeamHierarchy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('code', models.CharField(unique=True, max_length=200)),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descriptions')),
                ('site', models.IntegerField(blank=True, null=True)),
                ('parentNode', models.ForeignKey(blank=True, null=True, related_name='downHierachy', to='protoLib.TeamHierarchy')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('language', models.CharField(blank=True, null=True, max_length=500)),
                ('userTree', models.CharField(blank=True, null=True, max_length=500)),
                ('userConfig', jsonfield2.fields.JSONField(default={})),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
                ('userTeam', models.ForeignKey(blank=True, null=True, related_name='userTeam', to='protoLib.TeamHierarchy')),
            ],
        ),
        migrations.CreateModel(
            name='VersionHeaders',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('exclude', models.BooleanField(default=False)),
                ('modelCType', models.ForeignKey(to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='VersionTitle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('versionCode', models.CharField(blank=True, null=True, default='0', max_length=50)),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descriptions')),
                ('active', models.BooleanField(default=True)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smCreatedBy', models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('smModifiedBy', models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('versionBase', models.ForeignKey(blank=True, null=True, to='protoLib.VersionTitle')),
            ],
        ),
        migrations.CreateModel(
            name='VersionUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('active', models.BooleanField(default=False)),
                ('user', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL)),
                ('version', models.ForeignKey(blank=True, null=True, to='protoLib.VersionTitle')),
            ],
        ),
        migrations.AddField(
            model_name='logger',
            name='smOwningTeam',
            field=models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to='protoLib.TeamHierarchy'),
        ),
        migrations.AddField(
            model_name='contextvar',
            name='smOwningTeam',
            field=models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to='protoLib.TeamHierarchy'),
        ),
        migrations.AddField(
            model_name='contextvar',
            name='smOwningUser',
            field=models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='contextuser',
            name='contextVar',
            field=models.ForeignKey(to='protoLib.ContextVar'),
        ),
        migrations.AddField(
            model_name='contextuser',
            name='smCreatedBy',
            field=models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='contextuser',
            name='smModifiedBy',
            field=models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='contextuser',
            name='smOwningTeam',
            field=models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to='protoLib.TeamHierarchy'),
        ),
        migrations.AddField(
            model_name='contextuser',
            name='smOwningUser',
            field=models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL),
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
            field=models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='contextentity',
            name='smModifiedBy',
            field=models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='contextentity',
            name='smOwningTeam',
            field=models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to='protoLib.TeamHierarchy'),
        ),
        migrations.AddField(
            model_name='contextentity',
            name='smOwningUser',
            field=models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='versionuser',
            unique_together=set([('version', 'user')]),
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
