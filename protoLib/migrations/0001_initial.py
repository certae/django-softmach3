# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield2.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
                ('parentNode', models.ForeignKey(blank=True, null=True, to='protoLib.TeamHierarchy', related_name='downHierachy')),
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
                ('userTeam', models.ForeignKey(blank=True, null=True, to='protoLib.TeamHierarchy', related_name='userTeam')),
            ],
        ),
    ]
