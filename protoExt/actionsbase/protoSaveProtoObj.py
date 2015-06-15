
def protoSaveProtoObj(request):
    """ Save full metadata
    
    * objetos del tipo _XXX                   se guardan siempre en CustomDefinition 
    * objetos del tipo prototype.protoTable   se guardan siempre en Prototype 
     
    * Solo los adminstradores tienen el derecho de guardar pcls
    
    custom :  Los objetos de tipo custom, manejan la siguiente llave 
    
        _ColSet.[viewCode]        listDisplaySet  
        _QrySet.[viewCode]        filterSet
        _menu 
    
    Para manejar el modelo en las generacion de protoPci's  se usa :
    
        prototype.protoTable.[protoModel-viewCode]  --> al leer la pcl se leera prototype.protoTable.[protoModel-viewCode]
    
    """

    if request.method != 'POST':
        return JsonError('invalid message') 

    custom = False  
    prototype = False
    create = False 
     
    viewCode = request.POST.get('viewCode', '')

    userProfile = getUserProfile(request.user) 

    # Reglas para definir q se guarda  
    if viewCode.find('_') == 0 :
        custom = True 
    if viewCode.startswith(PROTO_PREFIX) :
        prototype = True 

    # Carga la meta 
    sMeta = request.POST.get('protoMeta', '')
    
    # Es customProperty 
    if custom: 

        try:
            protoDef, create = CustomDefinition.objects.get_or_create(code=viewCode, smOwningTeam=userProfile.userTeam)
        except Exception as e:
            return JsonError(getReadableError(e)) 

    # Es prototype
    elif prototype: 

        try:
            # debe existir previamente
            protoCode = viewCode.replace(PROTO_PREFIX, '')
            
            protoMeta = json.loads(sMeta)
            entityId = protoMeta['protoEntityId'] 
            entityObj = Entity.objects.get(id=entityId)
            protoDef, create = Prototype.objects.get_or_create(code=protoCode, entity=entityObj, smOwningTeam=userProfile.userTeam)
 
        except Exception as e:
            return JsonError(getReadableError(e)) 

    else: 

        # Verifica los permisos  
        viewEntity = getBaseModelName(viewCode)
        model = getDjangoModel(viewEntity)
        if not getModelPermission(request.user, model, 'config') : 
            return JsonError('permission denied') 

        try:
            protoDef = ViewDefinition.objects.get_or_create(code=viewCode)[0]
        except Exception as e:
            return JsonError(getReadableError(e)) 

        protoDef.active = True 
        protoDef.overWrite = False 

        # borra el custom por q confunde haecer modif en un lado y otro 
        try:
            CustomDefinition.objects.filter(code='_custom.' + viewCode, smOwningTeam=userProfile.userTeam).delete()
        except:
            pass


    protoDef.metaDefinition = sMeta 
    protoDef.save()    

    return  JsonSuccess({ 'message': 'Ok' })
