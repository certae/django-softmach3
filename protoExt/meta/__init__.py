# -*- coding: utf-8 -*-
from protoExt.utils.utilsBase import verifyList, random_string_generator
from .metaObjects import META_OBJECTS
from .metaProperties import META_PROPERTIES 


def verifyMeta( oMeta, ptType, tNode = None ): 
    """
    oMeta : Objeto a verificar 
    ptType : definicion del tipo de objeto 
    tNode : arbol extJs  

    verifyMeta : Verifica un objeto de acuerdo a la estructura
    Si es un objeto asociado a un arbol tNode es el de base,
    """


    msgError = ''

    ptConfig = META_OBJECTS.get( ptType, None ) 
    if not ptConfig : 
        msgError += 'invalid META key %s \n' % ( ptType, )
        return oMeta


    # Verifica las listas
    if  ptConfig.get( 'lists' ) :
        for sKey in ptConfig['lists'] :

            if type(sKey).__name__ != 'str' :
                msgError += 'invalid list key %s \n' % ( sKey, )
                continue

            listOfConf = META_OBJECTS.get( sKey, None) 
            if not listOfConf : 
                msgError += 'invalid META key %s \n' % ( sKey, )
                continue 

            # Se asegura q se una lista y asigna las propiedades por defecto 
            oMeta[sKey] = verifyList( oMeta.get( sKey, []), listOfConf.get( 'listDefault', []) )

            # agrega una nueva lista al arbol
            if (tNode) :
                nBranch = {
                    'text' : sKey,
                    '__ptType' : sKey,
                    '__ptConfig' : {
                        '__ptType' : sKey
                    },
                    'children' : []
                }

                tNode.get('children', []).append(nBranch)

    # Verifica los Objetos ( no aplica los default, pues la config puede eliminarlos )
    if  ptConfig.get( 'objects' ) :
        for sKey in ptConfig['objects'] :

            if type(sKey).__name__ != 'str' :
                msgError += 'invalid object key %s \n' % ( sKey, )
                continue

            myObj = oMeta.get( sKey, {} )

            # agrega un nuevo objeto al arbol
            if tNode :
                nBranch = getNodeBase(sKey, sKey, {'__ptType' : sKey})
                tNode.get('children', []).append(nBranch)

                # Agrega los hijos tambein al arbol; la creacion del arbol no es recursiva 
                oMeta[sKey] = verifyMeta(myObj, sKey, nBranch)[0]

            else:
                oMeta[sKey] = verifyMeta(myObj, sKey)[0]


    return oMeta, tNode 



def clearPhantonProps( ptConfig, ptType) :
    """
    Borra las propieades q no hacen parte de la config de base
    """
     
    objConfig = META_OBJECTS.get( ptType,  [] )
    if not objConfig.get( 'properties') :return
     
    for sKey in ptConfig.keys() :
        if not sKey in objConfig.properties + ['name', '__ptValue', '__ptList', 'ptType'] :
            del ptConfig[ sKey ]

    return ptConfig


def addDefaultActions( cBase  ): 

    # Add setContext Action 
    ACTION_NAME =  "doSetContext"
    if cBase.protoMeta.get( 'contextTo', []): 

        actionFound = False 
        lActions = cBase.protoMeta.get( 'actions', [])
        for lAction in lActions:
            if lAction.get( 'name') == ACTION_NAME: 
                actionFound = True
                break

        if not actionFound: 
            lActions.append( { "name": ACTION_NAME, "selectionMode" : "optional"} )


def getNodeBase(pName, ptType, __ptConfig):
    """
    Obtiene un Id y genera  una referencia cruzada de la pcl con el arbol
    El modelo debe crear la referencia a la data o se perdera en el treeStore
    """
    
    global root, index 
    if not root: 
        root = random_string_generator()
        index = 0 
    index += 1 
        
    return {
        'id' : '%s-%s' % (root, str( index ) ),
        'text' : pName,
        '__ptType' : ptType,
        '__ptConfig' : __ptConfig,
        'children' : []
    }
