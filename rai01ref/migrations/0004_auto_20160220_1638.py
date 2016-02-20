# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rai01ref', '0003_auto_20160219_1707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='raiversionheader',
            name='modelCType',
        ),
        migrations.RemoveField(
            model_name='raiversionheader',
            name='smCreatedBy',
        ),
        migrations.RemoveField(
            model_name='raiversionheader',
            name='smModifiedBy',
        ),
        migrations.RemoveField(
            model_name='raiversionheader',
            name='smOwningTeam',
        ),
        migrations.RemoveField(
            model_name='raiversionheader',
            name='smOwningUser',
        ),
        migrations.RemoveField(
            model_name='projet',
            name='smVersion',
        ),
        migrations.AlterUniqueTogether(
            name='artefact',
            unique_together=set([('docType', 'code', 'smVersion')]),
        ),
        migrations.AlterUniqueTogether(
            name='artefactcapacity',
            unique_together=set([('artefact', 'capacity', 'smVersion')]),
        ),
        migrations.AlterUniqueTogether(
            name='artefactrequirement',
            unique_together=set([('artefact', 'requirement', 'smVersion')]),
        ),
        migrations.AlterUniqueTogether(
            name='artefactsource',
            unique_together=set([('source', 'artefact', 'smVersion')]),
        ),
        migrations.AlterUniqueTogether(
            name='capacity',
            unique_together=set([('docType', 'code', 'smVersion')]),
        ),
        migrations.AlterUniqueTogether(
            name='docattribute',
            unique_together=set([('docType', 'code', 'smVersion')]),
        ),
        migrations.AlterUniqueTogether(
            name='doctype',
            unique_together=set([('document', 'dtype', 'smVersion')]),
        ),
        migrations.AlterUniqueTogether(
            name='projectartefact',
            unique_together=set([('artefact', 'projet', 'smVersion')]),
        ),
        migrations.AlterUniqueTogether(
            name='projectcapacity',
            unique_together=set([('projet', 'capacity', 'smVersion')]),
        ),
        migrations.AlterUniqueTogether(
            name='projectrequirement',
            unique_together=set([('projet', 'requirement', 'smVersion')]),
        ),
        migrations.AlterUniqueTogether(
            name='requirement',
            unique_together=set([('docType', 'code', 'smVersion')]),
        ),
        migrations.AlterUniqueTogether(
            name='source',
            unique_together=set([('code', 'smVersion')]),
        ),
        migrations.DeleteModel(
            name='RaiVersionHeader',
        ),
    ]
