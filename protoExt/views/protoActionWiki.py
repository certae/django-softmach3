# -*- coding: utf-8 -*-

# Manejo de reportes basdaos en plantillas ( sheets )
#Dg 121105   --------------------------------------------------
#
from .protoActionList  import getQSet
from protoExt.utils.utilsBase import  getReadableError
from protoExt.utils.utilsWeb import JsonError, JsonSuccess

from protoExt.views.protoActionList import prepareListEnv
import traceback
from django.template import loader
from django.template.context import Context
from protoExt.views.getStuff import getParameter
from protoExt.utils.utilsFile import joinPath, verifyDirPath, WriteFile
from protoLib.getStuff import cAux
from protoExt.utils.utilsConvert import slugify2


def protoWiki(request):
    """ 
    Reporte basado en plantillas wiki 

    Recibe  opcion, plantilla base,  Qs ( lista de ids )

    La plantilla de base sera solicitada al usuario, si se deja en blanco usara el sheetSelector o el default
    Los detalles no tienen selector, siempre se usara el template marcado en el detalle.

    """

    try:
        cBase, message = prepareListEnv(request)
        if message: return message

    except Exception as e:
        traceback.print_exc()
        message = getReadableError(e)
        return JsonError(message)


# 	Sheet et list selection
    cRep = cAux()
    cRep.sheetName = request.POST.get('sheetName', '' )
    _getSheetConf( cBase, cRep  )

    try:
        # Obtiene las filas del cBase.modelo
        Qs = getQSet(cBase)

    except Exception as e:
        traceback.print_exc()
        message = getReadableError(e)
        return JsonError(message)

    cRep.wikiPath = getParameter('wikiPath', '~/tmp/wiki')

    for reg in Qs:
        try:
            msgError = _doWikiFile(cBase, cRep , reg)
            if msgError: return msgError 

        except Exception as e:
            traceback.print_exc()
            message = getReadableError(e)
            return JsonError(message)

    return JsonSuccess()


def _doWikiFile(cBase, cRep,  reg ):
    """
    nameSpace     prefix, Campo ; prefix, Campo  
    pageExpr      prefix, Campo
    """
    
    myPath = cRep.wikiPath
    cRep.nSpace = ''
    
    # Obtiene los diferentes pedazos del path      
    for relPath in cRep.nSpaceExpr.replace(' ', '').split( ';' ):
        if len( relPath ) == 0: continue 
        preFix = _getRelNameSpace( relPath, reg  )
        
        cRep.nSpace = _joinNSpace( cRep.nSpace, preFix  )
        myPath  = joinPath( myPath, preFix  )
        
    # Verifica el path              
    filePath = verifyDirPath( myPath )
    if not filePath: 
        return JsonError('invalid path : %s' % myPath )

    #     
    fileName = _getRelNameSpace( cRep.pageExpr , reg )
    cRep.fullName = _joinNSpace( cRep.nSpace, fileName  )
 
    filePath = joinPath( filePath, fileName + '.txt' )

    # Carga el template   
    t = loader.get_template( cRep.template )
    wFile = t.render(Context({ 
          cRep.regName : reg, 
          'nspace' : cRep.nSpace,  
          'fullname' : cRep.fullName,
          }))

    WriteFile(filePath, wFile, 'w')


def _joinNSpace(nSpace, preFix):
    if nSpace: nSpace += ':'  
    return nSpace + preFix 


def _getRelNameSpace( relPath, reg ):
    """ 
    Construye el relPath basado en un prefijo y el vr de un campo
    """
    preFix, preVar =  relPath.replace(' ','').split( ',' )
    if len( preVar ):
        preVar = preVar.replace( '__', '.')
        preVar = slugify2( eval( '%s.%s' % ( 'reg',  preVar )))  
    return slugify2( preFix + preVar ) 


def _getSheetConf(cBase, cRep):
    """ 
    Obtiene un sheetConfig dado su nombre
    recibe  la definicion ( protoMeta ) y el nombre ( str )
    retorna sheetConfig ( obj )
    """

    sheetConfs = cBase.protoMeta.get('sheetConfig', [])

    # Los recorre todos pero se queda con el primero en caso de no encotrarl el nombre seleccionado
    cRep.sheetConf = None
    for item in sheetConfs:
        if cRep.sheetConf == None:
            cRep.sheetConf = item
        if item.get('name', '') == cRep.sheetName :
            cRep.sheetConf = item
            break

    if cRep.sheetConf == None:
        return "sheet definition not found %s" % cRep.sheetName  

    cRep.nSpaceExpr = cRep.sheetConf.get( 'nameSpace', '' )
    cRep.pageExpr = cRep.sheetConf.get( 'pageExpr', '' )
    cRep.template = cRep.sheetConf.get( 'template', '' )
    cRep.regName = slugify2( cBase.viewCode.split('.')[1] )  
    

