# -*- coding: utf-8 -*-
from protoExt.actionsbase.protoGrid import getModelDetails
from django.views.generic import detail
from django.contrib.contenttypes.models import ContentType
from protoLib.models.protoContext import UserContext

# -*- coding: utf-8 -*-


def actionSetDefaults(request, queryset , parameters):
    """
    Genera los defaults en la tabla  UserContext 
    """

    # Obtiene el proyecto y se asegura q sean todas de un mismo proyecto
    baseReg = queryset[0]
    baseModel = baseReg._meta.model 

    details = getModelDetails(baseModel, True)

    vrDefault = {'propValue': baseReg.id , \
                 'propDescription' : baseReg.__str__()}


    for detail in details: 
        # Obtiene el contenttye 
        detModel = detail.get( 'detailModel')
        modelCType = ContentType.objects.get_for_model(detModel)
        detField =  detail.get( 'detailField' )
        
        UserContext.smObjects.update_or_create(
           modelCType = modelCType,
           smOwningUser = request.user,
           propName = detField,
           defaults = vrDefault )  


    return  {'success':True , 'message' :  'Ok' }


