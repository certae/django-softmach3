# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('protoLib', '0003_versiontitle'),
    ]

    operations = [
        migrations.CreateModel(
            name='VersionHeaders',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('modelCType', models.ForeignKey(to='contenttypes.ContentType')),
            ],
        ),
        migrations.RemoveField(
            model_name='versiontitle',
            name='smRegStatus',
        ),
        migrations.AddField(
            model_name='versiontitle',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='versiontitle',
            name='versionBase',
            field=models.ForeignKey(blank=True, null=True, to='protoLib.VersionTitle'),
        ),
        migrations.AlterField(
            model_name='versiontitle',
            name='versionCode',
            field=models.CharField(default='0', blank=True, null=True, max_length=50),
        ),
    ]
