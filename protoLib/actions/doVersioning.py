# -*- coding: utf-8 -*-
from protoLib.getStuff import getDjangoModel
from protoExt.utils.utilsWeb import JsonError
from protoExt.views.protoGrid import getModelDetails
from protoLib.models.versions import VersionHeaders


def doDeleteVersion(modeladmin, request, queryset, parameters):
    """ 
    TODO : Borra los datos de una version existente
    """

    result = getDetailList( modeladmin, request, queryset, parameters )
    if type(result) == list:
        return result 


def doCreateVersion(modeladmin, request, queryset, parameters):
    """ 
    Clear una copia de la informacion bajo una nueva version 
    """

    result = getDetailList( modeladmin, request, queryset )
    if type(result) == list:
        return result 



def getDetailList( modeladmin, request, queryset  ):


#   El QSet viene con la lista de Ids  
    if queryset.count() != 1:
        return  {'success':False, 'message' : 'One version needed !!' }
        
#   Get selected version
    pVersion = queryset[0]
    detailList = []

#   Get Version Headers 
    for entity in VersionHeaders.objects.all(): 
        addDetailToVersionList( detailList,  entity.modelCType.model_class()  )

    return  detailList 


def addDetailToVersionList( detailList, model ):

    detailList.append ( model ) 
    baseMeta = model._meta

    for detail in baseMeta.get_all_related_objects():
        addDetailToVersionList( detailList, detail.related_model )

