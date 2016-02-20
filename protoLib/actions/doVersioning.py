# -*- coding: utf-8 -*-


import uuid
from protoExt.views import validateRequest
from protoLib.getStuff import getDjangoModel


def doDeleteVersion(modeladmin, request, queryset, parameters):
    """ 
    Borra los datos de una version existente
    """

    entitySet = getVersionDependency(modeladmin, request, queryset)
    if type(entitySet) is not set:
        return entitySet

#   Delete  selected version
    return _doDelVersion(entitySet, queryset[0])


def _doDelVersion(entitySet, v1):

    #  Delete old versions
    for pEntity in entitySet:
        pEntity.objects.filter(smVersion=v1).delete()

    return {'success': True, 'message':  'Ok'}


def doCopyVersion(modeladmin, request, queryset, parameters):
    """ 
    Clear una copia de la informacion bajo una nueva version 
    """

    entitySet = getVersionDependency(modeladmin, request, queryset)
    if type(entitySet) is not set:
        return entitySet

    # Se manejan uan estructuras por tabla con dos listas ordenadas {
    # 'entidad' : [ [], [] ] }
    idEquiv = {}

#   Get selected version
    v0 = queryset[0].versionBase
    v1 = queryset[0]


    _doDelVersion(entitySet, v1)

    for pEntity in entitySet:

        entityName = pEntity._meta.db_table

        # Dependant entity
        # Si anulo la entidad dependiente, solo pasan los campos del padre, el hijo no se copia 
        # La solucion es buscar cuando un registro del padre es invocado por el hijo 
        # if len(pEntity._meta.parents) > 0: continue

        # Duplicate entity?
        if idEquiv.get(entityName, '') != '':
            continue

        # Listas de ids
        idList0 = []
        idList1 = []

        #  Hace la copia
        for reg in pEntity.objects.filter(smVersion=v0):

            # Excepcion para el manejode relaciones heredadas de propiedades ( relationship - property )
            try:
                parentLink = ( entityName == 'prototype_property' ) and reg.isForeign
            except: parentLink = False 
            if parentLink: continue

            idList0.append(reg.pk)

            reg.smUUID = uuid.uuid4()
            reg.smVersion = v1

            # https://docs.djangoproject.com/en/1.9/topics/db/queries/#copying-model-instances             
            reg.pk = None
            reg.id = None
            reg.save()

            idList1.append(reg.id)

        # Guarda la estructura con las listas de equivalencia de ids
        idEquiv[entityName] = [idList0, idList1]

    # Busca todas los foreignkey  por UUID y los actualiza
    for pEntity in entitySet:

        entityName = pEntity._meta.db_table

        # FK identification          
        relFields = []
        for f in pEntity._meta.get_fields():
            if f.is_relation and (f.many_to_one and f.related_model):
                relName = f.related_model()._meta.db_table
                if not relName in idEquiv.keys(): continue
                relFields.append( (f, relName) )
        
        if len(relFields) == 0: 
            continue 

        for reg in pEntity.objects.filter(smVersion=v1):

            # Excepcion para el manejode relaciones heredadas de propiedades ( relationship - property )
            try:
                parentLink = ( entityName == 'prototype_property' ) and reg.isForeign
            except: parentLink = False 
            if parentLink: continue

            for f, relName in relFields:
       
                # get entity idsVersionTitle
                idRef0 = getattr( reg , f.column)
                idList0, idList1 = idEquiv.get(relName, [[], []])

                ix = idList0.index(idRef0)
                setattr( reg , f.column, idList1[ ix ])

            reg.save()


    return {'success': True, 'message': 'Ok'}


def getVersionDependency( modeladmin, request, queryset):

    #   El QSet viene con la lista de Ids
    if queryset.count() != 1:
        return {'success': False, 'message': 'One version needed !!'}


    detailSet = set()

    cBase, message = validateRequest( request )
    if message: return detailSet  
    
    # Get base model 
    try:
        VTitle = getDjangoModel(cBase.viewEntity)
        VHeaders = getattr(VTitle, 'versionHeaders', [])
    except :
        return detailSet


#   Get Version Headers
    for entityName in VHeaders:
        addDetailToVersionList(detailSet,  entityName  )


    return detailSet


def addDetailToVersionList(detailSet, entityName  ):

    # Get base model 
    try:
        model = getDjangoModel(entityName)
        model._meta.get_field('smVersion')
        detailSet.add(model)
    except:
        return 


