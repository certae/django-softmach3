# -*- coding: utf-8 -*-
import traceback


def doFindReplace(modeladmin, request, queryset, parameters):
    """ 
    find and replace sobre la tabla actual 
    parameters   campo,  findText, replaceText 
    """

#   El QSet viene con la lista de Ids  
    if queryset.count() < 1:
        return  {'success':False, 'message' : 'Multiple selection required'}

    if len(parameters) != 3: 
        return  {'success':False, 'message' : 'required: fieldName, findText, replaceText' }

    from protoLib.actions.findReplace import actionFindReplace  
    return actionFindReplace(request, queryset, parameters)


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
