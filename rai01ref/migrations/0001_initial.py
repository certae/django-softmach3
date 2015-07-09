# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid
from django.conf import settings
import jsonfield2.fields


class Migration(migrations.Migration):

    dependencies = [
        ('protoLib', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artefact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smNaturalCode', models.CharField(null=True, editable=False, blank=True, max_length=50)),
                ('smRegStatus', models.CharField(null=True, editable=False, blank=True, max_length=50)),
                ('smWflowStatus', models.CharField(null=True, editable=False, blank=True, max_length=50)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('code', models.CharField(max_length=200)),
                ('description', models.TextField(null=True, blank=True)),
                ('info', jsonfield2.fields.JSONField(default={})),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ArtefactCapacity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smNaturalCode', models.CharField(null=True, editable=False, blank=True, max_length=50)),
                ('smRegStatus', models.CharField(null=True, editable=False, blank=True, max_length=50)),
                ('smWflowStatus', models.CharField(null=True, editable=False, blank=True, max_length=50)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('notes', models.TextField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('artefact', models.ForeignKey(to='rai01ref.Artefact')),
            ],
        ),
        migrations.CreateModel(
            name='ArtefactComposition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smNaturalCode', models.CharField(null=True, editable=False, blank=True, max_length=50)),
                ('smRegStatus', models.CharField(null=True, editable=False, blank=True, max_length=50)),
                ('smWflowStatus', models.CharField(null=True, editable=False, blank=True, max_length=50)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('condition', models.TextField(null=True, blank=True)),
                ('notes', models.TextField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('containerArt', models.ForeignKey(to='rai01ref.Artefact', related_name='artefactcomposition_set')),
                ('inputArt', models.ForeignKey(to='rai01ref.Artefact', related_name='+')),
                ('outputArt', models.ForeignKey(to='rai01ref.Artefact', blank=True, null=True, related_name='+')),
                ('smCreatedBy', models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('smModifiedBy', models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('smOwningTeam', models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to='protoLib.TeamHierarchy')),
                ('smOwningUser', models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ArtefactRequirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smNaturalCode', models.CharField(null=True, editable=False, blank=True, max_length=50)),
                ('smRegStatus', models.CharField(null=True, editable=False, blank=True, max_length=50)),
                ('smWflowStatus', models.CharField(null=True, editable=False, blank=True, max_length=50)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('notes', models.TextField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('artefact', models.ForeignKey(to='rai01ref.Artefact')),
            ],
        ),
        migrations.CreateModel(
            name='ArtefactSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smNaturalCode', models.CharField(null=True, editable=False, blank=True, max_length=50)),
                ('smRegStatus', models.CharField(null=True, editable=False, blank=True, max_length=50)),
                ('smWflowStatus', models.CharField(null=True, editable=False, blank=True, max_length=50)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('notes', models.TextField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('artefact', models.ForeignKey(to='rai01ref.Artefact', blank=True, null=True)),
                ('smCreatedBy', models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('smModifiedBy', models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('smOwningTeam', models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to='protoLib.TeamHierarchy')),
                ('smOwningUser', models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Capacity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smNaturalCode', models.CharField(null=True, editable=False, blank=True, max_length=50)),
                ('smRegStatus', models.CharField(null=True, editable=False, blank=True, max_length=50)),
                ('smWflowStatus', models.CharField(null=True, editable=False, blank=True, max_length=50)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('code', models.CharField(max_length=200)),
                ('description', models.TextField(null=True, blank=True)),
                ('info', jsonfield2.fields.JSONField(default={})),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DocAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smNaturalCode', models.CharField(null=True, editable=False, blank=True, max_length=50)),
                ('smRegStatus', models.CharField(null=True, editable=False, blank=True, max_length=50)),
                ('smWflowStatus', models.CharField(null=True, editable=False, blank=True, max_length=50)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('code', models.CharField(max_length=200)),
                ('baseType', models.CharField(choices=[('string', 'string'), ('text', 'text'), ('bool', 'bool'), ('int', 'int'), ('sequence', 'sequence'), ('decimal', 'decimal'), ('money', 'money'), ('combo', 'combo'), ('date', 'date'), ('datetime', 'datetime'), ('time', 'time')], default='string', blank=True, max_length=50, null=True)),
                ('prpLength', models.IntegerField(null=True, blank=True)),
                ('prpScale', models.IntegerField(null=True, blank=True)),
                ('vType', models.CharField(choices=[('string', 'string'), ('text', 'text'), ('bool', 'bool'), ('int', 'int'), ('sequence', 'sequence'), ('decimal', 'decimal'), ('money', 'money'), ('combo', 'combo'), ('date', 'date'), ('datetime', 'datetime'), ('time', 'time')], default='string', blank=True, max_length=50, null=True)),
                ('prpDefault', models.CharField(null=True, blank=True, max_length=50)),
                ('prpChoices', models.TextField(null=True, blank=True)),
                ('isRequired', models.BooleanField(default=False)),
                ('isSensitive', models.BooleanField(default=False)),
                ('crudType', models.CharField(choices=[('storeOnly', 'No se presentan nunca (los id, jsonTypes, etc )'), ('readOnly', 'No se guarda nunca (usado por reglas de gestion)'), ('insertOnly', 'No se actualiza (un campo absorbido al momento de la creacion, ej:direccion de envio'), ('updateOnly', 'Al insertar nulo o VrDefault, (estado inicial fijo)')], blank=True, max_length=20, null=True)),
                ('description', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DocType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smNaturalCode', models.CharField(null=True, editable=False, blank=True, max_length=50)),
                ('smRegStatus', models.CharField(null=True, editable=False, blank=True, max_length=50)),
                ('smWflowStatus', models.CharField(null=True, editable=False, blank=True, max_length=50)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('document', models.CharField(choices=[('ARTEFACT', 'ARTEFACT'), ('CAPACITY', 'CAPACITY'), ('REQUIREMENT', 'REQUIREMENT')], max_length=11)),
                ('dtype', models.CharField(max_length=200)),
                ('category', models.CharField(null=True, blank=True, max_length=50)),
                ('notes', models.TextField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('smCreatedBy', models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('smModifiedBy', models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('smOwningTeam', models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to='protoLib.TeamHierarchy')),
                ('smOwningUser', models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smNaturalCode', models.CharField(null=True, editable=False, blank=True, max_length=50)),
                ('smRegStatus', models.CharField(null=True, editable=False, blank=True, max_length=50)),
                ('smWflowStatus', models.CharField(null=True, editable=False, blank=True, max_length=50)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('code', models.CharField(max_length=200)),
                ('description', models.TextField(null=True, blank=True)),
                ('smCreatedBy', models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('smModifiedBy', models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('smOwningTeam', models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to='protoLib.TeamHierarchy')),
                ('smOwningUser', models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectArtefact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smNaturalCode', models.CharField(null=True, editable=False, blank=True, max_length=50)),
                ('smRegStatus', models.CharField(null=True, editable=False, blank=True, max_length=50)),
                ('smWflowStatus', models.CharField(null=True, editable=False, blank=True, max_length=50)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('notes', models.TextField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('artefact', models.ForeignKey(to='rai01ref.Artefact')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectCapacity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smNaturalCode', models.CharField(null=True, editable=False, blank=True, max_length=50)),
                ('smRegStatus', models.CharField(null=True, editable=False, blank=True, max_length=50)),
                ('smWflowStatus', models.CharField(null=True, editable=False, blank=True, max_length=50)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('notes', models.TextField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('capacity', models.ForeignKey(to='rai01ref.Capacity')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectRequirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smNaturalCode', models.CharField(null=True, editable=False, blank=True, max_length=50)),
                ('smRegStatus', models.CharField(null=True, editable=False, blank=True, max_length=50)),
                ('smWflowStatus', models.CharField(null=True, editable=False, blank=True, max_length=50)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('notes', models.TextField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Projet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smNaturalCode', models.CharField(null=True, editable=False, blank=True, max_length=50)),
                ('smRegStatus', models.CharField(null=True, editable=False, blank=True, max_length=50)),
                ('smWflowStatus', models.CharField(null=True, editable=False, blank=True, max_length=50)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('code', models.CharField(max_length=200)),
                ('notes', models.TextField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('domain', models.ForeignKey(to='rai01ref.Domain')),
                ('smCreatedBy', models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('smModifiedBy', models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('smOwningTeam', models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to='protoLib.TeamHierarchy')),
                ('smOwningUser', models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smNaturalCode', models.CharField(null=True, editable=False, blank=True, max_length=50)),
                ('smRegStatus', models.CharField(null=True, editable=False, blank=True, max_length=50)),
                ('smWflowStatus', models.CharField(null=True, editable=False, blank=True, max_length=50)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('code', models.CharField(max_length=200)),
                ('description', models.TextField(null=True, blank=True)),
                ('info', jsonfield2.fields.JSONField(default={})),
                ('docType', models.ForeignKey(to='rai01ref.DocType', blank=True, null=True, related_name='+')),
                ('domain', models.ForeignKey(to='rai01ref.Domain', blank=True, null=True, related_name='+')),
                ('refRequirement', models.ForeignKey(to='rai01ref.Requirement', blank=True, null=True, related_name='+')),
                ('smCreatedBy', models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('smModifiedBy', models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('smOwningTeam', models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to='protoLib.TeamHierarchy')),
                ('smOwningUser', models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smNaturalCode', models.CharField(null=True, editable=False, blank=True, max_length=50)),
                ('smRegStatus', models.CharField(null=True, editable=False, blank=True, max_length=50)),
                ('smWflowStatus', models.CharField(null=True, editable=False, blank=True, max_length=50)),
                ('smCreatedOn', models.DateTimeField(null=True, auto_now_add=True)),
                ('smModifiedOn', models.DateTimeField(null=True, auto_now=True)),
                ('smUUID', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('code', models.CharField(max_length=200)),
                ('reference', models.CharField(null=True, blank=True, max_length=200)),
                ('notes', models.TextField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('smCreatedBy', models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('smModifiedBy', models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('smOwningTeam', models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to='protoLib.TeamHierarchy')),
                ('smOwningUser', models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='projectrequirement',
            name='projet',
            field=models.ForeignKey(to='rai01ref.Projet'),
        ),
        migrations.AddField(
            model_name='projectrequirement',
            name='requirement',
            field=models.ForeignKey(to='rai01ref.Requirement'),
        ),
        migrations.AddField(
            model_name='projectrequirement',
            name='smCreatedBy',
            field=models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='projectrequirement',
            name='smModifiedBy',
            field=models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='projectrequirement',
            name='smOwningTeam',
            field=models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to='protoLib.TeamHierarchy'),
        ),
        migrations.AddField(
            model_name='projectrequirement',
            name='smOwningUser',
            field=models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='projectcapacity',
            name='projet',
            field=models.ForeignKey(to='rai01ref.Projet'),
        ),
        migrations.AddField(
            model_name='projectcapacity',
            name='smCreatedBy',
            field=models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='projectcapacity',
            name='smModifiedBy',
            field=models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='projectcapacity',
            name='smOwningTeam',
            field=models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to='protoLib.TeamHierarchy'),
        ),
        migrations.AddField(
            model_name='projectcapacity',
            name='smOwningUser',
            field=models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='projectartefact',
            name='projet',
            field=models.ForeignKey(to='rai01ref.Projet'),
        ),
        migrations.AddField(
            model_name='projectartefact',
            name='smCreatedBy',
            field=models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='projectartefact',
            name='smModifiedBy',
            field=models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='projectartefact',
            name='smOwningTeam',
            field=models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to='protoLib.TeamHierarchy'),
        ),
        migrations.AddField(
            model_name='projectartefact',
            name='smOwningUser',
            field=models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='docattribute',
            name='docType',
            field=models.ForeignKey(to='rai01ref.DocType', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='docattribute',
            name='smCreatedBy',
            field=models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='docattribute',
            name='smModifiedBy',
            field=models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='docattribute',
            name='smOwningTeam',
            field=models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to='protoLib.TeamHierarchy'),
        ),
        migrations.AddField(
            model_name='docattribute',
            name='smOwningUser',
            field=models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='capacity',
            name='docType',
            field=models.ForeignKey(to='rai01ref.DocType', blank=True, null=True, related_name='+'),
        ),
        migrations.AddField(
            model_name='capacity',
            name='domain',
            field=models.ForeignKey(to='rai01ref.Domain', blank=True, null=True, related_name='+'),
        ),
        migrations.AddField(
            model_name='capacity',
            name='refCapacity',
            field=models.ForeignKey(to='rai01ref.Capacity', blank=True, null=True, related_name='+'),
        ),
        migrations.AddField(
            model_name='capacity',
            name='smCreatedBy',
            field=models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='capacity',
            name='smModifiedBy',
            field=models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='capacity',
            name='smOwningTeam',
            field=models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to='protoLib.TeamHierarchy'),
        ),
        migrations.AddField(
            model_name='capacity',
            name='smOwningUser',
            field=models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='artefactsource',
            name='source',
            field=models.ForeignKey(to='rai01ref.Source', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='artefactrequirement',
            name='requirement',
            field=models.ForeignKey(to='rai01ref.Requirement'),
        ),
        migrations.AddField(
            model_name='artefactrequirement',
            name='smCreatedBy',
            field=models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='artefactrequirement',
            name='smModifiedBy',
            field=models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='artefactrequirement',
            name='smOwningTeam',
            field=models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to='protoLib.TeamHierarchy'),
        ),
        migrations.AddField(
            model_name='artefactrequirement',
            name='smOwningUser',
            field=models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='artefactcapacity',
            name='capacity',
            field=models.ForeignKey(to='rai01ref.Capacity'),
        ),
        migrations.AddField(
            model_name='artefactcapacity',
            name='smCreatedBy',
            field=models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='artefactcapacity',
            name='smModifiedBy',
            field=models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='artefactcapacity',
            name='smOwningTeam',
            field=models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to='protoLib.TeamHierarchy'),
        ),
        migrations.AddField(
            model_name='artefactcapacity',
            name='smOwningUser',
            field=models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='artefact',
            name='docType',
            field=models.ForeignKey(to='rai01ref.DocType', blank=True, null=True, related_name='+'),
        ),
        migrations.AddField(
            model_name='artefact',
            name='domain',
            field=models.ForeignKey(to='rai01ref.Domain', blank=True, null=True, related_name='+'),
        ),
        migrations.AddField(
            model_name='artefact',
            name='refArtefact',
            field=models.ForeignKey(to='rai01ref.Artefact', blank=True, null=True, related_name='+'),
        ),
        migrations.AddField(
            model_name='artefact',
            name='smCreatedBy',
            field=models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='artefact',
            name='smModifiedBy',
            field=models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='artefact',
            name='smOwningTeam',
            field=models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to='protoLib.TeamHierarchy'),
        ),
        migrations.AddField(
            model_name='artefact',
            name='smOwningUser',
            field=models.ForeignKey(editable=False, blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='source',
            unique_together=set([('code',)]),
        ),
        migrations.AlterUniqueTogether(
            name='requirement',
            unique_together=set([('docType', 'code')]),
        ),
        migrations.AlterUniqueTogether(
            name='projet',
            unique_together=set([('domain', 'code')]),
        ),
        migrations.AlterUniqueTogether(
            name='projectrequirement',
            unique_together=set([('projet', 'requirement')]),
        ),
        migrations.AlterUniqueTogether(
            name='projectcapacity',
            unique_together=set([('projet', 'capacity')]),
        ),
        migrations.AlterUniqueTogether(
            name='projectartefact',
            unique_together=set([('artefact', 'projet')]),
        ),
        migrations.AlterUniqueTogether(
            name='domain',
            unique_together=set([('code',)]),
        ),
        migrations.AlterUniqueTogether(
            name='doctype',
            unique_together=set([('document', 'dtype')]),
        ),
        migrations.AlterUniqueTogether(
            name='docattribute',
            unique_together=set([('docType', 'code')]),
        ),
        migrations.AlterUniqueTogether(
            name='capacity',
            unique_together=set([('docType', 'code')]),
        ),
        migrations.AlterUniqueTogether(
            name='artefactsource',
            unique_together=set([('source', 'artefact')]),
        ),
        migrations.AlterUniqueTogether(
            name='artefactrequirement',
            unique_together=set([('artefact', 'requirement')]),
        ),
        migrations.AlterUniqueTogether(
            name='artefactcapacity',
            unique_together=set([('artefact', 'capacity')]),
        ),
        migrations.AlterUniqueTogether(
            name='artefact',
            unique_together=set([('docType', 'code')]),
        ),
    ]
