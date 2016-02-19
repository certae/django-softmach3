# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('protoLib', '0007_contextuser_description'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('rai01ref', '0002_auto_20160218_0934'),
    ]

    operations = [
        migrations.CreateModel(
            name='RaiVersionHeader',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('smNaturalCode', models.CharField(blank=True, editable=False, null=True, max_length=50)),
                ('smRegStatus', models.CharField(blank=True, editable=False, null=True, max_length=50)),
                ('smWflowStatus', models.CharField(blank=True, editable=False, null=True, max_length=50)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('exclude', models.BooleanField(default=False)),
                ('modelCType', models.ForeignKey(to='contenttypes.ContentType')),
                ('smCreatedBy', models.ForeignKey(blank=True, related_name='+', null=True, to=settings.AUTH_USER_MODEL, editable=False)),
                ('smModifiedBy', models.ForeignKey(blank=True, related_name='+', null=True, to=settings.AUTH_USER_MODEL, editable=False)),
                ('smOwningTeam', models.ForeignKey(blank=True, related_name='+', null=True, to='protoLib.TeamHierarchy', editable=False)),
                ('smOwningUser', models.ForeignKey(blank=True, related_name='+', null=True, to=settings.AUTH_USER_MODEL, editable=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RaiVersionTitle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('smNaturalCode', models.CharField(blank=True, editable=False, null=True, max_length=50)),
                ('smRegStatus', models.CharField(blank=True, editable=False, null=True, max_length=50)),
                ('smWflowStatus', models.CharField(blank=True, editable=False, null=True, max_length=50)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('versionCode', models.CharField(default='0', blank=True, null=True, max_length=50)),
                ('description', models.TextField(verbose_name='Descriptions', blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('smCreatedBy', models.ForeignKey(blank=True, related_name='+', null=True, to=settings.AUTH_USER_MODEL, editable=False)),
                ('smModifiedBy', models.ForeignKey(blank=True, related_name='+', null=True, to=settings.AUTH_USER_MODEL, editable=False)),
                ('smOwningTeam', models.ForeignKey(blank=True, related_name='+', null=True, to='protoLib.TeamHierarchy', editable=False)),
                ('smOwningUser', models.ForeignKey(blank=True, related_name='+', null=True, to=settings.AUTH_USER_MODEL, editable=False)),
                ('versionBase', models.ForeignKey(blank=True, null=True, to='rai01ref.RaiVersionTitle')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='artefact',
            name='smVersion',
            field=models.ForeignKey(default=1, to='rai01ref.RaiVersionTitle'),
        ),
        migrations.AddField(
            model_name='artefactcapacity',
            name='smVersion',
            field=models.ForeignKey(default=1, to='rai01ref.RaiVersionTitle'),
        ),
        migrations.AddField(
            model_name='artefactcomposition',
            name='smVersion',
            field=models.ForeignKey(default=1, to='rai01ref.RaiVersionTitle'),
        ),
        migrations.AddField(
            model_name='artefactrequirement',
            name='smVersion',
            field=models.ForeignKey(default=1, to='rai01ref.RaiVersionTitle'),
        ),
        migrations.AddField(
            model_name='artefactsource',
            name='smVersion',
            field=models.ForeignKey(default=1, to='rai01ref.RaiVersionTitle'),
        ),
        migrations.AddField(
            model_name='capacity',
            name='smVersion',
            field=models.ForeignKey(default=1, to='rai01ref.RaiVersionTitle'),
        ),
        migrations.AddField(
            model_name='docattribute',
            name='smVersion',
            field=models.ForeignKey(default=1, to='rai01ref.RaiVersionTitle'),
        ),
        migrations.AddField(
            model_name='doctype',
            name='smVersion',
            field=models.ForeignKey(default=1, to='rai01ref.RaiVersionTitle'),
        ),
        migrations.AddField(
            model_name='domain',
            name='smVersion',
            field=models.ForeignKey(default=1, to='rai01ref.RaiVersionTitle'),
        ),
        migrations.AddField(
            model_name='projectartefact',
            name='smVersion',
            field=models.ForeignKey(default=1, to='rai01ref.RaiVersionTitle'),
        ),
        migrations.AddField(
            model_name='projectcapacity',
            name='smVersion',
            field=models.ForeignKey(default=1, to='rai01ref.RaiVersionTitle'),
        ),
        migrations.AddField(
            model_name='projectrequirement',
            name='smVersion',
            field=models.ForeignKey(default=1, to='rai01ref.RaiVersionTitle'),
        ),
        migrations.AddField(
            model_name='projet',
            name='smVersion',
            field=models.ForeignKey(default=1, to='rai01ref.RaiVersionTitle'),
        ),
        migrations.AddField(
            model_name='requirement',
            name='smVersion',
            field=models.ForeignKey(default=1, to='rai01ref.RaiVersionTitle'),
        ),
        migrations.AddField(
            model_name='source',
            name='smVersion',
            field=models.ForeignKey(default=1, to='rai01ref.RaiVersionTitle'),
        ),
    ]
