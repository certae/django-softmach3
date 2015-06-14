# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('entityConfig', jsonfield2.fields.JSONField(default={})),
                ('entityBase', models.OneToOneField(to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='TeamHierarchy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('code', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descriptions')),
                ('site', models.IntegerField(blank=True, null=True)),
                ('parentNode', models.ForeignKey(related_name='downHierachy', blank=True, null=True, to='protoLib.TeamHierarchy')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('language', models.CharField(blank=True, max_length=500, null=True)),
                ('userTree', models.CharField(blank=True, max_length=500, null=True)),
                ('userConfig', jsonfield2.fields.JSONField(default={})),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
                ('userTeam', models.ForeignKey(related_name='userTeam', blank=True, null=True, to='protoLib.TeamHierarchy')),
            ],
        ),
    ]
