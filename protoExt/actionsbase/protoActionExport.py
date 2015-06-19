# -*- coding: utf-8 -*-

import traceback, tablib  

# from django.http import HttpResponse
from django.template.defaultfilters import slugify

from protoExt.utils.utilsBase import getReadableError
from protoExt.utils.utilsWeb import JsonError , JsonSuccess
from protoExt.utils.downloadFile import getFullPath 

from .protoActionList import prepareListEnv, getQSet, Q2Dict


from import_export.formats import base_formats  
DEFAULT_FORMATS = (
    base_formats.CSV,
    base_formats.XLS,
    base_formats.ODS,
    base_formats.JSON,
    base_formats.YAML,
    base_formats.HTML,
#     base_formats.TSV,
)


def protoExport(request):

    cBase, message = prepareListEnv( request )
    if message: return message  

    try:
        Qs = getQSet( cBase )
        cBase.totalCount = len( Qs )
        pRows = Qs[:]
        pList = Q2Dict(cBase , pRows  )
 
    except Exception as e:
        traceback.print_exc()
        message = getReadableError(e)
        return JsonError( message ) 


    try:
        cBase.fileFormat = int(request.POST.get('fileFormat', 0))
        fileName = _doExportFile( cBase, pList, request )

    except Exception as e:
        traceback.print_exc()
        message = getReadableError(e)
        return JsonError( message ) 

    return  JsonSuccess( {'message' : fileName,  'fileName' : fileName } )


def _doExportFile( cBase, pList, request ):
#   Archivo de salida 

    formats = get_export_formats()
    file_format = formats[ cBase.fileFormat ]()

#   File creation 
    fileName = "%s.%s" % (slugify( cBase.viewCode ), file_format.get_extension())
    fullPath = getFullPath(request, fileName)

    open_mode = 'w' 
    if file_format.is_binary(): open_mode = 'wb' 

#   Carga los datos
    headers = pList[0].keys()
    data = [] 
    for row in pList:
        data.append( row.values()) 

    dataSet = tablib.Dataset(*data, headers=headers)
    export_data = file_format.export_data(dataSet)

#   Write 
    with open( fullPath, open_mode ) as f:
        f.write( export_data )

    return fileName 

    # content_type = file_format.get_content_type()
    # response = HttpResponse(export_data, content_type=content_type)
    # response['Content-Disposition'] = 'attachment; filename=%s' % ( file_name, )
    # return response    


def get_export_formats():
    """
    Returns available import formats.
    """
    return [f for f in DEFAULT_FORMATS if f().can_export()]

