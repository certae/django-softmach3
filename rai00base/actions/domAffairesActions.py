# -*- coding: utf-8 -*-

# Import Database class

from protoExt.utils.utilsBase import traceError
from protoExt.utils.utilsBase import getReadableError


def doRaiActions( modeladmin, request, queryset, parameters, action ):
    """
    funcion para importar modelos realizados en OMS ( Open Model Spher )
    """

    # Background function 
    def doBaseImport( cOMS ):
    
        try:
            cOMS.doImport()
            cOMS.doFkMatch( )
    
        except :
            traceError()
            raise 


#   El QSet viene con la lista de Ids
    if queryset.count() != 1:
        return  {'success':False, 'message' : 'No record selected' }

    from protoLib.getStuff import getUserProfile
    userProfile = getUserProfile( request.user, 'prototype', '' )

    from rai00base.actions.domAffimportOMS import importOMS_RAI
    cOMS = importOMS_RAI( userProfile, queryset[0]  )

    if action == 'IMPORT':

        actionFiles = request.POST.get( "actionFiles", {} )

    #   load and validate xml file
        try:

            fileName = actionFiles[ 'file']
            cOMS.loadFile( fileName  )

        except Exception as e:
            traceError()
            return  {'success':False, 'message' : getReadableError(e) }


        # Return and continue 
        from threading import Thread
        t = Thread(target= doBaseImport, args=( cOMS,))
        t.daemon = True 
        t.start()

        return {'success':True, 'message' :  'runing ...' }


    elif action == 'MATCH':
        try:
            cOMS.doRacMatch()

    #   Recorre los registros selccionados
        except Exception as e:
            traceError()
            return  {'success':False, 'message' : 'Load error' }


        return {'success':True, 'message' :  'runing ...' }

