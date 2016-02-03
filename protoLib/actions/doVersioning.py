# -*- coding: utf-8 -*-

from protoLib.models.versions import VersionHeaders
import uuid


def doDeleteVersion(modeladmin, request, queryset, parameters):
    """ 
    Borra los datos de una version existente
    """

    result = getdetailSet(modeladmin, request, queryset)
    if type(result) is not set:
        return result

#   Get selected version
    v1 = queryset[0].versionCode

    for pEntity in result:

        # Version Allow
        try:
            pEntity._meta.get_field('smVersion')
        except:
            continue

        #  Delete old versions
        pEntity.objects.filter(smVersion=v1).delete()

    return {'success': True, 'message':  'Ok'}


def doCreateVersion(modeladmin, request, queryset, parameters):
    """ 
    Clear una copia de la informacion bajo una nueva version 
    """

    result = getdetailSet(modeladmin, request, queryset)
    if type(result) is not set:
        return result

    # Se manejan uan estructuras por tabla con dos listas ordenadas {
    # 'entidad' : [ [], [] ] }
    idEquiv = {}

#   Get selected version
    v0 = queryset[0].versionBase
    v1 = queryset[0].versionCode

    for pEntity in result:

        entityName = pEntity._meta.db_table

        # Version Allow
        try:
            pEntity._meta.get_field('smVersion')
        except:
            continue

        # Dependant entity
        if len(pEntity._meta.parents) > 0:
            continue

        # Duplicate entity?
        if idEquiv.get(entityName, '') != '':
            continue

        # Listas de ids
        idList0 = []
        idList1 = []

        #  Delete old versions
        pEntity.objects.filter(smVersion=v1).delete()

        #  Hace la copia
        for reg in pEntity.objects.filter(smVersion=v0):

            idList0.append(reg.pk)

            reg.smUUID = uuid.uuid4()
            reg.smVersion = v1
            reg.id = None
            reg.save()

            idList1.append(reg.id)

        # Guarda la estructura con las listas de equivalencia de ids
        idEquiv[entityName] = [idList0, idList1]

    # Busca todas los foreignkey  por UUID y los actualiza
    for pEntity in result:

        entityName = pEntity._meta.db_table

        # Version Allow
        try:
            pEntity._meta.get_field('smVersion')
        except:
            continue

        # Dependant entity
        if len(pEntity._meta.parents) > 0:
            continue

        for f in pEntity._meta.get_fields():
            if not (f.is_relation or f.one_to_one or (f.many_to_one and f.related_model)):
                continue

            entityName = pEntity._meta.db_table

            # get entity ids
            idList0, idList1 = idEquiv.get(entityName, set([[], []]))

    return {'success': True, 'message': 'Ok'}


def getdetailSet(modeladmin, request, queryset):

    #   El QSet viene con la lista de Ids
    if queryset.count() != 1:
        return {'success': False, 'message': 'One version needed !!'}

    detailSet = set()

#   Get Version Headers
    for entity in VersionHeaders.objects.all():
        addDetailToVersionList(detailSet,  entity.modelCType.model_class())

    return detailSet


def addDetailToVersionList(detailSet, model):

    detailSet.add(model)

    for detail in model._meta.get_all_related_objects():
        addDetailToVersionList(detailSet, detail.related_model)
