# -*- coding: utf-8 -*-

"""
ProtoGetPci 
"""

import traceback

from django.http import HttpResponse

from protoExt.models import ViewDefinition, CustomDefinition 
from protoLib.getStuff import getDjangoModel, getProtoAdmin 
from protoExt.utils.utilsWeb import JsonError 

from . import getReturnMsg, validateRequest 
from .protoQbe import getSearcheableFields
from .protoGrid import ProtoGridFactory 


# 12/10/28 Permite la carga directa de json de definicion. 
PROTOVERSION = '130310'


def protoGetPCI(request):
    """ 
    Return full metadata (columns, renderers, totalcount...)
    """

    cBase, msgError = validateRequest( request )
    if msgError: return msgError  
    
    try: 
        cBase.model = getDjangoModel(cBase.viewEntity)
    except :
        return JsonError('model not found: {0}'.format( cBase.viewEntity )) 
    

    # =============  PROTOTIPOS
    from .prototypeActions import isProtoPci, getProtoPci 
    if isProtoPci( cBase ): 
        return getProtoPci( cBase )



    # =============  Obtiene o fabrica la pci 
    # protoDef : PCI leida de la DB ; created : El objeto es nuevo
    protoDef, created = ViewDefinition.objects.get_or_create(code=cBase.viewCode)

    if ( not protoDef.active) :
        return JsonError('Inactive definition : {0}'.format( cBase.viewCode ))


    # Si la directiva es reescribirlo es como si fuera nuevo cada vez y si es nuevo lee Django
    if protoDef.overWrite : created = True
    if created  :
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


#   ============  Collecciones personalizables  y elementos particulares 
    customCode = '_custom.' + cBase.viewCode 
    try:
        custom = CustomDefinition.objects.get(code=customCode, smOwningTeam= cBase.userProfile.userTeam)
        cBase.protoMeta['custom'] = custom.metaDefinition
    except:
        pass

    #TODO:  addWfParameters( cBase  )

    
#   ============== Verificacion de la metadata 
    try:
        cBase.protoMeta = verifyMeta( cBase , 'pci')
    except Exception:
        traceback.print_exc()    
        return JsonError('invalid definition: {0}'.format( cBase.viewEntity )) 


    context =  getReturnMsg( cBase  )
    return HttpResponse(context, content_type="application/json")


# protoGetPCI ----------------------------


def createProtoMeta( cBase, grid ):

    # Los criterios de busqueda ni los ordenamientos son heredados del admin, 
    pSearchFields = grid.gridConfig.get('searchFields', []) 
    if len(pSearchFields) == 0:
        pSearchFields = getSearcheableFields(cBase.model)

    pSortFields = grid.gridConfig.get('sortFields', []) 
    if len(pSortFields) == 0:
        pSortFields = getSearcheableFields(cBase.model)

    # Lista de campos precedidos con '-' para order desc  ( 'campo1' , '-campo2' )
    # * o [{ "property": "code", "direction": "ASC" }, {  
    initialSort = grid.gridConfig.get('initialSort', ())
    sortInfo = []
    for sField in initialSort:
        # Si es un string lo convierte en objeto 
        if type(sField).__name__ == type('').__name__ :  
            sortOrder = 'ASC'
            if sField[0] == '-':
                sortOrder = 'DESC'
                sField = sField[1:]
            sField = { 'property': sField, 'direction' : sortOrder }
            
        sortInfo.append(sField)


    # ----------- Completa las propiedades del gridConfig 
    gridConfig = { 
             'searchFields': pSearchFields,
             'sortFields': pSortFields,
             'initialSort': sortInfo,

             # Si no es autoload  -  '{"pk" : 0,}'            
             'baseFilter': grid.gridConfig.get('baseFilter', []),
             'initialFilter': grid.gridConfig.get('initialFilter', []),

             # Toma las definidas en la grilla 
             'listDisplay' : grid.gridConfig.get('listDisplay', []),
             'readOnlyFields' : grid.gridConfig.get('readOnlyFields', []),
             
             # Garantiza q existan en la definicion 
             'hideRowNumbers' : grid.gridConfig.get('hideRowNumbers', False),
             'filterSetABC': grid.gridConfig.get('filterSetABC', ''),

             'hiddenFields': cBase.protoMeta.get('hiddenFields', ['id', ]),
         } 

    #---------- Ahora las propiedades generales de la PCI 
    viewIcon = cBase.protoMeta.get('viewIcon', 'icon-1') 

    pDescription = cBase.protoMeta.get('description', '')
    if len(pDescription) == 0:
        pDescription = cBase.protoMeta.get('title', grid.title)
    
    # FIX: busca el id en la META  ( id_field = cBase.model._meta.pk.name ) 
    id_field = u'id'
    shortTitle = cBase.protoMeta.get('shortTitle', grid.title),

    # Manejo de documentos rai          
    if getattr(cBase.model, '_uddObject', False ):
        dBase = getattr(cBase.model, '_jDefValueDoc', False )    
        idType = ''

        try: 
            idType =  cBase.viewCode.split('.')[2] 
        except: pass 
            # return False 


        # TODO : Los hijos deben ser del mismo tipo, o deben eliminarse 

        if len( dBase ) > 0 and len( idType ) > 0:

            docFields, shortTitle  = cBase.model.getJfields( idType )

            gridConfig['baseFilter'].append( { 'property':'docType', 'filterStmt' : '=' + idType  } )

            grid.fieldsDict['docType_id']['prpDefault'] = idType 

            grid.fieldsDict['docType']['prpDefault'] = shortTitle 
            grid.fieldsDict['docType']['readOnly'] = True
            grid.fieldsDict['docType']['hidden'] = True

            grid.fieldsDict.update( docFields )

            pDescription = '{0}: {1}'.format( dBase, shortTitle ).lower()
            grid.fields = []
            for lField in grid.fieldsDict.itervalues():
                grid.fields.append( lField )


    protoTmp = { 
         'metaVersion' : PROTOVERSION ,
         'viewCode' : cBase.viewCode,
         'viewEntity' : cBase.viewEntity,
         'idProperty': cBase.protoMeta.get('idProperty', id_field),
         'shortTitle': shortTitle,
         'description': pDescription ,
         'viewIcon': viewIcon,

         'fields': grid.fields,
         'gridConfig' : gridConfig,
         'gridSets': cBase.protoMeta.get('gridSets', {}),

         'detailsConfig': grid.get_details() ,
         'formConfig': grid.getFieldSets(),

#        El resto  no las carga pues ya estan en la meta ... 
         }
    

    cBase.protoMeta.update( protoTmp ) 
    return True 
    

# --------------------------------------------------------------------------

def isFieldDefined(pFields , fName):
    # Verifica si un campo esta en la lista 
    for pField  in pFields:
        if pField.get('name') == fName: 
            return True 
    return False 


def verifyMeta( cBase , pciType ): 
    # TODO: verifyMeta
    return cBase.protoMeta

