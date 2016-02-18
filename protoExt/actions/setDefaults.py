# -*- coding: utf-8 -*-

from django.contrib.contenttypes.models import ContentType
from protoLib.models.protoContext import ContextUser, ContextVar, ContextEntity
from protoExt.views import validateRequest
from protoExt.models import ViewDefinition
from protoExt.utils.utilsWeb import JsonError
from protoLib.getStuff import getDjangoModel



def actionSetDefaults(request, queryset , parameters):
    """
    Genera los defaults en la tabla  ContextUser 
    """

    cBase, message = validateRequest( request )
    if message: return message  
    
    # Lee la pci      
    try:
        protoDef = ViewDefinition.objects.get( code = cBase.viewCode )
        cBase.protoMeta = protoDef.metaDefinition
    except Exception :
        return JsonError('ViewDefinition not found: {0}'.format( cBase.viewCode  )) 



    # Get base model 
    try:
        cBase.model = getDjangoModel(cBase.viewEntity)
    except :
        return JsonError( 'Model notFound')

    # Get ContextVar 
    modelCType = ContentType.objects.get_for_model( cBase.model ) 
    cVar = ContextVar.objects.update_or_create(
       modelCType = modelCType,
       propName = 'id',
    )[0]

    # Add Context Entity Values 
    cBase.defTo = cBase.protoMeta.get( 'defaultTo' , [] )
    for detail in cBase.defTo: 

        ettName = detail.get( 'deftModel').strip()
        entity = ContentType.objects.get_by_natural_key( *ettName.split('.')) 
        detField =  detail.get( 'deftField' )

        ContextEntity.objects.update_or_create(
           contextVar = cVar,
           entity = entity,  
           propName = detField
        )  

    # Add or delete filter 
    vrDefault =  None 
    if queryset: 
        vrDefault = queryset[0].id

    # Update UserContext 
    ContextUser.smObjects.update_or_create(
        contextVar = cVar,
        propValue = vrDefault
    )  

    return  {'success':True , 'message' :  'Ok' }

