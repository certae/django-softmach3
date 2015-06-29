# -*- coding: utf-8 -*-

from django.http import HttpResponse
# from django.contrib.admin.utils import  get_fields_from_path
from django.utils.encoding import smart_str

from protoExt.utils.utilsBase import JSONEncoder, getReadableError
from protoExt.utils.utilsBase import verifyList, list2dict

from .protoQbe import getFieldValue, getQbeFilter 
from protoLib.getStuff import  getModelPermission, getRowById


from protoLib.getStuff import getDjangoModel
from protoExt.utils.utilsWeb import JsonError , doReturn
from . import validateRequest 

import json
import traceback
from protoExt.views.getStuff import setContextFilter
from protoExt.views.protoGetPci import getGenericPci
from django.contrib.admin.sites import  site

def protoExecuteAction(request):
    """ Ejecuta una opcion
    """


    cBase, message = validateRequest( request )
    if message: return None, message  

    cBase.actionName = request.POST.get('actionName', '')

    cBase.selectedKeys = request.POST.get('selectedKeys', '')
    cBase.selectedKeys = json.loads(cBase.selectedKeys)

    cBase.parameters = request.POST.get('parameters', [])
    cBase.parameters = json.loads(cBase.parameters)

    cBase.actionDef = request.POST.get('actionDef', {})
    cBase.actionDef = json.loads(cBase.actionDef)

    # hace el QSet de los registros seleccionados
    if cBase.actionDef.get('selectionMode', '') == 'optional':
        if cBase.selectedKeys.__len__() > 1:
            return JsonError( 'too many records selected')
    elif cBase.actionDef.get('selectionMode', '') != 'none' and cBase.selectedKeys.__len__() == 0:
        return JsonError( 'No record selected')


    # Obtiene el modelo
    try:
        cBase.model = getDjangoModel(cBase.viewEntity)
        cBase.modelAdmin = site._registry.get(cBase.model)
    except :
        return JsonError( 'Model notFound')


    # details
    if actionDef.get('selectionMode', '') == 'details':
        detKeys = request.POST.get('detKeys', {} )
        detKeys = json.loads(detKeys)

        return doAdminDetailAction(model, selectedKeys, detKeys, parameters, actionDef, modelAdmin )

#     elif actionDef.get('actionType', '') == 'wflow':
#         return doWfAction(model, selectedKeys, parameters, actionDef, viewEntity, request.user)

    elif hasattr(modelAdmin, 'actions'):
        return doAdminAction (model, selectedKeys, parameters, actionDef, modelAdmin)

    else:
        return JsonError( 'Action notFound')




def doAdminAction(model, selectedKeys, parameters, actionDef, modelAdmin):

    try: 
        action = site.get_action( actionName )
        actionFound = True
    except: 
        action = None 
        actionFound = False        

    if not actionFound:
        for action in modelAdmin.actions:
            if action.__name__ == actionName:
                actionFound = True
                break

    if not actionFound:
        return JsonError( 'Action notFound')


    Qs = model.objects.select_related()
    Qs = Qs.filter(pk__in=selectedKeys)

    try:
        returnObj = action(modelAdmin, request, Qs , parameters)
        return doReturn (returnObj)

    except Exception as e:
        return JsonError( str(e) )



def doAdminDetailAction(model, selectedKeys, detKeys, parameters, actionDef, modelAdmin ):

    for action in modelAdmin.actions:
        if action.__name__ == actionName:
            break

    if not action:
        return JsonError( 'Action notFound')

    try:
        returnObj = action( modelAdmin, request, selectedKeys, detKeys, parameters )
        return doReturn(returnObj)

    except Exception as e:
        return JsonError( str(e) )


#TODO: Wf from .prototypeWfActions import doWfAction

#   ----------------------------------------
