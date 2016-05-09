# -*- coding: utf-8 -*-

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

    #  Do Pci's
    retSt, msgReturn = doBuildRaiMeta(cBase, queryset)
    if not retSt:
        return JsonError(msgReturn)


def doBuildRaiMeta(cBase, queryset):

    for pDoc in queryset:

        idType = str(pDoc.pk)
        cBase.viewEntity = 'rai01ref.{0}.{1}'.format(pDoc.document, idType)

        try:
            cBase.model = getDjangoModel(cBase.viewEntity)
            getBasePci(cBase, False, True )
        except:
            return False, 'model not found: {0}'.format(cBase.viewEntity)

        # Get Dopcument info fields from instance definition rai01ref
        docFields, shortTitle = cBase.model.getJfields(idType)
        for lKey in docFields.keys():
            cBase.protoMeta['fields'].append(docFields[lKey])

        # DocType conf          
        docFields = list2dict(cBase.protoMeta[ 'fields' ], 'name')
        docFields['docType_id']['prpDefault'] = idType
        docFields['docType']['prpDefault'] = shortTitle
        cBase.protoMeta['gridConfig']['baseFilter'].append({'property': 'docType', 'filterStmt': '=' + idType})

        # varias           
        cBase.protoMeta['jsonField'] = "info"
        cBase.protoMeta['description'] = '{0}: {1}'.format(pDoc.document, shortTitle)

        # Update definition
        cBase.protoDef.metaDefinition = cBase.protoMeta
        cBase.protoDef.description = cBase.protoMeta['description']
        cBase.protoDef.save()

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
        defaults={'active': False, 'code': viewCode, 'smOwningTeam': cBase.userProfile.userTeam}
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
