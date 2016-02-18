'''
Created on Jun 21, 2015

@author: dario
'''

from protoExt.utils.utilsBase import list2dict


def getContextEntity( cBase ):
    """
    get context filter by entity 
    """
    
    cttArray = []

    from protoExt.models import ContextEntity, ContextUser
    modelCType = ContentType.objects.get_for_model( cBase.model ) 

    cEntities = ContextEntity.objects.filter(
               contextVar__modelCType = modelCType, 
               active = True 
           )
    
    for cEnt in cEntities:
        cVars = ContextUser.objects.filter(
                    contextVar  = cEnt.contextVar, 
                    smOwningUser = cBase.userProfile.user, 
                    active = True 
               )

        for cVar in cVars:
            cttArray.append( {
                'property' = cEnt.propName, 
                'propValue' = cVar.propValue 
                })


    return cttArray



def setContextDefaults( cBase ):
    """
    set Meta context defaults  
    """

    cttArray = getContextEntity(cBase)
    if len( cttArray ) == 0: return 

    cBase.fieldsDict = list2dict(cBase.protoMeta[ 'fields' ], 'name')

    for lField in cttArray:

        # If parent property continue 
        if  len( lField[ 'property' ].split('__')) > 0  : continue 
        
        lName = lField[ 'property' ]
        vFld = cBase.fieldsDict.get( lName ) 
        if not vFld: continue  
        
        vFld['prpDefault'] = lField.get( 'propValue' ) 

        # If Fk, set _str__  
        # if lName.endswith('_id'):
        #     lName = lName[:-3]
        #     vFld = cBase.fieldsDict.get( lName ) 
        #     if not vFld: continue
        #     vFld['prpDefault'] = lField.get( 'propDescription' ) 
            


def setContextFilter( cBase ):
    """
    set meta context filters 
    """

    cttArray = getContextEntity(cBase)
    if len( cttArray ) == 0: return 

    for lField in cttArray:
        cBase.contextFilter.append( { 
            'property': lField['property'], 
            'filterStmt' : '=%s' % lField.get( 'propValue' )   
        } )

       


def getParameter(paramKey, default):

    jAux  = {'parameterValue' : default, }

    from protoExt.models import Parameters 
    param  = Parameters.objects.get_or_create(parameterKey = paramKey , defaults = jAux )[0]
    
    return param.parameterValue 


