# -*- coding: utf-8 -*-

from protoExt.models import ViewDefinition, CustomDefinition 
from protoLib.getStuff import getDjangoModel, getModelPermission 
from protoExt.utils.utilsWeb import JsonError, JsonSuccess
from protoExt.utils.utilsBase import getReadableError
from protoExt.views import validateRequest 
from protoExt.views.prototypeActions import isPrototypePci, saveProtoPci


def protoSaveProtoObj(request):
    """ Save full metadata
    
    * objetos del tipo _XXX                   se guardan siempre en CustomDefinition 
    * objetos del tipo prototype.protoTable   se guardan siempre en Prototype 
     
    * Solo los adminstradores tienen el derecho de guardar pcls
    
    custom :  Los objetos de tipo custom, manejan la siguiente llave 
    
        _ColSet.[cBase.viewCode]        listDisplaySet  
        _QrySet.[cBase.viewCode]        filterSet
        _menu 
    
    Para manejar el modelo en las generacion de protoPci's  se usa :
    
        prototype.protoTable.[protoModel-cBase.viewCode]  --> al leer la pcl se leera prototype.protoTable.[protoModel-cBase.viewCode]
    """

    cBase, msgReturn = validateRequest( request )
    if msgReturn: return msgReturn  

    # Carga la meta 
    cBase.sMeta = request.POST.get('protoMeta', '')
     
    # Reglas para definir q se guarda  
    if isPrototypePci( cBase ):
        return saveProtoPci( cBase )


    if cBase.viewCode.find('_') == 0 :
        # Es customProperty 

        try:
            protoDef = CustomDefinition.objects.get_or_create(
                            code= cBase.viewCode, 
                            smOwningUser= cBase.userProfile.user
                            )[0]

        except Exception as e:
            return JsonError(getReadableError(e)) 

    else: 

        cBase.model = getDjangoModel( cBase.viewEntity )

        # Verifica los permisos  
        if not getModelPermission(request.user, cBase.model, 'config') : 
            return JsonError('permission denied') 

        try:
            protoDef = ViewDefinition.objects.get_or_create(code=cBase.viewCode)[0]
        except Exception as e:
            return JsonError(getReadableError(e)) 

        protoDef.active = True 
        protoDef.overWrite = False 

        # borra el custom por q confunde haecer modif en un lado y otro 
        try:
            CustomDefinition.objects.filter(\
                code='_custom.' + cBase.viewCode,\
                smOwningUser=cBase.userProfile.user
            ).delete()

        except:
            pass


    protoDef.metaDefinition = cBase.sMeta 
    protoDef.save()    

    return  JsonSuccess({ 'message': 'Ok' })


