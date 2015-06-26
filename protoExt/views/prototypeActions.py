# -*- coding: utf-8 -*-

"""
Funciones asociadas al manejo de prototype 
"""

import json 

from django.conf import settings 
from protoExt.utils.utilsWeb import JsonError, JsonSuccess 
from protoExt.utils.utilsBase import getReadableError

try:
    PROTO_PREFIX = settings.PROTO_PREFIX or "prototype.ProtoTable."
    from prototype.models import Prototype, Entity
except: 
    pass     


def isPrototypePci( cBase   ):

    if cBase.viewCode.startswith(PROTO_PREFIX)  and cBase.viewCode != cBase.viewEntity :
        return True
    return False 


def getPrototypePci( cBase ):

    try:
        prototypeView = cBase.viewCode.replace( PROTO_PREFIX, '')
        protoDef = Prototype.objects.get(code=prototypeView, smOwningTeam=cBase.userProfile.userTeam)

        cBase.protoMeta = protoDef.metaDefinition
        cBase.protoMeta['viewCode'] = cBase.viewCode  
        
    except:
        return JsonError('prototype not found: {0}'.format( cBase.viewCode ))


        
def saveProtoPci( cBase ): 

    protoCode = cBase.viewCode.replace( PROTO_PREFIX, '' )

    try:
        protoMeta = json.loads( cBase.sMeta)

        entityId = protoMeta['protoEntityId'] 
        entityObj = Entity.objects.get(id=entityId)
        
        protoDef  = Prototype.objects.get(\
            code= protoCode, \
            entity= entityObj, \
            smOwningTeam= cBase.userProfile.userTeam \
            )
 
        protoDef.metaDefinition = cBase.sMeta 
        protoDef.save()    

    except Exception as e:
        return JsonError(getReadableError(e)) 

    return  JsonSuccess({ 'message': 'Ok' })
