# -*- coding: utf-8 -*-


def doClearLog(modeladmin, request, queryset, parameters):
    """ 
    Clear Log 
    """

    from protoLib.models import Logger

    Logger.objects.all().delete()

    return  {'success':True, 'message' : 'Ok' }

