# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
        ('protoLib', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserContext',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('smNaturalCode', models.CharField(max_length=50, null=True, editable=False, blank=True)),
                ('smRegStatus', models.CharField(max_length=50, null=True, editable=False, blank=True)),
                ('smWflowStatus', models.CharField(max_length=50, null=True, editable=False, blank=True)),
                ('smCreatedOn', models.DateTimeField(auto_now_add=True, null=True)),
                ('smModifiedOn', models.DateTimeField(auto_now=True, null=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('property', models.CharField(max_length=500)),
                ('propValue', models.CharField(max_length=200)),
                ('propDescription', models.TextField(null=True, blank=True)),
                ('isDefault', models.BooleanField(default=True)),
                ('isFilter', models.BooleanField(default=True)),
                ('entity', models.ForeignKey(to='contenttypes.ContentType')),
                ('smCreatedBy', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, related_name='+', editable=False, blank=True)),
                ('smModifiedBy', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, related_name='+', editable=False, blank=True)),
                ('smOwningTeam', models.ForeignKey(to='protoLib.TeamHierarchy', null=True, related_name='+', editable=False, blank=True)),
                ('smOwningUser', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, related_name='+', editable=False, blank=True)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='usercontext',
            unique_together=set([('entity', 'property', 'smOwningUser')]),
        ),
    ]
