# -*- encoding: UTF-8 -*-


from protoLib.models import UserProfile, TeamHierarchy


def  getUserProfile(pUser, action, actionInfo):
    """
    Obtiene el profile de usuario, permitira retornar valores como el
    idioma y otros eltos del entorno,

    Permitira tambien el manejo de logs,

    action :
    - login
    - saveData
    - loadData
    - saveConfig

    actionInfo :
    - Entidad, ids, fecha etc

    Se puede crear una sesion propia para manejar el log de autorizaciones
    permitira cerrar una sesion cambiando el estado tal como se maneja en sm

    """

    # User
    if pUser is None:
        return None

    # Profile
    uProfile = UserProfile.objects.get_or_create(user=pUser)[0]

    if uProfile.userTeam is None:
        # verifica el grupo  ( proto por defecto )
        uProfile.userTeam = TeamHierarchy.objects.get_or_create(code='proto')[0]
        uProfile.save()

    if action == 'login':
        uOrgTree = uProfile.userTeam.treeHierarchy

        # permisos adicionales
        for item in pUser.usershare_set.all() :
            uOrgTree += ',' + item.userTeam.treeHierarchy

        # Organiza los ids
        uProfile.userTree = ','.join(set(uOrgTree.split(',')))
        uProfile.save()

        usrLanguage = uProfile.language
        if usrLanguage not in ['es', 'en', 'fr' ] :
            usrLanguage = 'fr'
        usrLanguage = 'protoLib.localisation.' + usrLanguage
        myModule = __import__(usrLanguage, globals(), locals(), ['__language' ], -1)

        return myModule.__language


    return uProfile



def getUserNodes(pUser, viewEntity):
    """
    Verifica la jerarquia hacia los nodos superiores ( RefOnly )
    """
    userProfile = getUserProfile(pUser, 'list', viewEntity)
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
