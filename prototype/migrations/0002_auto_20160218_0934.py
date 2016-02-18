# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('protoLib', '0006_auto_20160218_0934'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('prototype', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProtoVersionHeader',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('smNaturalCode', models.CharField(blank=True, null=True, editable=False, max_length=50)),
                ('smRegStatus', models.CharField(blank=True, null=True, editable=False, max_length=50)),
                ('smWflowStatus', models.CharField(blank=True, null=True, editable=False, max_length=50)),
                ('smCreatedOn', models.DateTimeField(auto_now_add=True, null=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('exclude', models.BooleanField(default=False)),
                ('modelCType', models.ForeignKey(to='contenttypes.ContentType')),
                ('smCreatedBy', models.ForeignKey(blank=True, null=True, related_name='+', editable=False, to=settings.AUTH_USER_MODEL)),
                ('smModifiedBy', models.ForeignKey(blank=True, null=True, related_name='+', editable=False, to=settings.AUTH_USER_MODEL)),
                ('smOwningTeam', models.ForeignKey(blank=True, null=True, related_name='+', editable=False, to='protoLib.TeamHierarchy')),
                ('smOwningUser', models.ForeignKey(blank=True, null=True, related_name='+', editable=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProtoVersionTitle',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('smNaturalCode', models.CharField(blank=True, null=True, editable=False, max_length=50)),
                ('smRegStatus', models.CharField(blank=True, null=True, editable=False, max_length=50)),
                ('smWflowStatus', models.CharField(blank=True, null=True, editable=False, max_length=50)),
                ('smCreatedOn', models.DateTimeField(auto_now_add=True, null=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('versionCode', models.CharField(blank=True, null=True, default='0', max_length=50)),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descriptions')),
                ('active', models.BooleanField(default=True)),
                ('smCreatedBy', models.ForeignKey(blank=True, null=True, related_name='+', editable=False, to=settings.AUTH_USER_MODEL)),
                ('smModifiedBy', models.ForeignKey(blank=True, null=True, related_name='+', editable=False, to=settings.AUTH_USER_MODEL)),
                ('smOwningTeam', models.ForeignKey(blank=True, null=True, related_name='+', editable=False, to='protoLib.TeamHierarchy')),
                ('smOwningUser', models.ForeignKey(blank=True, null=True, related_name='+', editable=False, to=settings.AUTH_USER_MODEL)),
                ('versionBase', models.ForeignKey(blank=True, null=True, to='prototype.ProtoVersionTitle')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='diagram',
            name='smVersion',
            field=models.ForeignKey(blank=True, null=True, to='prototype.ProtoVersionTitle'),
        ),
        migrations.AlterField(
            model_name='diagramentity',
            name='smVersion',
            field=models.ForeignKey(blank=True, null=True, to='prototype.ProtoVersionTitle'),
        ),
        migrations.AlterField(
            model_name='entity',
            name='smVersion',
            field=models.ForeignKey(blank=True, null=True, to='prototype.ProtoVersionTitle'),
        ),
        migrations.AlterField(
            model_name='model',
            name='smVersion',
            field=models.ForeignKey(blank=True, null=True, to='prototype.ProtoVersionTitle'),
        ),
        migrations.AlterField(
            model_name='project',
            name='smVersion',
            field=models.ForeignKey(blank=True, null=True, to='prototype.ProtoVersionTitle'),
        ),
        migrations.AlterField(
            model_name='property',
            name='smVersion',
            field=models.ForeignKey(blank=True, null=True, to='prototype.ProtoVersionTitle'),
        ),
        migrations.AlterField(
            model_name='propertyequivalence',
            name='smVersion',
            field=models.ForeignKey(blank=True, null=True, to='prototype.ProtoVersionTitle'),
        ),
        migrations.AlterField(
            model_name='prototable',
            name='smVersion',
            field=models.ForeignKey(blank=True, null=True, to='prototype.ProtoVersionTitle'),
        ),
        migrations.AlterField(
            model_name='prototype',
            name='smVersion',
            field=models.ForeignKey(blank=True, null=True, to='prototype.ProtoVersionTitle'),
        ),
    ]
