# -*- coding: utf-8 -*-

import traceback
from protoExt.utils.utilsBase import getReadableError


def doSetDefaults(modeladmin, request, queryset, parameters):
    """ 
    find and replace sobre la tabla actual 
    parameters   campo,  findText, replaceText 
    """

#   El QSet viene con la lista de Ids  
    if queryset.count() != 1:
        return  {'success':False, 'message' : 'Single selection required'}


    from protoLib.actions.setDefaults import actionSetDefaults  

    try:
        result = actionSetDefaults(request, queryset, parameters)

    except Exception as e:
        traceback.print_exc()
        result = {'success':False, 'message' : getReadableError(e) }

    return result  



# def doClearLog(modeladmin, request, queryset, parameters):
#     """ 
#     TODO: Clear Log 
#     """
# 
#     from protoLib.models import Logger
# 
#     Logger.objects.all().delete()
# 
#     return  {'success':True, 'message' : 'Ok' }
