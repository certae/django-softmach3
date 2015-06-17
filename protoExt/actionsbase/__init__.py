# -*- coding: utf-8 -*-

import json

from django.contrib.admin.sites import  site
from protoLib.getStuff import getBaseModelName, getDjangoModel, getUserProfile 

from protoExt.utils.utilsWeb import JsonError 
from protoExt.utils.utilsWeb import doReturn


class cAux: 
    """
    Class for passing parameters 
    """
    def __init__(self):
        self.viewCode = ''  
        self.viewEntity = ''  
        self.userProfile = None   


def validateRequest( request ): 

    cBase = cAux()
    if not request.user.is_authenticated(): 
        return cBase, JsonError('readOnly User')
    
    if request.method != 'POST':
        return cBase, JsonError('invalid message') 

    cBase.viewCode = request.POST.get('viewCode', '') 
    cBase.viewEntity = getBaseModelName(cBase.viewCode)
    cBase.userProfile = getUserProfile( request.user ) 

    return cBase, None  


def protoExecuteAction(request):
    """ Ejecuta una opcion
    """

    #TODO: Wf from .prototypeWfActions import doWfAction

    def doAdminAction(model, selectedKeys, parameters, actionDef, modelAdmin):

        for action in modelAdmin.actions:
            if action.__name__ == actionName:
                break

        if not action:
            return doReturn ({'success':False, 'message' : 'Action notFound'})


        Qs = model.objects.select_related()
        Qs = Qs.filter(pk__in=selectedKeys)

        try:
            returnObj = action(modelAdmin, request, Qs , parameters)
            return doReturn (returnObj)

        except Exception as e:
            return doReturn ({'success':False, 'message' : str(e) })



#   ----------------------------------------
    def doAdminDetailAction(model, selectedKeys, detKeys, parameters, actionDef, modelAdmin ):

        for action in modelAdmin.actions:
            if action.__name__ == actionName:
                break

        if not action:
            return doReturn ({'success':False, 'message' : 'Action notFound'})

        try:
            returnObj = action( modelAdmin, request, selectedKeys, detKeys, parameters )
            return doReturn (returnObj)

        except Exception as e:
            return doReturn ({'success':False, 'message' : str(e) })


#   ----------------------------------------

    if not request.user.is_authenticated():
        return doReturn ({'success':False , 'message' : 'readOnly User'})

    if request.method != 'POST':
        return doReturn ({'success':False , 'message' : 'PostAction required'})

    actionName = request.POST.get('actionName', '')

    viewCode = request.POST.get('viewCode', '')
    viewEntity = getBaseModelName(viewCode)

    selectedKeys = request.POST.get('selectedKeys', [])
    selectedKeys = json.loads(selectedKeys)

    parameters = request.POST.get('parameters', [])
    parameters = json.loads(parameters)

    actionDef = request.POST.get('actionDef', {})
    actionDef = json.loads(actionDef)

    # hace el QSet de los registros seleccionados
    if actionDef.get('selectionMode', '') != 'none' and selectedKeys.__len__() == 0:
        return doReturn ({'success':False, 'message' : 'No record selected'})


    # Obtiene el modelo
    try:
        model = getDjangoModel(viewEntity)
        modelAdmin = site._registry.get(model)
    except :
        return doReturn ({'success':False, 'message' : 'Model notFound'})


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
        return doReturn ({'success':False, 'message' : 'Action notFound'})



#   ----------------------------------------


def getReturnMsg( cBase  ):

    from protoLib.getStuff import getAllModelPermissions 

    jsondict = {
        'success':True,
        'message': '',
        'metaData':{
            # The name of the property which contains the Array of row objects. ...
            'root': 'rows',

            # Name of the property within a row object that contains a record identifier value. ...
            'idProperty': cBase.protoMeta.get( 'idProperty', 'id'),

            # Name of the property from which to retrieve the total number of records in t
            'totalProperty':'totalCount',

            # Name of the property from which to retrieve the success attribute. ...
            'successProperty':'success',
            
            # The name of the property which contains a response message. (optional)
            'messageProperty': 'message',
            },
        'protoMeta': cBase.protoMeta,
        'permissions': getAllModelPermissions(cBase.userProfile.user, cBase.model),
        'rows':[],
        'totalCount': 0,
    }

    return json.dumps( jsondict )

