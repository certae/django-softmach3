# -*- coding: utf-8 -*-

from django.views.generic import detail
from django.contrib.contenttypes.models import ContentType
from protoLib.models.protoContext import UserContext
from protoExt.views import validateRequest
from protoExt.models import ViewDefinition
from protoExt.utils.utilsWeb import JsonError

# -*- coding: utf-8 -*-


def actionSetDefaults(request, queryset , parameters):
    """
    Genera los defaults en la tabla  UserContext 
    """

    cBase, message = validateRequest( request )
    if message: return message  
    
    # Lee la pci      
    try:
        protoDef = ViewDefinition.objects.get( code = cBase.viewCode )
        cBase.protoMeta = protoDef.metaDefinition
    except Exception :
        return JsonError('ViewDefinition not found: {0}'.format( cBase.viewCode  )) 


    # Obtiene el proyecto y se asegura q sean todas de un mismo proyecto
    if queryset: 
        baseReg = queryset[0]
        vrDefault = {'propValue': baseReg.id , 'propDescription' : baseReg.__str__(), 
                     'isDefault' : True , 'isFilter' : True }
    else: 
        vrDefault = {'propValue': '' , 'propDescription' : '', 
                     'isDefault' : True , 'isFilter' : False }


    cBase.defTo = cBase.protoMeta.get( 'defaultTo' , [] )


    for detail in cBase.defTo: 
        # Obtiene el contenttye 
        detModel = detail.get( 'deftModel')
        modelCType = ContentType.objects.get_by_natural_key( *detModel.strip().split('.')) 
        detField =  detail.get( 'deftField' )
        
        UserContext.smObjects.update_or_create(
           modelCType = modelCType,
           smOwningUser = request.user,
           propName = detField,
           defaults = vrDefault )  


    return  {'success':True , 'message' :  'Ok' }

