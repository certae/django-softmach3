# -*- coding: utf-8 -*-

"""
ProtoGetPci 
"""

import traceback

from django.http import HttpResponse

from protoExt.models import ViewDefinition, CustomDefinition 
from protoLib.getStuff import getDjangoModel, getProtoAdmin 
from protoExt.utils.utilsWeb import JsonError 
from protoExt.views import getReturnMsg, validateRequest 
from protoExt.views.protoGrid import ProtoGridFactory , createProtoMeta
from protoExt.views.getStuff import setContextDefaults

from protoExt.views.prototypeActions import isPrototypePci, getPrototypePci 


def protoGetPCI(request):
    """ 
    Return full metadata (columns, renderers, totalcount...)
    """

    cBase, msgReturn = validateRequest( request )
    if msgReturn: return msgReturn  
    
    try: 
        cBase.model = getDjangoModel(cBase.viewEntity)
    except :
        return JsonError('model not found: {0}'.format( cBase.viewEntity )) 
    

    if isPrototypePci( cBase ): 
        msgReturn = getPrototypePci( cBase )
        if msgReturn: return msgReturn  
    
    else:  
        msgReturn = getBasePci( cBase, False )
        if msgReturn: return msgReturn  

#   ============  Collecciones personalizables  y elementos particulares 
    customCode = '_custom.' + cBase.viewCode 
    try:
        custom = CustomDefinition.objects.get(code=customCode, smOwningUser= cBase.userProfile.user )
        cBase.protoMeta['custom'] = custom.metaDefinition
    except:
        pass

    
    try:

#   ==============  Lee el contexto 
        setContextDefaults( cBase )
        #FUTURE:  addWfParameters( cBase  )

#   ============== Verificacion de la metadata 
        cBase.protoMeta = verifyMeta( cBase , 'pci')
    except Exception:
        traceback.print_exc()    
        return JsonError('invalid definition: {0}'.format( cBase.viewEntity )) 


    context =  getReturnMsg( cBase  )
    return HttpResponse(context, content_type="application/json")


# protoGetPCI ----------------------------



# --------------------------------------------------------------------------

def isFieldDefined(pFields , fName):
    # Verifica si un campo esta en la lista 
    for pField  in pFields:
        if pField.get('name') == fName: 
            return True 
    return False 



def getBasePci(cBase, readOnly = False  ):

    # protoDef : PCI leida de la DB ; created : El objeto es nuevo
    try:
        protoDef = ViewDefinition.objects.get(code=cBase.viewCode)
        created = False 

    except ViewDefinition.DoesNotExist:
    
        if readOnly :
            return JsonError('pci not found: {0}'.format( cBase.viewCode ))
            
        protoDef = ViewDefinition.objects.get(code=cBase.viewCode)
        protoDef.save()
        created = True  
        

    if ( not protoDef.active ) :
        return JsonError('inactive pci : {0}'.format( cBase.viewCode ))


    # Si la directiva es reescribirlo es como si fuera nuevo cada vez y si es nuevo lee Django
    if protoDef.overWrite : created = True
    if created and ( not readOnly )   :
        cBase.model_admin, cBase.protoMeta = getProtoAdmin(cBase.model)

        # Genera la definicion de la vista 
        grid = ProtoGridFactory( cBase )
        if not createProtoMeta( cBase , grid ) : 
            return JsonError('Document type required: {0}.???'.format( cBase.viewCode ))
    
        # Guarda o refresca la Meta y mantiene la directiva overWrite
        protoDef.metaDefinition = cBase.protoMeta
        protoDef.description = cBase.protoMeta['description'] 
        protoDef.save()    


    else:
        cBase.protoMeta = protoDef.metaDefinition
        cBase.protoMeta['viewCode'] = cBase.viewCode  

    return 


def verifyMeta( cBase , pciType ): 
    """
    FUTURE: verifyMeta
    """


    # TODO: Add setDefault Action 
    if pciType == 'pci': 

        ACTION_NAME =  "doSetDefaults"
        if cBase.protoMeta.get( 'defaultTo', []): 

            actionFound = False 
            lActions = cBase.protoMeta.get( 'actions', [])
            for lAction in lActions:
                if lAction.get( 'name') == ACTION_NAME: 
                    actionFound = True
                    break

            if not actionFound: 
                lActions.append( { "name": ACTION_NAME, "selectionMode" : "optional"} )


    return cBase.protoMeta

