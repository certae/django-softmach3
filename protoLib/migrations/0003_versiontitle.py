# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('protoLib', '0002_usercontext_smversion'),
    ]

    operations = [
        migrations.CreateModel(
            name='VersionTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('versionCode', models.CharField(editable=False, null=True, max_length=50, default='0', blank=True)),
                ('versionBase', models.CharField(editable=False, null=True, max_length=50, default='0', blank=True)),
                ('description', models.TextField(verbose_name='Descriptions', null=True, blank=True)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smRegStatus', models.CharField(editable=False, max_length=50, null=True, blank=True)),
                ('smCreatedBy', models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL, null=True, blank=True, related_name='+')),
                ('smModifiedBy', models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL, null=True, blank=True, related_name='+')),
            ],
        ),
    ]
