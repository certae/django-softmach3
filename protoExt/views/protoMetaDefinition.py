# -*- coding: utf-8 -*-

import json
from protoExt.utils.utilsWeb import JsonError
from protoExt.meta import META_OBJECTS, META_PROPERTIES, verifyMeta
from django.http.response import HttpResponse
from protoLib.getStuff import cAux

def protoGetMetaStructure(request):
    """
    Load MetaDefinition 
    """
    
    if request.method != 'POST': 
        return JsonError('invalid message') 

    metaDefinition = { 
        'metaObjects' : META_OBJECTS, 
        'metaProperties' : META_PROPERTIES 
    }
    
    context = json.dumps( metaDefinition ) 
    return HttpResponse(context, content_type="application/json")



def protoVerifyMeta(request):
    """
    Verify MetaDefinition ( add Nodes )
    """
    
    if request.method != 'POST': 
        return JsonError('invalid message') 

    cBase = cAux()
    cBase.oMeta = json.loads( request.POST.get('oMeta', '{}')) 
    cBase.tNode = json.loads( request.POST.get('tNode', '{}'))
    cBase.ptType = request.POST.get('ptType', '') 

    # retorna meta y tNode, toma solo el tNode 
    cBase.tNode = verifyMeta( cBase.oMeta, cBase.ptType, cBase.tNode )[1]
    
    context = json.dumps( cBase.tNode ) 
    return HttpResponse(context, content_type="application/json")
