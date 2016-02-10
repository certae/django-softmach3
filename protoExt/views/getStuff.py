'''
Created on Jun 21, 2015

@author: dario
'''

from protoExt.utils.utilsBase import list2dict
from protoLib.models.versions import VersionUser


def getContext( cBase ):
    """
    Lee el contexto de customDefinition  
    """
    
    from protoExt.models import CustomDefinition
    viewCode = '_context.%s' % cBase.viewEntity.lower()

    try: 
        protoDef = CustomDefinition.objects.get(
               code = viewCode, 
               smOwningUser = cBase.userProfile.user  
               )
    
        return protoDef.metaDefinition 

    except: 
        return []


def setContextDefaults( cBase ):
    """
    Define los defaults sobre la meta   
    """

    userContext = getContext(cBase)
    if len( userContext ) == 0: return 

    cBase.fieldsDict = list2dict(cBase.protoMeta[ 'fields' ], 'name')

    for lField in userContext:
        if not lField[ 'isDefault' ]: continue 
        
        lName = lField[ 'property' ]
        vFld = cBase.fieldsDict.get( lName ) 
        if not vFld: continue  
        
        vFld['prpDefault'] = lField.get( 'propValue' ) 
        
        if lName.endswith('_id'):
            lName = lName[:-3]
            vFld = cBase.fieldsDict.get( lName ) 
            if not vFld: continue
              
            vFld['prpDefault'] = lField.get( 'propDescription' ) 
            


def setContextFilter( cBase ):
    """
    Define los filtros contextuales 
    """

    userContext = getContext(cBase)
    if len( userContext ) == 0: return 

    for lField in userContext:
        if not lField[ 'isFilter' ]: continue 

        cBase.contextFilter.append( { 
            'property': lField['property'], 
            'filterStmt' : '=%s' % lField.get( 'propValue' )   
        } )


def getCurrentVersion( cBase ):
     
    # Version Allow
    try:
        cBase.model._meta.get_field('smVersion')
    except:
        cBase.cVersion = None 
        return 

    #  Active user version 
    try: 
        cVersion = VersionUser.objects.get(
               user = cBase.userProfile.user, 
               active = True   
               )
    except: 
        cBase.cVersion = '0' 
        return  


    cBase.cVersion = cVersion.version 



def setVersionFilter( cBase ): 

    getCurrentVersion( cBase )
    if not cBase.cVersion is None: 

        cBase.contextFilter.append( { 
            'property': 'smVersion', 
            'filterStmt' : '=%s' % cBase.cVersion   
        } )
        


def getParameter(paramKey, default):

    jAux  = {'parameterValue' : default, }

    from protoExt.models import Parameters 
    param  = Parameters.objects.get_or_create(parameterKey = paramKey , defaults = jAux )[0]
    
    return param.parameterValue 


