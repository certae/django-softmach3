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



def getModelPermissions(pUser, model , perm=None):

    appName = model._meta.app_label
    modName = model._meta.module_name

    return  getOptionPermissions(pUser, appName, modName , perm)


def getOptionPermissions(pUser, appName, modName , perm=None):

    # Verifica los permisos para cada opcion
    permissions = {}

    def getIndPermission(perm):
        permissions[ perm ] = pUser.is_superuser or pUser.has_perm(appName + '.' + perm + '_' + modName)

    # Si es un solo permiso retorna true / false
    if not (perm is None):
        getIndPermission (perm)
        return permissions[ perm ]

    # Si son todos retorna un objto
    # get_all_permissions  no vale la pena, pues lo guarda en un cache y filtra por objeto,
    # la busqueda individual usa el mismo cache ya cargarda
    getIndPermission ('menu')
    getIndPermission ('list')
    getIndPermission ('add')
    getIndPermission ('change')
    getIndPermission ('delete')
    getIndPermission ('config')
    getIndPermission ('custom')
    getIndPermission ('refallow')

    return  permissions


#  ---------------


# def  getUserProfile(pUser):
#     """
#     Obtiene el profile de usuario, permitira retornar valores como el
#     idioma y otros eltos del entorno,

#     Permitira tambien el manejo de logs,

#     action :
#     - login
#     - saveData
#     - loadData
#     - saveConfig

#     actionInfo :
#     - Entidad, ids, fecha etc

#     Se puede crear una sesion propia para manejar el log de autorizaciones
#     permitira cerrar una sesion cambiando el estado tal como se maneja en sm

#     """

#     # User
#     if pUser is None:
#         return None

#     # Profile
#     uProfile = UserProfile.objects.get_or_create(user=pUser)[0]

#     if uProfile.userTeam is None:
#         # verifica el grupo  ( proto por defecto )
#         uProfile.userTeam = TeamHierarchy.objects.get_or_create(code='proto')[0]
#         uProfile.save()

#     if action == 'login':
#         uOrgTree = uProfile.userTeam.treeHierarchy

#         # permisos adicionales
#         for item in pUser.usershare_set.all() :
#             uOrgTree += ',' + item.userTeam.treeHierarchy

#         # Organiza los ids
#         uProfile.userTree = ','.join(set(uOrgTree.split(',')))
#         uProfile.save()

#         usrLanguage = uProfile.language
#         if usrLanguage not in ['es', 'en', 'fr' ] :
#             usrLanguage = 'fr'
#         usrLanguage = 'protoLib.localisation.' + usrLanguage
#         myModule = __import__(usrLanguage, globals(), locals(), ['__language' ], -1)

#         return myModule.__language


#     return uProfile



# def getUserNodes(pUser, viewEntity):
#     """
#     Verifica la jerarquia hacia los nodos superiores ( RefOnly )
#     """
#     userProfile = getUserProfile(pUser)
#     userNodes = None
#     if userProfile and userProfile.userTree:
#         userNodes = userProfile.userTree.split(',')

#     return userNodes



# def getModelPermissions(pUser, model , perm=None):

#     appName = model._meta.app_label
#     modName = model._meta.module_name

#     return  getOptionPermissions(pUser, appName, modName , perm)


# def getOptionPermissions(pUser, appName, modName , perm=None):

#     # Verifica los permisos para cada opcion
#     permissions = {}

#     def getIndPermission(perm):
#         permissions[ perm ] = pUser.is_superuser or pUser.has_perm(appName + '.' + perm + '_' + modName)

#     # Si es un solo permiso retorna true / false
#     if not (perm is None):
#         getIndPermission (perm)
#         return permissions[ perm ]

#     # Si son todos retorna un objto
#     # get_all_permissions  no vale la pena, pues lo guarda en un cache y filtra por objeto,
#     # la busqueda individual usa el mismo cache ya cargarda
#     getIndPermission ('menu')
#     getIndPermission ('list')
#     getIndPermission ('add')
#     getIndPermission ('change')
#     getIndPermission ('delete')
#     getIndPermission ('config')
#     getIndPermission ('custom')
#     getIndPermission ('refallow')

#     return  permissions


