# -*- coding: utf-8 -*-
from protoLib.getStuff import getDjangoModel
from protoExt.utils.utilsWeb import JsonError
from protoExt.views.protoGrid import getModelDetails
from protoLib.models.versions import VersionHeaders


def doDeleteVersion(modeladmin, request, queryset, parameters):
    """ 
    TODO : Borra los datos de una version existente
    """

    result = getdetailSet( modeladmin, request, queryset, parameters )
    if type(result) == list:
        return result 


def doCreateVersion(modeladmin, request, queryset, parameters):
    """ 
    Clear una copia de la informacion bajo una nueva version 
    """

    result = getdetailSet( modeladmin, request, queryset )
    if type(result) is not list:
        return result 

    # Se manejan uan estructuras por tabla con dos listas ordenadas { 'entidad' : [ [], [] ] }
    idEquiv = {}

#   Get selected version
    v0 = queryset[0].versionBase 
    v1 = queryset[0].versionCode 

    for pEntity in  result: 
        if not hasattr( pEntity, 'smVersion'): 
            continue 

        # Listas de ids 
        idList0 = []
        idList1 = []

        #  Se asegura de borrar para no sobre escribir 
        pEntity.objects.filter( smVersion = v1 ).delete()

        #  Hace la copia
        for reg in pEntity.objects.filter( smVersion = v0 ): 
            
            idList0.append( reg.pk )

            reg.smUUID = uuid.uuid4()
            reg.smVersion = v1 
            reg.id = None 
            reg.save()

            idList1.append( reg.id )


        # Guarda la estructura con las listas de equivalencia de ids 
        idEquiv[ pEntity._meta.db_table ] = [ idList0, idList1 ]
        
    # Busca todas los foreignkey  por UUID y los actualiza 


    return {'success':True, 'message' : 'Ok'}


def getdetailSet( modeladmin, request, queryset  ):


#   El QSet viene con la lista de Ids  
    if queryset.count() != 1:
        return  {'success':False, 'message' : 'One version needed !!' }
        
    detailSet = ()

#   Get Version Headers 
    for entity in VersionHeaders.objects.all(): 
        addDetailToVersionList(  detailSet,  entity.modelCType.model_class()  )

    return  detailSet 


def addDetailToVersionList(  detailSet, model ):


    detailSet.add ( model ) 

    for detail in model._meta.get_all_related_objects():
        addDetailToVersionList(  detailSet, detail.related_model )

