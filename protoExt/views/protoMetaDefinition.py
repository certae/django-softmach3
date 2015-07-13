# -*- coding: utf-8 -*-

import json
from protoExt.utils.utilsWeb import JsonError
from protoExt.meta import META_OBJECTS, META_PROPERTIES
from django.http.response import HttpResponse

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


    metaDefinition = { 
        'metaObjects' : META_OBJECTS, 
        'metaProperties' : META_PROPERTIES 
    }
    
    context = json.dumps( metaDefinition ) 
    return HttpResponse(context, content_type="application/json")
