# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prototype', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='crudType',
            field=models.CharField(choices=[('editable', 'Default behavior'), ('readOnly', 'Never saved (rules, functions, linked, ...)'), ('insertOnly', 'Never updated (absorbed at the time of the creation field, eg shipping address'), ('updateOnly', 'Adding null or VrDefault, (fixed initial state)'), ('storeOnly', 'Never show on screen (id, json Types, etc)'), ('screenOnly', 'Calculated on the frontend')], max_length=20, blank=True, null=True),
        ),
    ]
