
# -*- coding: utf-8 -*-

from protoLib.models.smbase import TeamHierarchy
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from protoLib.tests.dataSetup import createAuthExt
from protoLib.tests.dataImporter import BasicImportHelper

importer = BasicImportHelper()

def createContext():

    createAuthExt()

    # Processing model: UserContext

    from protoLib.models.protoContext import UserContext

    protoLib_usercontext_1 = UserContext()
    protoLib_usercontext_1.smNaturalCode = 'model project_id'
    protoLib_usercontext_1.smOwningUser =  importer.locate_object(User, "id", User, "id", 1) 
    protoLib_usercontext_1.smOwningTeam = TeamHierarchy.objects.get( id=1 )
    protoLib_usercontext_1.modelCType = ContentType.objects.get(app_label="prototype", model="model")
    protoLib_usercontext_1.propName = 'project_id'
    protoLib_usercontext_1.propValue = '1'
    protoLib_usercontext_1.isDefault = True
    protoLib_usercontext_1.isFilter = False
    protoLib_usercontext_1 = importer.save_or_locate(protoLib_usercontext_1)


    protoLib_usercontext_3 = UserContext()
    protoLib_usercontext_3.smNaturalCode = 'entity model__project_id'
    protoLib_usercontext_3.smOwningUser =  importer.locate_object(User, "id", User, "id", 1) 
    protoLib_usercontext_3.smOwningTeam = TeamHierarchy.objects.get( id=1 )

    protoLib_usercontext_3.modelCType = ContentType.objects.get(app_label="prototype", model="entity")
    protoLib_usercontext_3.propName = 'model__project_id'
    protoLib_usercontext_3.propValue = ''
    protoLib_usercontext_3.isDefault = True
    protoLib_usercontext_3.isFilter = False
    protoLib_usercontext_3 = importer.save_or_locate(protoLib_usercontext_3)


    from protoExt.models import ViewDefinition

    protoExt_viewdefinition_1 = ViewDefinition()
    protoExt_viewdefinition_1.code = 'prototype.Diagram'
    protoExt_viewdefinition_1.description = 'Diagram'
    protoExt_viewdefinition_1.active = True
    protoExt_viewdefinition_1.overWrite = False
    protoExt_viewdefinition_1.metaDefinition = {'formConfig': {'items': [{'fsLayout': '2col', 'items': [{'name': 'project', '__ptType': 'formField'}, {'name': 'code', '__ptType': 'formField'}], '__ptType': 'fieldset'}, {'fsLayout': '2col', 'items': [{'name': 'showFKey', '__ptType': 'formField'}, {'name': 'showPrpType', '__ptType': 'formField'}, {'name': 'showBorder', '__ptType': 'formField'}], '__ptType': 'fieldset'}, {'fsLayout': '2col', 'items': [{'name': 'title', '__ptType': 'formField'}, {'name': 'prefix', '__ptType': 'formField'}, {'name': 'grphMode', '__ptType': 'formField'}, {'name': 'graphForm', '__ptType': 'formField'}, {'name': 'graphLevel', '__ptType': 'formField'}], '__ptType': 'fieldset'}, {'fsLayout': '1col', 'items': [{'name': 'notes', '__ptType': 'formField'}, {'name': 'description', '__ptType': 'formField'}], '__ptType': 'fieldset'}, {'title': 'Admin', 'collapsible': True, '__ptType': 'fieldset', 'collapsed': True, 'fsLayout': '2col', 'items': [{'name': 'smCreatedOn', '__ptType': 'formField'}, {'name': 'smOwningUser', '__ptType': 'formField'}, {'name': 'smModifiedOn', '__ptType': 'formField'}, {'name': 'smNaturalCode', '__ptType': 'formField'}, {'name': 'smRegStatus', '__ptType': 'formField'}, {'name': 'smOwningTeam', '__ptType': 'formField'}, {'name': 'smUUID', '__ptType': 'formField'}, {'name': 'smCreatedBy', '__ptType': 'formField'}, {'name': 'smModifiedBy', '__ptType': 'formField'}, {'name': 'smWflowStatus', '__ptType': 'formField'}]}]}, 'gridConfig': {'baseFilter': [], 'searchFields': ['smNaturalCode', 'smRegStatus', 'smWflowStatus', 'smInfo', 'code', 'description', 'notes', 'title', 'prefix'], 'filterSetABC': '', 'initialSort': [], 'sortFields': ['smNaturalCode', 'smRegStatus', 'smWflowStatus', 'smInfo', 'code', 'description', 'notes', 'title', 'prefix'], 'readOnlyFields': [], 'initialFilter': [], 'listDisplay': ['__str__'], 'hideRowNumbers': False, 'hiddenFields': ['id']}, 'metaVersion': '130310', 'description': 'Diagram', 'gridSets': {}, 'fields': [{'sortable': True, 'name': 'smCreatedOn', 'header': 'smCreatedOn', 'readOnly': True, 'searchable': True, 'type': 'datetime'}, {'sortable': True, 'name': 'smOwningUser', 'header': 'smOwningUser', 'readOnly': True, 'searchable': True, 'type': 'foreigntext'}, {'sortable': True, 'name': 'showFKey', 'header': 'showFKey', 'searchable': True, 'type': 'bool'}, {'sortable': True, 'name': 'smModifiedOn', 'header': 'smModifiedOn', 'readOnly': True, 'searchable': True, 'type': 'datetime'}, {'sortable': False, 'name': 'id', 'header': 'ID', 'required': False, 'readOnly': True, 'searchable': False, 'type': 'autofield'}, {'sortable': True, 'name': 'notes', 'header': 'notes', 'searchable': True, 'type': 'text', 'vType': 'plainText'}, {'sortable': True, 'name': 'title', 'header': 'title', 'searchable': True, 'type': 'string'}, {'sortable': True, 'name': 'smNaturalCode', 'header': 'smNaturalCode', 'readOnly': True, 'searchable': True, 'type': 'string'}, {'sortable': True, 'name': 'showPrpType', 'header': 'showPrpType', 'searchable': True, 'type': 'bool'}, {'sortable': True, 'name': 'prefix', 'header': 'prefix', 'searchable': True, 'type': 'string'}, {'sortable': True, 'name': 'showBorder', 'header': 'showBorder', 'searchable': True, 'type': 'bool'}, {'sortable': True, 'name': 'smRegStatus', 'header': 'smRegStatus', 'readOnly': True, 'searchable': True, 'type': 'string'}, {'sortable': False, 'name': 'smInfo', 'header': 'smInfo', 'required': True, 'searchable': True, 'readOnly': True, 'type': 'text', 'crudType': 'storeOnly'}, {'sortable': True, 'name': 'grphMode', 'header': 'grphMode', 'searchable': True, 'type': 'int', 'prpDefault': 0}, {'sortable': True, 'name': 'project', 'header': 'project', 'required': True, 'searchable': False, 'fkId': 'project_id', 'zoomModel': 'prototype.Project', 'type': 'foreigntext'}, {'sortable': True, 'name': 'smOwningTeam', 'header': 'smOwningTeam', 'readOnly': True, 'searchable': True, 'type': 'foreigntext'}, {'sortable': True, 'name': '__str__', 'flex': 1, 'header': 'Diagram', 'readOnly': True, 'fkId': 'id', 'zoomModel': 'prototype.Diagram', 'type': 'string', 'cellLink': True}, {'name': 'project_id', 'type': 'foreignid', 'hidden': True, 'readOnly': True, 'fkField': 'project'}, {'sortable': True, 'name': 'smUUID', 'header': 'smUUID', 'required': True, 'readOnly': True, 'searchable': True, 'type': 'string'}, {'sortable': True, 'name': 'smCreatedBy', 'header': 'smCreatedBy', 'readOnly': True, 'searchable': True, 'type': 'foreigntext'}, {'sortable': True, 'name': 'smModifiedBy', 'header': 'smModifiedBy', 'readOnly': True, 'searchable': True, 'type': 'foreigntext'}, {'sortable': True, 'name': 'code', 'header': 'code', 'required': True, 'searchable': True, 'type': 'string'}, {'sortable': True, 'name': 'graphForm', 'header': 'graphForm', 'searchable': True, 'type': 'int', 'prpDefault': 0}, {'sortable': True, 'name': 'smWflowStatus', 'header': 'smWflowStatus', 'readOnly': True, 'searchable': True, 'type': 'string'}, {'sortable': True, 'name': 'graphLevel', 'header': 'graphLevel', 'searchable': True, 'type': 'int', 'prpDefault': 0}, {'sortable': True, 'name': 'description', 'header': 'description', 'searchable': True, 'type': 'text', 'vType': 'plainText'}], 'idProperty': 'id', 'viewCode': 'prototype.Diagram', 'actions': [{'name': 'doDiagram', 'selectionMode': 'multiple'}], 'shortTitle': 'Diagram', 'viewEntity': 'prototype.Diagram', 'viewIcon': 'icon-1', 'detailsConfig': [{'detailName': 'diagramentity.diagram', 'conceptDetail': 'prototype.DiagramEntity', 'detailField': 'diagram__pk', 'masterField': 'pk', 'menuText': 'Diagramentity.diagram'}], 'exclude': []}
    protoExt_viewdefinition_1 = importer.save_or_locate(protoExt_viewdefinition_1)

