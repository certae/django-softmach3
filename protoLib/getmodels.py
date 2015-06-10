# -*- coding: utf-8 -*-

from protoLib.models.smbase import UserProfile, TeamHierarchy

def getUserProfile( cuser): 
    return UserProfile.objects.get_or_create( user = cuser)[0]

def getUserTeam( cuser): 
    return getUserProfile( cuser ).userTeam 


def getDjangoModel(modelName):
    """
    Obtiene el modelo
    """

    try:
        from django.apps import apps
        get_model = apps.get_model
        get_models = apps.get_models
    except ImportError:
        from django.db.models.loading import get_model, get_models  

    if modelName.count('.') == 1:
        model = get_model(*modelName.split('.'))

    elif modelName.count('.') == 0:
        for m in get_models(include_auto_created=True):
            if m._meta.object_name.lower() == modelName.lower():
                model = m
                break

    elif modelName.count(".") == 2:
        model = get_model(*modelName.split(".")[0:2])

    if model is None:
        raise Exception('model not found:' + modelName)

    return model



def getNodeHierarchy(record, parentField, codeField, pathFunction):
    "Returns the full hierarchy path."

    pRec = record.__getattribute__(parentField)
    if pRec   :
        return pRec.__getattribute__(pathFunction) + ',' +  str(record.__getattribute__(codeField))
    else:
        return str(record.__getattribute__(codeField))

