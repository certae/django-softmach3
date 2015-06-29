# -*- coding: utf-8 -*-

import json

from django.contrib.admin.sites import  site
from protoLib.getStuff import getUserProfile 

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

    cBase.viewCode = request.POST.get('viewCode', '').strip() 
    cBase.userProfile = getUserProfile( request.user ) 

    # Elimina un punto extrano q viene de js      
    if cBase.viewCode[-1] == '.':
        cBase.viewCode = cBase.viewCode[:-1]

    # Si viene el valor lo asume por defecto 
    cBase.viewEntity = request.POST.get('viewEntity', cBase.viewCode ).strip() 

    # Verifica si es una vista del modelo y obtiene el nombre base 
    if cBase.viewEntity.count(".") >= 2:
        app, model = cBase.viewEntity.split(".")[:2]
        cBase.viewEntity = app + '.' + model


    return cBase, None  



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

