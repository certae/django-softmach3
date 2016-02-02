# -*- coding: utf-8 -*-

from .doVersioning import doCreateVersion, doDeleteVersion 

def doClearLog(modeladmin, request, queryset, parameters):
    """ 
    Clear Log 
    """

    from protoLib.models.smbase import Logger

    Logger.objects.all().delete()

    return  {'success':True, 'message' : 'Ok' }

