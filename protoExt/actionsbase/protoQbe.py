# -*- encoding: utf-8 -*-

from django.db import models
from django.db.models import Q
from protoExt.utils.utilsConvert import isNumeric, toInteger, toBoolean
import re


from protoExt.utils.utilsBase import JSONEncoder
from protoExt.utils.utilsBase import verifyStr 
from protoExt.utils.utilsConvert import getTypedValue

import json



def addFilter(Qs, sFilter):
#   Agrega un filtro q viene en modo texto a un Qset
    if (len (sFilter) == 0):
        return Qs

    protoStmt = ''

    # Tipo array
    if type(sFilter) == type([]):
        protoStmt = ''


    # Tipo dictionario viene conformado @property[_contain],  .....
    elif type(sFilter) == type({}):
        protoStmt = sFilter

    # Filtro String
    else:
        try:
            protoStmt = eval(sFilter)
        except:
            return Qs

    # en caso de q halla un stmt lo evalua
    if (len (protoStmt) != 0):
        Qs = Qs.filter(**protoStmt)

    return Qs


def construct_search(field_name):
    if field_name.startswith('^'):
        return "%s__istartswith" % field_name[1:]

    elif field_name.startswith('='):
        return "%s__iexact" % field_name[1:]

    elif field_name.startswith('@'):
        return "%s__search" % field_name[1:]

    else:
        return "%s__icontains" % field_name

def getSearcheableFields(model):
# Obtiene los campos visibles del modelo base, se usa como valor por defecto para los searchFields

    lFields = []
    filterableTypes = [ 'CharField', 'TextField', 'JSONField' ]

    for field in model._meta.fields:
        if field.__class__.__name__ in filterableTypes:
            lFields.append(field.name)

    return lFields



def getQbeStmt(fieldName , sQBE, sType):

    QResult = Q()

    # Valida el tipo del criterio
    if type(sQBE).__name__ in ['str', 'unicode']:
        sQBE = sQBE.strip()

        # Verifica si es una funcion
        # if (sQBE and sQBE[0] == '@'):
        #     sQBE = evaluateFunction (sQBE)

        if sQBE == '' :
            return QResult

    elif type(sQBE).__name__ in ['int', 'long', 'float', 'decimal']:
        # es un numero, no hay criterios posibles solo =
        Qobj = { "{0}".format(fieldName) :   sQBE }
        return  Q(**Qobj)

    else:
        sQBE = str(sQBE)


    #  Negacion del criterio
    bNot = False
    if sQBE.startswith('!')  :
        sQBE = sQBE[1:]
        bNot = True


    # -- Para hacerlo recursivo lo que dbde controlar incialemente es el or
    if sQBE.find(";") > 0 :

        lCondicion = sQBE.split(";")
        for sCondicion in lCondicion:
            if len (sCondicion) == 0:
                continue

            bAndConector = False
            if sCondicion.startswith('!') :
                bAndConector = True
                sCondicion = sCondicion[1:]

            Qtmp = getQbeStmt(fieldName, sCondicion, sType)
            if bAndConector:
                QResult = QResult & Qtmp
            else:
                QResult = QResult | Qtmp

        if bNot :
            QResult = ~QResult
        return QResult



    # String:  \iexact, \icontains, \istartswith, isnull, search, TODO: \iendswith, \iregex
    if sType in ([ 'string', 'text', 'jsonfield' ]) :
        if sQBE.startswith('^'):
            Qobj = { "{0}__istartswith".format(fieldName) :  sQBE[1:]  }

        elif sQBE == '=' :
            Qobj = { "{0}__isnnull".format(fieldName) : True }

        elif sQBE.startswith('='):
            Qobj = { "{0}__iexact".format(fieldName) :  sQBE[1:]  }

        elif sQBE.startswith('@'):
            Qobj = { "{0}__search".format(fieldName) :  sQBE[1:]  }

        else:
            Qobj = { "{0}__icontains".format(fieldName) :  sQBE }

        QResult = Q(**Qobj)


    # TODO: Verificar q sea numerico (
    # foreignText es una simple representacion, es siempre el id
    # Numericos : gt, gte, lt, lte,   TODO: in,   range,
    elif sType in ([ 'int', 'foreignid', 'foreigntext', 'decimal' ]):

        if sQBE.startswith(">=") :
            Qobj = { "{0}__gte".format(fieldName) :  sQBE[2:]  }
        elif sQBE.startswith("<=") :
            Qobj = { "{0}__lte".format(fieldName) :  sQBE[2:]  }
        elif sQBE.startswith("<>") | sQBE.startswith("!=") :
            bNot = ~bNot
            Qobj = { "{0}".format(fieldName) :  sQBE[2:]  }

        elif sQBE.startswith(">") :
            Qobj = { "{0}__gt".format(fieldName) :  sQBE[1:]  }
        elif sQBE.startswith("<") :
            Qobj = { "{0}__lt".format(fieldName) :  sQBE[1:]  }
        elif sQBE.startswith("=") :
            Qobj = { "{0}".format(fieldName) :  sQBE[1:]  }
        else:
            Qobj = { "{0}".format(fieldName) :  toInteger(sQBE)  }

        if not isNumeric(re.sub(r'[=><!]', '', sQBE)):
            return QResult

        QResult = Q(**Qobj)

#    TODO: if sType == 'bool':
#    Fechas: year, month, day,   
#    TODO: if sType in ( [ 'date''datetime', 'time' ]) : 

    
    if bNot :
        QResult = ~QResult
    return QResult



def getQbeFilter( cBase,  lFilter  ):
    """
    Retorna oun objeto QStmt q se construye en forma independiente 

    QResult = Q()

    QResult.add(Q(), Q.AND)
    QResult.add(Q(), Q.OR)

    QResult = QResult & Qtmp
    QResult = QResult | Qtmp

    """

    QBase = models.Q()

    # No hay criterios
    if len(lFilter) == 0: return QBase
    for sFilter in lFilter:

        if sFilter[ 'property' ] == '_allCols':
            # debe descomponer la busqueda usando el objeto Q
            QTmp = getTextSearch(sFilter, cBase )
            if QTmp is None: QTmp = models.Q()
            QBase = QBase & QTmp 

        else:
            # Los campos simples se filtran directamente, 
            QTmp = addQbeFilterStmt(sFilter, cBase )
            QBase = QBase & QTmp 

    return QBase


def addQbeFilterStmt( sFilter, cBase ):
    """ 
    Verifica casos especiales y obtiene el QStmt
    retorna un objeto Q
    """
    fieldName = sFilter['property'].replace('.', '__')

    if fieldName == '__str__':
        if cBase.isProtoModel:  
            fieldName = 'smNaturalCode'
        else : return models.Q()

    fAux = cBase.fieldsDict.get(fieldName, {})
    sType = fAux.get('type', '') 

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
    except:
        pSearchFields = getSearcheableFields(cBase.model)


    for fName in pSearchFields:
        fAux = cBase.fieldsDict.get(fName, {})
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
        val = evaluateFunction(fName, rowData)

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


    # Campo del modelo
    else:
        try:
            val = getattr(rowData, fName)
            # Si es una referencia ( fk ) es del tipo models
            if isinstance(val, models.Model):
                val = verifyStr(val , '')
        except: 
            val = 'vr?'

        # Evita el valor null en el el frontEnd
        if val is None: 
            val = ''


    if type( val ) == type(True):
        val = toBoolean( val )  
    else: str( val )

    return val 


def evaluateFunction(fName, rowData):
    """ 
    para evaluar las funciones @  declaradas en el cBase.modelo 
    obtener el titulo y los parametros y enviar la tupla

    Se define una tabla de funciones genericas q seran ejectua dinamicamente por pyton 
    se ejectuan en el contexto actual, se deberia pasar algunas rutinas basicas en la medida q sean necesarias  
     
    Esta rutina servira tambien para desencadenar reglas de gestion sobre modelos y podria ser la base 
    de la ejecucion del wKflow
    """

    # Fix:
    # from protoExt.utils.utilsBase import explode

    # # obtiene los parametros
    # fCall = explode(sQBE[1:])

    # # obtiene la definicion de la funcion
    # from .models import PtFunction, getDjangoModel
    # fBase = PtFunction.objects.get(code=fCall[0])

    # # Construyte las variables de entorno
    # myVars = { 'model' : getDjangoModel(fBase.modelName) }

    # arguments = fBase.arguments.split(',')
    # params = fCall[1].split(',')
    # for i  in range(0 , len(arguments)):
    #     myVars[ arguments[i] ] = params[i]

    # # ejecta y toma la base
    # exec(fBase.functionBody, myVars)
    # return myVars [ 'ret' ]

    try:
        expr = 'rowData.' + fName[1:]
        val = eval(expr)
        val = verifyStr(val , '')
    except: 
        val = fName + '?'

    return val

    pass 
