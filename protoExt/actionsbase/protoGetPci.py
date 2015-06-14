# -*- coding: utf-8 -*-

from django.http import HttpResponse

from django.db.models import Max

from .protoGrid import getBaseModelName, setDefaultField , getProtoAdmin
from .protoGrid import ProtoGridFactory
from .protoField import setFieldDict, isAdmField 
from protoExt.models import ViewDefinition, CustomDefinition 

from protoLib.getmodels import getDjangoModel, getUserProfile, getModelPermission, getAllModelPermissions

from protoExt.utils.utilsBase import getReadableError
from protoExt.utils.utilsWeb import JsonError, JsonSuccess 

from .protoQbe import getSearcheableFields


try:
    from prototype.models import Prototype, Entity
    installedProto = True 
except:
    installedProto = False 



PROTO_PREFIX = "prototype.ProtoTable."

# TODO: 
# from protoLib.protoPci import verifyMeta 

# import django.utils.simplejson as json
import json
import traceback


# 12/10/28 Permite la carga directa de json de definicion. 
PROTOVERSION = '130310'


def protoGetPCI(request):
    """ return full metadata (columns, renderers, totalcount...)
    """

    if not request.user.is_authenticated(): 
        return JsonError('readOnly User')
    
    if request.method != 'POST':
        return JsonError('invalid message') 
    
    viewCode = request.POST.get('viewCode', '') 
    viewEntity = getBaseModelName(viewCode)
    
    try: 
        model = getDjangoModel(viewEntity)
    except :
        return JsonError('model not found: {0}'.format( viewEntity)) 
    
    # 
    userProfile = getUserProfile(request.user) 


    # PROTOTIPOS
    isPrototype = False 
    if viewCode.startswith(PROTO_PREFIX)  and viewCode != viewEntity :
        try:
            prototypeView = viewCode.replace(PROTO_PREFIX, '')
            protoDef = Prototype.objects.get(code=prototypeView, smOwningTeam=userProfile.userTeam)
            created = False   
            isPrototype = True 
            
        except:
            return JsonError('prototype not found: {0}'.format( viewCode ))

    else:
        # protoDef : PCI leida de la DB ; created : El objeto es nuevo
        protoDef, created = ViewDefinition.objects.get_or_create(code=viewCode)


    if ( not isPrototype ) :
        # if ( not protoDef.active) :
        #     return JsonError('Inactive definition : {0}'.format( viewCode ))

        if protoDef.overWrite :
            # Si la directiva es reescribirlo es como si fuera nuevo cada vez 
            created = True 


    # Si es nuevo lee Django 
    if created  :

        model_admin, protoMeta = getProtoAdmin(model)

        # Genera la definicion de la vista 
        grid = ProtoGridFactory(model, viewCode, model_admin, protoMeta)
        if not createProtoMeta(model, grid, viewEntity, viewCode) : 
            return JsonError('Document type required: {0}.???'.format( viewCode ))
    
        # Guarda o refresca la Meta y mantiene la directiva overWrite
        protoDef.metaDefinition = json.dumps(grid.protoMeta) 
        protoDef.description = protoMeta['description'] 
        protoDef.save()    


    else:
        protoMeta = json.loads(protoDef.metaDefinition) 
        protoMeta['viewCode'] = viewCode  



    # La definicion del arbol es fija, pues las cols deben ser siempre uniformes sin importar el tipo de modelo.
#    pStyle = protoMeta.get( 'pciStyle', '')      
#    if pStyle == 'tree':  setTreeDefinition()


    customCode = '_custom.' + viewCode 
    try:
        custom = CustomDefinition.objects.get(code=customCode, smOwningTeam=userProfile.userTeam)
        custom = json.loads(custom.metaDefinition)
        protoMeta['custom'] = custom['custom']  
    except:
        pass
    
    # TODO: Verificacion de la metadata 
#     try:
#         protoMeta = verifyMeta(protoMeta, 'pcl')
#     except Exception, e:
#         traceback.print_exc()    
#         message = getReadableError(e)


    # WorkFlow  
    if hasattr(model , '_WorkFlow') : 
        wflowControl = getattr(model, '_WorkFlow', {})

        if request.user.is_superuser  or getModelPermission(request.user , model, 'wfadmin') :
            protoMeta['WFlowActions'] = wflowControl.get('transitions', []) 

        wfFilterSet = wflowControl.get('wfFilters', []) 
        if len(wfFilterSet) > 0: 
            protoMeta['gridSets'] = protoMeta.get('gridSets', {})
            protoMeta['gridSets']['filtersSet'] = wfFilterSet
            for lFilter in wfFilterSet:
                lFilter['customFilter'] = [{
                            "property": "smWflowStatus",
                            "filterStmt": lFilter[ 'wfStatus']
                }]

    jsondict = {
        'success':True,
        'message': '',
        'metaData':{
            # The name of the property which contains the Array of row objects. ...
            'root': 'rows',

            # Name of the property within a row object that contains a record identifier value. ...
            'idProperty': protoMeta['idProperty'],

            # Name of the property from which to retrieve the total number of records in t
            'totalProperty':'totalCount',

            # Name of the property from which to retrieve the success attribute. ...
            'successProperty':'success',
            
            # The name of the property which contains a response message. (optional)
            'messageProperty': 'message',
            },
        'protoMeta': protoMeta,
        'permissions': getAllModelPermissions(request.user, model),
        
        'rows':[],
        'totalCount': 0,
    }
    
    # Codifica el mssage json 
    context = json.dumps(jsondict)
    return HttpResponse(context, content_type="application/json")

            


# protoGetPCI ----------------------------


def createProtoMeta(model, grid, viewEntity , viewCode):

    # Los criterios de busqueda ni los ordenamientos son heredados del admin, 
    pSearchFields = grid.gridConfig.get('searchFields', []) 
    if len(pSearchFields) == 0:
        pSearchFields = getSearcheableFields(model)

    pSortFields = grid.gridConfig.get('sortFields', []) 
    if len(pSortFields) == 0:
        pSortFields = getSearcheableFields(model)

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

             'hiddenFields': grid.protoMeta.get('hiddenFields', ['id', ]),
         } 

    #---------- Ahora las propiedades generales de la PCI 
    viewIcon = grid.protoMeta.get('viewIcon', 'icon-1') 

    pDescription = grid.protoMeta.get('description', '')
    if len(pDescription) == 0:
        pDescription = grid.protoMeta.get('title', grid.title)
    
    # FIX: busca el id en la META  ( id_field = model._meta.pk.name ) 
    id_field = u'id'
    shortTitle = grid.protoMeta.get('shortTitle', grid.title),

    # Manejo de documentos rai          
    if getattr(model, '_uddObject', False ):
        dBase = getattr(model, '_jDefValueDoc', False )    
        idType = ''

        try: 
            idType =  viewCode.split('.')[2] 
        except: pass 
            # return False 


        # TODO : Los hijos deben ser del mismo tipo, o deben eliminarse 

        if len( dBase ) > 0 and len( idType ) > 0:

            docFields, shortTitle  = model.getJfields( idType )

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
         'viewCode' : viewCode,
         'viewEntity' : viewEntity,
         'idProperty': grid.protoMeta.get('idProperty', id_field),
         'shortTitle': shortTitle,
         'description': pDescription ,
         'viewIcon': viewIcon,

         'fields': grid.fields,
         'gridConfig' : gridConfig,
         'gridSets': grid.protoMeta.get('gridSets', {}),

         'detailsConfig': grid.get_details() ,
         'formConfig': grid.getFieldSets(),

#        El resto  no las carga pues ya estan en la meta ... 
         }
    

    grid.protoMeta.update( protoTmp ) 
    return True 
    

# ------------------------------------------------------------------------


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


def protoGetFieldTree(request):
    """ return full field tree 
    """

    if request.method != 'POST':
        return JsonError('Invalid message') 
    
    viewCode = request.POST.get('viewCode', '') 
    viewEntity = getBaseModelName(viewCode)
    
    try: 
        model = getDjangoModel(viewEntity)
    except Exception as e:
        return JsonError(getReadableError(e)) 
    
    fieldList = []
    if viewCode.startswith(PROTO_PREFIX) and viewCode != viewEntity :
        # ---------------------------------------------------              Prototipos 
        protoEntityId = request.POST.get('protoEntityId')
        if not protoEntityId >= 0:
            return JsonError('invalid idEntity')

        try:  
            from prototype.actions.viewDefinition import GetProtoFieldsTree
            fieldList = GetProtoFieldsTree(protoEntityId)
        except: 
            return JsonError('invalid idEntity')

    else: 
        # -----------------------------------------------------------------------------------------------------
        # Se crean los campos con base al modelo ( trae todos los campos del modelo 
        # for field in model._meta._fields(): # only for django 1.4
        for field in model._meta.fields:
            try: 
                addFiedToList(fieldList, field , '')
            except Exception as  e:
                traceback.print_exc()
                return JsonError(getReadableError(e)) 
            
        # Add __str__ 
        myField = { 
            'id'        : '__str__' ,
            'text'      : '__str__' ,
            'checked'   : False,
            'leaf'      : True 
         }
        
        # Defaults values
        setDefaultField(myField, model , viewCode)
        
        # FormLink redefinition to original view 
        # myField['zoomModel'] =  viewCode  
        
        fieldList.append(myField)

    # Codifica el mssage json 
    context = json.dumps(fieldList)
    return HttpResponse(context, content_type="application/json")



def addFiedToList(fieldList , field, fieldBase):
    """ return parcial field tree  ( Called from protoGetFieldTree ) 
    """

    fieldId = fieldBase + field.name

    # DEfinicion proveniente del dict ( setFieldDict )  
    protoFields = {}
    setFieldDict (protoFields , field)
    pField = protoFields[ field.name ]
    
    # fieldBase indica campos de llaves foraneas       
    if fieldBase != '': 
        # Los campos heredados son siempre ro y no requeridos  
        pField[ 'readOnly' ] = True 
        pField['required'] = False 
        if pField['type'] == 'autofield':
            pField['type'] = 'int'

    pField['id'] = fieldId
    pField['text'] = field.name

    pField['leaf'] = True
    pField['checked'] = False

    # Recursividad Fk 
    if pField['type'] != 'foreigntext':
        pass 

    # no se requiere profundizar en los campos de seguridad ( usr, ... )   
    elif isAdmField(field.name): 
        pass 

    # Evita demasiada recursividad ( 5 niveles debe ser mas q suficiente ) 
    elif fieldId.count('__') > 3:   
        pass 

    else:  

        # si es base, Agrega el campo id del zoom   
        # en los campos heredados no se hace zoom ( no se requiere el id )   
        if (fieldBase == '') :  

            # Obtiene el fkId del diccionario  
            pFieldId = protoFields[ pField['fkId'] ]

            pFieldId['id'] = pFieldId['name']
            pFieldId['text'] = pFieldId['name']  
            pFieldId['required'] = pField.get('required', False)   

            pFieldId['leaf'] = True
            pFieldId['checked'] = False
    
            fieldList.append(pFieldId)

        # itera sobre el campo para heredar de sus padres  
        fkFieldList = []
        model = field.rel.to
        # for fAux in model._meta._fields(): #django 1.4
        for fAux in model._meta.fields:
            # los id de los campos heredados tampoco se presentan 
            if fAux.name == 'id' :
                continue 
            
            # los campos adm de los heredados no se presentan  
            if isAdmField(fAux.name):
                continue 
            
            addFiedToList(fkFieldList, fAux , fieldId + '__')

        pField['leaf'] = False 
        pField['children'] = fkFieldList
    
    fieldList.append(pField)


# --------------------------------------------------------------------------

def isFieldDefined(pFields , fName):
    # Verifica si un campo esta en la lista 
    for pField  in pFields:
        if pField.get('name') == fName: 
            return True 
    return False 

def getFieldIncrement(request):
    success = False
    fieldName = request.GET['fieldName']
    viewEntity = request.GET['viewEntity']
    try: 
        model = getDjangoModel(viewEntity)
    except :
        return JsonError('model not found:' + viewEntity)
    
    fieldType = model._meta.get_field(fieldName).get_internal_type()
    increment = 0
    if fieldType == 'IntegerField':
        maxid = model.objects.aggregate(Max('id'))
        if maxid['id__max']:
            increment = maxid['id__max'] + 1
        else:
            increment = 1
    else:
        return JsonError('Invalid field type')
    
    if increment > 0:
        success = True
        
    jsondict = {
        'success': success,
        'increment': increment
    }
    
    json_data = json.dumps(jsondict)
    return HttpResponse(json_data, content_type="application/json")
