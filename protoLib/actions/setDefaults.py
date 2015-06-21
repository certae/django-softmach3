# -*- coding: utf-8 -*-
from protoExt.actionsbase.protoGrid import getModelDetails
from pyexpat import model
from django.views.generic import detail


# -*- coding: utf-8 -*-


def actionSetDefaults(request, queryset , parameters):
    """
    Genera los defaults en la tabla  UserContext 
    """

    # Obtiene el proyecto y se asegura q sean todas de un mismo proyecto
    baseReg = queryset[0]
    baseModel = baseReg._meta.model 

    details = getModelDetails(baseModel, True)

    for detail in details: 
        # Obtiene el contenttye 
        cType = detail.get( 'detailModel').getAttribute( 'contenttype' ) 


    return  {'success':True , 'message' :  'Ok' }


