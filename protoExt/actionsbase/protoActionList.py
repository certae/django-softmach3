# -*- coding: utf-8 -*-


from django.db import models
from django.utils import six 
from django.http import HttpResponse
from django.contrib.admin.utils import  get_fields_from_path
from django.utils.encoding import smart_str
from django.db.models import Q

from protoExt.utils.utilsBase import JSONEncoder, getReadableError
from protoExt.utils.utilsBase import verifyStr, verifyList, list2dict
from protoExt.utils.utilsConvert import getTypedValue

from .protoQbe import getSearcheableFields, getQbeStmt
from protoLib.getStuff import  getModelPermission, getRowById

from .protoField import TypeEquivalence

from protoLib.getStuff import getDjangoModel
from protoExt.utils.utilsWeb import JsonError 
from protoExt.models import ViewDefinition 

from . import validateRequest 

import json
import traceback


def protoList(request):
#   Vista simple para cargar la informacion,

    PAGESIZE = 50
    message = ''

    cBase, msgError = validateRequest( request )
    if msgError: return msgError  
    
    # Lee la pci      
    try:
        protoDef = ViewDefinition.objects.get( code = cBase.viewCode )
        cBase.protoMeta = protoDef.metaDefinition
    except Exception as e :
        return JsonError('ViewDefinition not found: {0}'.format( cBase.viewCode  )) 

#   Parametros de la consulta 
    cBase.protoFilter = request.POST.get('protoFilter', '')
    cBase.baseFilter = request.POST.get('baseFilter', '')
    cBase.sort = request.POST.get('sort', '')

    cBase.start = int(request.POST.get('start', 0))
    cBase.page = int(request.POST.get('page', 1))
    cBase.limit = int(request.POST.get('limit', PAGESIZE))
#   Fix: Cuando esta en la pagina el filtro continua en la pagina 2 y no muestra nada.
#   if ( ( cBase.page -1 ) *cBase.limit >= pRowsCount ): cBase.page = 1

    cBase.jsonLookups = [] 
    cBase.jsonSorters = [] 
    

#   Obtiene las filas del cBase.modelo
    Qs = getQSet( cBase )

    try:
        pRows = Qs.order_by(*cBase.orderBy)[ cBase.start: cBase.page * cBase.limit ]
    except:
        pRows = Qs.all()[ cBase.start: cBase.page * cBase.limit ]

#   Asegura la carga 
    cBase.regCount = pRows.count()      

    if cBase.jsonLookups: 
        pass 

#   Prepara las cols del Query
    try:
        pList = Q2Dict(cBase , pRows  )
        bResult = True
    except Exception as e:
        traceback.print_exc()
        message = getReadableError(e)
        bResult = False
        pList = []


    context = json.dumps({
            'success': bResult,
            'message': message,
            'totalCount': len( pList ),
            'filter': cBase.protoFilter,
            'rows': pList,
        }, cls=JSONEncoder)


    return HttpResponse(context, content_type="application/json")


def getQSet( cBase ):
    """
    Get QuerySet, order_by, isFakeId 

    """
    cBase.viewEntity = cBase.protoMeta.get('viewEntity', '')
    cBase.model = getDjangoModel(cBase.viewEntity)

    cBase.isProtoModel = hasattr( cBase.model , '_protoObj')
    cBase.isPJsonModel = hasattr(cBase.model , '_protoJson')
    cBase.jsonField = cBase.protoMeta.get('jsonField', '')
    if cBase.isPJsonModel: cBase.jsonField = 'smInfo' 
    
    cBase.fakeId = hasattr(cBase.model , '_fakeId')
    cBase.orderBy = []
    # pStyle = cBase.protoMeta.get( 'pciStyle', '')


#   Autentica '
    if not getModelPermission( cBase.userProfile.user, cBase.model, 'list'):
        return cBase.model.objects.none()

#   Usa el manager de base 
    if cBase.isProtoModel:
        Qs = cBase.model.smObjects
    else: Qs = cBase.model.objects

#   El filtro base viene en la configuracion MD
    try:
        Qs = addQbeFilter(cBase, Qs)
    except Exception as e:
        traceback.print_exc()
        getReadableError(e)


#   Order by
    localSort = cBase.protoMeta.get('localSort', False)
    if not localSort :
        cBase.sort = verifyList(cBase.sort)
        for sField in cBase.sort:

            sName = sField['property']
            if cBase.isProtoModel:

                # Permite el ordenamiento sobre la funcion de presentacion 
                if sName == '__str__': 
                    sName = 'smNaturalCode'
                
                # Permite el ordenamiento sobre maestros e impide sobre jsofield 
                elif sName.split('__')[0] in ['smInfo', cBase.jsonField] : 
                    cBase.jsonSorters.append( sField )
                    continue  

            # __str__ is not sortable 
            if sName == '__str__': continue
    

            if sField['direction'] == 'DESC': sName = '-' + sName
            cBase.orderBy.append(sName)

    cBase.orderBy = tuple(cBase.orderBy)

    return Qs


def Q2Dict ( cBase, pRows, userNodes=[]):
    """
    return the row list from given queryset
    """

    rows = []
    relModels = {}      # Tablas de zoom para absorcion de campos

    # cBase.udpFields = [] 

    # Alimenta la coleccion de zooms, por cada campo pues hay q hacer un select para esto
    for lField  in cBase.protoMeta['fields']:
        fName = lField['name']
        myZoomModel = lField.get('zoomModel', '')
        if (len(myZoomModel) > 0) and (myZoomModel != cBase.protoMeta['viewEntity']):
            relModels[ fName ] = { 'zoomModel' : myZoomModel, 'fkId' : lField.get('fkId', '') , 'loaded' : False }


    # Verifica si existen reemplazos por hacer ( cpFromField )
    # 1.  Marca los zooms q estan referenciados
    bCopyFromFld = False
    for lField  in cBase.protoMeta['fields']:
        fName = lField['name']
        if (lField.get('cpFromField') is None or lField.get('cpFromZoom') is None): continue

        bCopyFromFld = True
        lField[ 'isAbsorbed' ] = True

        # Marca el zoom
        try:
            relModel = relModels[ lField.get('cpFromZoom') ]
            relModel[ 'loaded'] = True
        except: 
            pass


    # 2.  borra los q no tienen marca
    lAux = list( relModels.keys() )
    for relName in lAux:
        relModel = relModels[ relName ]
        if not relModel[ 'loaded']: 
            del relModels[ relName ]


    #   Esta forma permite agregar las funciones entre ellas el __unicode__
    rowId = 0
    for rowData in pRows:
        rowId += 1
        rowdict = {}

        # limpia los datos de tablas relacionadas
        for relName in relModels:
            relModel = relModels[ relName ]
            relModel[ 'rowData'] = {}
            relModel[ 'loaded'] = False

        # recorre los campos para obtener su valor
        for lField  in cBase.protoMeta['fields']:
            fName = lField['name']
            pName = lField.get('physicalName', fName)

            if lField.get('crudType') == "screenOnly" : 
                continue

            elif (lField['type'] == 'protoN2N'):
                continue

            # Si el campo es absorbido ( bCopyFromFld es un shortcut para evitar la evulacion en caso de q no haya ningun cpFromField )
            elif bCopyFromFld and (lField.get('isAbsorbed', False)) :
                continue

            rowdict[ fName ] = getFieldValue(pName, lField[ 'type'], rowData, cBase )



        # Realiza la absorcion de datos provenientes de un zoom
        if bCopyFromFld:
            rowdict = copyValuesFromFields(cBase , rowdict, relModels )

        # Dont delete  ( Dgt ) 
        # if pStyle == 'tree':
        #    rowdict[ 'viewEntity' ] = cBase.protoMeta.get('viewEntity', '')
        #    rowdict[ 'leaf' ] = False; rowdict[ 'children' ] = []

        # Agrega el Id Siempre como idInterno ( no representa una col, idProperty )
        rowdict[ 'id'] = rowData.pk
        if cBase.fakeId: rowdict[ 'id'] = rowId


        # Agrega la fila al diccionario
        rows.append(rowdict)


    return rows


def copyValuesFromFields( cBase, rowdict, relModels ):
    """
    Permite copiar campos q vienen de los zooms,
    En el caso de prototipos hace un select a la instancia relacionada
    """

    for lField  in cBase.protoMeta['fields']:
        cpFromField = lField.get('cpFromField')
        if not cpFromField: continue

        fName = smart_str(lField['name'])
        cpFromField = smart_str(cpFromField)

        if not lField.get('isAbsorbed', False):
            # Es un copy q puede ser resuelto a partir del cBase.modelo objeto
            # esta es la situacion normal cuando no se idetifica un cBase.modelo y se cargan los datos por jerarquia
            # por ahora requiere q el campo este tambien en el cBase.modelo ( se puede cambiar si hay la necesidad )

            # Se uso para copiar cosas de discretas,  debia poner por defecto el vr en el campo
            # Si ya contiene algun valor, sale, solo copia cuando es nulo.
            val = rowdict.get(fName, None)
            if (val) and smart_str(val).__len__() > 0: 
                continue

            val = rowdict.get(cpFromField , None)
            if (val is None) : 
                val = ''

        else:
            # Esta es la situacion de los prototipos q requieren el cpFromZoom,
            # se hace un select adicional para obtner el registro relacionado

            cpFromZoom = lField.get('cpFromZoom')

            try:
                relModel = relModels[ cpFromZoom ]
            except:
                # para envitar volverlo a leer, si son varios campos del mismo registro
                relModel = { 'loaded': True, 'rowData' : None   }

            if not relModel['loaded']:
                # Obtiene el id
                rowId = rowdict[ relModel['fkId'] ]
                if rowId:
                    relModel['rowData'] = getRowById(relModel['zoomModel'], rowId)
                else:
                    relModel['rowData'] = None
                relModel['loaded'] = True

            rowData = relModel['rowData']
            if rowData is not None  :
                # interpreta los datos del registro
                val = getFieldValue(cpFromField, lField[ 'type'], rowData  , cBase )
            else: 
                val = ''

        rowdict[ fName ] = val

    return rowdict




def addQbeFilter( cBase, Qs ):

    # No hay criterios
    if len(cBase.protoFilter) == 0:
        return Qs

    cBase.baseFilter = verifyList(cBase.baseFilter)
    cBase.protoFilter = verifyList(cBase.protoFilter)

    for sFilter in cBase.baseFilter + cBase.protoFilter:

        if sFilter[ 'property' ] == '_allCols':
            # debe descomponer la busqueda usando el objeto Q
            QTmp = getTextSearch(sFilter, cBase )
            if QTmp is None: QTmp = models.Q()
            Qs = Qs.filter(QTmp)


        else:
            # Los campos simples se filtran directamente, se require para el jsonField
            QTmp = addQbeFilterStmt(sFilter, cBase )
            QTmp = dict((x, y) for x, y in QTmp.children)
            Qs = Qs.filter(**QTmp)


    return Qs


def addQbeFilterStmt( sFilter, cBase ):
    """ 
    Verifica casos especiales y obtiene el QStmt
    retorna un objeto Q
    """
    fieldName = sFilter['property'].replace('.', '__')

    if fieldName == '__str__':
        if cBase.isProtoModel:  
            fieldName = 'smNaturalCode'
        else : return Q()

    if fieldName.endswith('__pk') or fieldName.endswith('_id') or fieldName == 'pk':
        # Los id por ahora son numericos
        sType = 'int'

    elif fieldName.startswith(cBase.jsonField + '__'):
        cBase.jsonLookups.append( sFilter ) 
        return Q()

    else:
        try:
            # Obtiene el tipo de dato, si no existe la col retorna elimina la condicion
            field = get_fields_from_path(cBase.model, fieldName)[-1]
            sType = TypeEquivalence.get(field.__class__.__name__, 'string')
        except :
            return Q()

    QStmt = getQbeStmt(fieldName , sFilter['filterStmt'], sType)

    return QStmt


def getTextSearch(sFilter, cBase ):
    """
    Busqueda Textual ( no viene con ningun tipo de formato solo el texto a buscar
    Si no trae nada deja el Qs con el filtro de base
    Si trae algo y comienza por  "{" trae la estructura del filtro

    Si solo viene el texto, se podria tomar la "lista" de campos "mostrados"
    ya los campos q veo deben coincidir con el criterio, q pasa con los __str__ ??
    Se busca sobre los campos del combo ( filtrables  )
    """

    QStmt = None

    try:
        pSearchFields = cBase.protoMeta['gridConfig']['searchFields']
        fieldsDict = list2dict(cBase.protoMeta[ 'fields' ], 'name')
    except:
        pSearchFields = getSearcheableFields(cBase.model)
        fieldsDict = {}


    for fName in pSearchFields:
        fAux = fieldsDict.get(fName, {})
        if fAux.get('type', '')  not in [ 'string', 'text', 'jsonField' ]: 
            continue

        QTmp = addQbeFilterStmt({'property': fName, 'filterStmt': sFilter['filterStmt'] } , cBase )

        if QStmt is None:  
            QStmt = QTmp
        else: 
            QStmt = QStmt | QTmp

    return QStmt


def getFieldValue(fName, fType, rowData, cBase ):

    # Es una funcion
    if (fName == '__str__'):
        if cBase.isProtoModel:  
            val = rowData.__getattribute__('smNaturalCode')
        else: 
            try:
                val = eval('rowData.__str__()')
                val = verifyStr(val , '')
            except:
                val = 'Id#' + verifyStr(rowData.pk, '?')

    elif fName.startswith('@'):
        val = evalueFuncion(fName, rowData)

    elif (fName == cBase.jsonField):
        # Master jsonField ( se carga texto )
        try:
            val = rowData.__getattribute__(fName)
        except: val = {}
        if isinstance(val, dict):
            val = json.dumps(val , cls=JSONEncoder)

    elif fName.startswith(cBase.jsonField + '__'):
        # JSon fields
        try:
            val = rowData.__getattribute__(cBase.jsonField)
            val = val.get(fName[ len(cBase.jsonField + '__'):])
            val = getTypedValue(val, fType)

        except: 
            val = ''


    elif ('__' in fName):
        # Campo Absorbido modo objeto
        try:
            val = eval('rowData.' + fName.replace('__', '.'))
            val = verifyStr(val , '')
        except: 
            val = '__?'


    # Campo del cBase.modelo
    else:
        try:
            val = getattr(rowData, fName)
            # Si es una referencia ( fk ) es del tipo cBase.model
            if isinstance(val, models.Model):
                val = verifyStr(val , '')
        except: 
            val = 'vr?'

        # Evita el valor null en el el frontEnd
        if val is None: 
            val = ''


    return val


def evalueFuncion(fName, rowData):
    """ 
    para evaluar las funciones @  declaradas en el cBase.modelo
    obtener el titulo y los parametros y enviar la tupla
    """

    try:
        expr = 'rowData.' + fName[1:]
        val = eval(expr)
        val = verifyStr(val , '')
    except: 
        val = fName + '?'

    return val

