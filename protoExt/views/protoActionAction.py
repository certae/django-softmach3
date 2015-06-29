# -*- coding: utf-8 -*-



from protoLib.getStuff import getDjangoModel
from protoExt.utils.utilsWeb import JsonError , doReturn
from . import validateRequest 

import json
import traceback
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
    if cBase.actionDef.get('selectionMode', '') == 'details':
        cBase.detKeys = request.POST.get('detKeys', {} )
        cBase.detKeys = json.loads(cBase.detKeys)

        return doAdminDetailAction( request, cBase  )

#     elif cBase.actionDef.get('actionType', '') == 'wflow':
#         return doWfAction(cBase.model, cBase.selectedKeys, cBase.parameters, cBase.actionDef, cBase.viewEntity, request.user)

    elif hasattr(cBase.modelAdmin, 'actions'):
        return doAdminAction (request, cBase )

    else:
        return JsonError( 'Action notFound')




def doAdminAction( request, cBase ):

    try: 
        action = site.get_action( cBase.actionName )
        actionFound = True
    except: 
        action = None 
        actionFound = False        

    if not actionFound:
        for action in cBase.modelAdmin.actions:
            if action.__name__ == cBase.actionName:
                actionFound = True
                break

    if not actionFound:
        return JsonError( 'Action notFound')


    Qs = cBase.model.objects.select_related()
    Qs = Qs.filter(pk__in=cBase.selectedKeys)

    try:
        returnObj = action(cBase.modelAdmin, request, Qs , cBase.parameters)
        return doReturn (returnObj)

    except Exception as e:
        return JsonError( str(e) )



def doAdminDetailAction( request, cBase  ):

    for action in cBase.modelAdmin.actions:
        if action.__name__ == cBase.actionName:
            break

    if not action:
        return JsonError( 'Action notFound')

    try:
        returnObj = action( cBase.modelAdmin, request, cBase.selectedKeys, cBase.detKeys, cBase.parameters )
        return doReturn(returnObj)

    except Exception as e:
        return JsonError( str(e) )


#TODO: Wf from .prototypeWfActions import doWfAction

#   ----------------------------------------
