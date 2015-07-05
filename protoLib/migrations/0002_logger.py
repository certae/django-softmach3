# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('protoLib', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logger',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now=True)),
                ('logType', models.CharField(default='INF', max_length=10)),
                ('logObject', models.CharField(blank=True, null=True, max_length=250)),
                ('logNotes', models.CharField(blank=True, null=True, max_length=250)),
                ('logInfo', models.TextField(blank=True, null=True)),
                ('logKey', models.CharField(default='', choices=[('INF', 'INFO'), ('WAR', 'WARNING'), ('ERR', 'ERROR'), ('INS', 'INSERT'), ('UPD', 'UPDATE'), ('DEL', 'DELETE')], max_length=5)),
                ('smCreatedBy', models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL, related_name='+', editable=False)),
                ('smOwningTeam', models.ForeignKey(blank=True, null=True, to='protoLib.TeamHierarchy', related_name='+', editable=False)),
            ],
        ),
    ]
