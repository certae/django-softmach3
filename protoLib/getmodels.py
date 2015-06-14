# -*- coding: utf-8 -*-


def getUserProfile( cuser):
    from protoLib.models.smbase import UserProfile
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




# -----------------------------------------------
# DGT: Verificar y borrar lo q no se necesite 



def getUserNodes(pUser, viewEntity):
    """
    Verifica la jerarquia hacia los nodos superiores ( CELL - RefOnly )
    """
    userProfile = getUserProfile(pUser)
    userNodes = None
    if userProfile and userProfile.userTree:
        userNodes = userProfile.userTree.split(',')

    return userNodes



def getModelPermission( pUser, model , perm=None):
    appName = model._meta.app_label
    modName = model._meta.model_name

    return  pUser.is_superuser or pUser.has_perm(appName + '.' + perm + '_' + modName)
    

def getAllModelPermissions(pUser, model ):
    """
    Equivalente de get_all_permissions por objeto 
    get_all_permissions : no trae lo q necesito, pues lo guarda en un cache y filtra por objeto,
    """

    permissions = {}
    for perm in [ 'menu', 'list', 'add', 'change', 'delete', 'config', 'custom', 'refallow' ]:
        if getModelPermission( pUser, model, perm ):
            permissions[ perm ] = True  

    return  permissions

#  ---------------


def  getUserLanguage( usrLanguage ):

    if usrLanguage not in ['es', 'en', 'fr' ] :
        usrLanguage = 'en'
    usrLanguage = 'protoExt.localisation.' + usrLanguage
    myModule = __import__( usrLanguage, globals(), locals(), ['__language' ], 0)

    return myModule.__language

