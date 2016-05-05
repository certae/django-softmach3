# -*- coding: utf-8 -*-
from protoExt.views import validateRequest
from protoLib.getStuff import getDjangoModel
from protoExt.utils.utilsBase import traceError, list2dict, getReadableError
from protoExt.models import ViewDefinition


def doBuildFieldList(modeladmin, request, queryset):

    cBase, message = validateRequest( request )
    if message: return message   
    
    # Get base model 
    try: 
        cBase.model = getDjangoModel(cBase.viewEntity)
    except :
        traceError()
        return 'model not found: {0}'.format( cBase.viewEntity ) 
    

    # Get ProtoDefinition      
    try:
        protoDef = ViewDefinition.objects.get_or_create(code=cBase.viewCode)[0]
        cBase.protoMeta = protoDef.metaDefinition
    except Exception as e:
        return getReadableError(e) 
   
    # Get all fields in document      
    newFieldDict  = cBase.model.getJfields(None, cBase.model._jDefValueDoc )[0]
    
    # get base fieldDict      
    oldFieldDict = list2dict(cBase.protoMeta[ 'fields' ], 'name')

    # Add  all not info_fields      
    for fName in oldFieldDict.keys() :
        if not fName.startswith( 'info__'): 
            newFieldDict[ fName ]  = oldFieldDict[ fName ]

    # Add fields 
    cBase.protoMeta['fields'] = [] 
    for fName in newFieldDict.keys() :
        cBase.protoMeta['fields'].append( newFieldDict[fName] )


    protoDef.metaDefinition = cBase.protoMeta 
    protoDef.save()    
