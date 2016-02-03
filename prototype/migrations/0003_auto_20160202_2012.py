# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prototype', '0002_auto_20160201_2020'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='diagram',
            unique_together=set([('project', 'code', 'smOwningTeam', 'smVersion')]),
        ),
        migrations.AlterUniqueTogether(
            name='diagramentity',
            unique_together=set([('diagram', 'entity', 'smOwningTeam', 'smVersion')]),
        ),
        migrations.AlterUniqueTogether(
            name='entity',
            unique_together=set([('model', 'code', 'smOwningTeam', 'smVersion')]),
        ),
        migrations.AlterUniqueTogether(
            name='model',
            unique_together=set([('project', 'code', 'smOwningTeam', 'smVersion')]),
        ),
        migrations.AlterUniqueTogether(
            name='project',
            unique_together=set([('code', 'smOwningTeam', 'smVersion')]),
        ),
        migrations.AlterUniqueTogether(
            name='property',
            unique_together=set([('entity', 'code', 'smOwningTeam', 'smVersion')]),
        ),
        migrations.AlterUniqueTogether(
            name='propertyequivalence',
            unique_together=set([('sourceProperty', 'targetProperty', 'smOwningTeam', 'smVersion')]),
        ),
        migrations.AlterUniqueTogether(
            name='prototype',
            unique_together=set([('entity', 'code', 'smOwningTeam', 'smVersion')]),
        ),
    ]
