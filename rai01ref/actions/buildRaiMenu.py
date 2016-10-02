# -*- coding: utf-8 -*-
__updated__ = "2016-05-10"

import json
from protoExt.models import CustomDefinition, ViewDefinition
from protoExt.views import validateRequest
from protoExt.utils.utilsWeb import JsonError
from protoExt.views.protoGetPci import getBasePci
from protoLib.getStuff import getDjangoModel
from protoExt.utils.utilsBase import list2dict


DOCUMENTS = ('Artefact', 'Capacity', 'Requirement')


def doBuildRaiConfig(request, queryset):
    """ 
    Build Rai Config 
    """

    cBase, msgReturn = validateRequest(request)
    if msgReturn:
        return msgReturn

    #  Do Menu
    retSt, msgReturn = doBuildRaiMenu(cBase, queryset)
    if not retSt:
        return JsonError(msgReturn)

    #  Do single documents Pci's
    retSt, msgReturn = doSingleDocsMeta(cBase, queryset)
    if not retSt:
        return JsonError(msgReturn)

    #  Do tree documents Pci's
    retSt, msgReturn = doTreeDocsMeta(cBase)
    if not retSt:
        return JsonError(msgReturn)

    return {'success': True, 'message': 'Ok'}


def doFinalDetails(cBase, document, docFields):

    # Details config
    doDetailsConf(cBase, document)

    # Form config
    doFormConf(cBase, document, docFields)

    # Update definition
    cBase.protoDef.metaDefinition = cBase.protoMeta
    cBase.protoDef.description = cBase.protoMeta['description']
    cBase.protoDef.save()


def doTreeDocsMeta(cBase):

    viewIcon = 'icon-tree'
    for document in DOCUMENTS:
        cBase.viewCode = 'rai01ref.{0}.tree'.format(document)
        cBase.viewEntity = 'rai01ref.{0}'.format(document)

        try:
            cBase.model = getDjangoModel(cBase.viewCode)
            getBasePci(cBase, False, True)
        except:
            return False, 'model not found: {0}'.format(cBase.viewCode)

        # DocType conf
        docFields = list2dict(cBase.protoMeta['fields'], 'name')
        docFields['docType']['zoomFilter'] = "document, ={0}".format( document )

        # Get Dopcument info fields from document definition rai01ref
        docFields = cBase.model.getJfields(None, document)[0]
        for lKey in docFields.keys():
            cBase.protoMeta['fields'].append(docFields[lKey])

        # Add IconField
        cBase.protoMeta['fields'].append({"name": "iconCls", "crudType": "readOnly", })

        # Tree Config and Form selector
        cBase.protoMeta.update({
            "pciStyle": "tree",
            "treeRefField": "ref{0}".format(document),
            "formSelector": "docType_id",
            "jsonField": "info",
            "description": 'Tree {0}'.format(document),
            "viewIcon": viewIcon,
        })

        # do User interface and save
        doFinalDetails(cBase, document, {})

    return True, ''


def doSingleDocsMeta(cBase, queryset):

    for pDoc in queryset:

        idType = str(pDoc.pk)
        cBase.viewCode = 'rai01ref.{0}.{1}'.format(pDoc.document, idType)
        cBase.viewEntity = 'rai01ref.{0}'.format(pDoc.document)
        shortTitle = pDoc.dtype

        try:
            cBase.model = getDjangoModel(cBase.viewCode)
            getBasePci(cBase, False, True)
        except:
            return False, 'model not found: {0}'.format(cBase.viewCode)

        # DocType conf
        docFields = list2dict(cBase.protoMeta['fields'], 'name')
        docFields['docType_id']['prpDefault'] = idType
        docFields['docType']['prpDefault'] = shortTitle
        docFields['docType']['zoomFilter'] = "document, ={0}".format( pDoc.document )

        cBase.protoMeta['gridConfig']['baseFilter'].append({'property': 'docType', 'filterStmt': '=' + idType})

        # varias
        cBase.protoMeta['jsonField'] = "info"
        cBase.protoMeta['shortTitle'] =  shortTitle
        cBase.protoMeta['description'] = '{0}: {1}'.format(pDoc.document, shortTitle)

        # Get Dopcument info fields from instance definition rai01ref
        docFields = cBase.model.getJfields(idType)[0]
        for lKey in docFields.keys():
            cBase.protoMeta['fields'].append(docFields[lKey])

        # do User interface and save
        doFinalDetails(cBase, pDoc.document, docFields)

    return True, ''


def doBuildRaiMenu(cBase, queryset):

    #-- RAI Auto Menu ( documents and selected documents  )
    lMenu = {}
    Ix = 0

    # Trees
    viewIcon = 'icon-tree'
    for document in DOCUMENTS:
        viewCode = 'rai01ref.{0}.{1}'.format(document, 'tree')
        lMenu[viewCode] = {
            'viewCode': viewCode,
            'text': document,
            'index': Ix,
            'iconCls': viewIcon,
            'leaf': True,
        }
        Ix += 1

    # Documents config
    for document in DOCUMENTS:
        viewIcon = 'rai_{}'.format(document[:3].lower())
        lMenu[document] = {
            'text': document,
            'expanded': True,
            'index':  Ix,
            'iconCls': viewIcon,
            'leaf': False,
            'children': [],
        }
        Ix += 1

    for pDoc in queryset:
        viewCode = 'rai01ref.{0}.{1}'.format(pDoc.document, str(pDoc.pk))
        viewIcon = 'rai_{}'.format(pDoc.__str__())
        model_dict = {
            'viewCode': viewCode,
            'text': pDoc.dtype,
            'index': Ix,
            'iconCls': viewIcon,
            'leaf': True,
        }
        Ix += 1

        lMenu[pDoc.document]['children'].append(model_dict)

        # Delete previous definition
        ViewDefinition.objects.filter(code=viewCode).delete()


#-- Update Menu in customDefinition --------------------------------------
    viewCode = '__menu'
    protoDef = CustomDefinition.objects.get_or_create(
        code=viewCode, smOwningTeam=cBase.userProfile.userTeam,
        defaults={'active': False, 'code': viewCode,
                  'smOwningTeam': cBase.userProfile.userTeam}
    )[0]

    # El default solo parece funcionar al insertar en la Db
    if not protoDef.active:
        return False, 'Menu not found'

    menuData = protoDef.metaDefinition


#-- Update  Db ------------------------------------------------------
    try:
        raiMenu = menuData[0]
        if str(raiMenu['text']) == str('RAI MENU'):
            raiMenu = menuData.pop(0)
    except:
        pass

    raiMenu = {
        'text': 'RAI MENU',
        'expanded': False,
        'index':  0,
        'leaf': False,
        'children': [],
    }

    for lKey in lMenu.keys():
        raiMenu['children'].append(lMenu[lKey])

    menuData.insert(0, raiMenu)

    protoDef.metaDefinition = json.dumps(menuData)
    protoDef.save()

    return True, ''


def doDetailsConf(cBase, document):

    if document == 'Capacity':
        cBase.protoMeta["detailsConfig"] = [{
            "detailName": "artefactcapacity",
            "menuText": "Artefacts",
            "masterField": "pk",
            "detailField": "capacity__pk",
            "conceptDetail": "rai01ref.ArtefactCapacity",
        }, {
            "detailName": "projectcapacity",
            "menuText": "Projects",
            "masterField": "pk",
            "detailField": "capacity__pk",
            "conceptDetail": "rai01ref.ProjectCapacity",
        }, {
            "detailName": "copyto",
            "menuText": "Copies",
            "masterField": "pk",
            "detailField": "copyFrom_id",
            "conceptDetail": "rai01ref.Capacity",
        }]

    elif document == 'Requirement':
        cBase.protoMeta["detailsConfig"] = [{
            "menuText": "Artefacts",
            "detailName": "artefactrequirement",
            "masterField": "pk",
            "detailField": "requirement__pk",
            "conceptDetail": "rai01ref.ArtefactRequirement",
        }, {
            "menuText": "Projects",
            "detailName": "projectrequirement",
            "masterField": "pk",
            "detailField": "requirement__pk",
            "conceptDetail": "rai01ref.ProjectRequirement",
        }, {
            "menuText": "Copies",
            "detailName": "copyto",
            "masterField": "pk",
            "detailField": "copyFrom_id",
            "conceptDetail": "rai01ref.Requirement",
        }]

    elif document == 'Artefact':
        cBase.protoMeta["detailsConfig"] = [{
            "menuText": "Composition",
            "detailField": "containerArt__pk",
            "conceptDetail": "rai01ref.ArtefactComposition",
            "masterField": "pk",
            "detailName": "artefactcomposition.containerArt",
        }, {
            "menuText": "Requirements",
            "detailField": "artefact__pk",
            "conceptDetail": "rai01ref.ArtefactRequirement",
            "masterField": "pk",
            "detailName": "artefactrequirement.artefact",
        }, {
            "menuText": "Capacities",
            "detailField": "artefact__pk",
            "conceptDetail": "rai01ref.ArtefactCapacity",
            "masterField": "pk",
            "detailName": "artefactcapacity.artefact",
        }, {
            "menuText": "Projects",
            "detailField": "artefact__pk",
            "conceptDetail": "rai01ref.ProjectArtefact",
            "masterField": "pk",
            "detailName": "projectartefact.artefact",
        }, {
            "menuText": "Sources",
            "detailField": "artefact__pk",
            "conceptDetail": "rai01ref.ArtefactSource",
            "masterField": "pk",
            "detailName": "artefactsource.artefact",
        }, {
            "menuText": "Copies",
            "detailName": "copyto",
            "masterField": "pk",
            "detailField": "copyFrom_id",
            "conceptDetail": "rai01ref.Artefact",
        }]


def doFormConf(cBase, document, docFields):

    udfs = []

    if document == 'Artefact': 
        udfs.append({'__ptType': 'formField', "name": "capacity"})
        udfs.append({'__ptType': 'formField', "name": "requirement"})


    for lKey in docFields.keys():
        udfs.append({'__ptType': 'formField', "name": lKey})


    cBase.protoMeta["formConfig"] = {
        "items": [
            {
                '__ptType': 'fieldset',
                "fsLayout": "2col",
                "items": [
                    {'__ptType': 'formField', "name": "code"},
                    {'__ptType': 'formField', "name": "docType"},
                    {'__ptType': 'formField',
                        "name": "description", "prpLength": "1", },
                    {'__ptType': 'formField', "name": "ref{0}".format(document)},
                    {'__ptType': 'formField', "name": "copyFrom"}
                ],
            },
            {
                '__ptType': 'fieldset',
                "fsLayout": "2col",
                "items": udfs,
            },
            {
                '__ptType': 'fieldset',
                "fsLayout": "2col",
                "title": "Admin",
                "collapsible": True,
                "collapsed": True,
                "items": [
                    {'__ptType': 'formField', "name": "smOwningUser"},
                    {'__ptType': 'formField', "name": "smOwningTeam"},
                    {'__ptType': 'formField', "name": "smCreatedBy"},
                    {'__ptType': 'formField', "name": "smModifiedOn"},
                    {'__ptType': 'formField', "name": "smCreatedOn"},
                    {'__ptType': 'formField', "name": "smModifiedBy"},
                ],
            }
        ]
    }
