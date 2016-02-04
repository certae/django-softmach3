# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('protoLib', '0004_auto_20160202_1451'),
    ]

    operations = [
        migrations.CreateModel(
            name='VersionUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('active', models.BooleanField(default=False)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='+')),
                ('version', models.ForeignKey(null=True, blank=True, to='protoLib.VersionTitle')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='versionuser',
            unique_together=set([('version', 'user')]),
        ),
    ]
