# -*- coding: utf-8 -*-

from django.contrib.contenttypes.models import ContentType
from protoLib.models.protoContext import ContextUser, ContextVar, ContextEntity
from protoExt.views import validateRequest
from protoExt.models import ViewDefinition
from protoExt.utils.utilsWeb import JsonError
from protoLib.getStuff import getDjangoModel



def actionSetContext(request, queryset , parameters):
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
    cBase.defTo = cBase.protoMeta.get( 'contextTo' , [] )
    for detail in cBase.defTo: 

        ettName = detail.get( 'deftModel').strip()
        entity = ContentType.objects.get_by_natural_key( *ettName.split('.')) 
        detField =  detail.get( 'deftField' )

        defValues = { 'propName' : detField }
        ContextEntity.objects.update_or_create(
           contextVar = cVar,
           entity = entity,  
           defaults= defValues 
        )  

    # Add or delete filter 
    if queryset: 
        baseReg = queryset[0]
        defValues = {
            'propValue': baseReg.id , 
            'description' : baseReg.__str__(), }
    else: 
        defValues = {
            'propValue': None , 
            'description' : '' }


    # Update UserContext 
    ContextUser.smObjects.update_or_create(
        contextVar = cVar,
        smOwningUser = cBase.userProfile.user,
        defaults= defValues 
    )  

    return  {'success':True , 'message' :  'Ok' }

