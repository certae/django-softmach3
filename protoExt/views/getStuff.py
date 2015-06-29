'''
Created on Jun 21, 2015

@author: dario
'''

from protoExt.utils.utilsBase import list2dict

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
            

    return vFld 



def setContextFilter( cBase ):
    """
    Define los filtros contextuales 
    """

    cBase.contextFilter = [] 

    userContext = getContext(cBase)
    if len( userContext ) == 0: return 

    for lField in userContext:
        if not lField[ 'isFilter' ]: continue 

        cBase.contextFilter.append( { 
            'property': lField['property'], 
            'filterStmt' : '=%s' % lField.get( 'propValue' )   
        } )
        

def getParameter(paramKey, default):

    jAux  = {'parameterValue' : parameterValue, }

    from protoExt.models import Parameters 
    param  = Parameters.objects.get_or_create(parameterKey = paramKey , defaults = jAux )[0]
    
    return param.parameterValue 
