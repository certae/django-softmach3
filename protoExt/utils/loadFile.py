# -*- coding: utf-8 -*-

from protoExt.utils.utilsWeb import JsonError
from django.views.decorators.csrf import csrf_exempt    
import datetime 
from protoExt.views.protoActionAction import protoExecuteAction
from protoExt.utils.utilsFile import verifyDirPath

@csrf_exempt
def loadFiles(request):

    if not request.user.is_authenticated(): 
        return JsonError('readOnly User')

    if request.method != 'POST':
        return JsonError( 'invalid message' ) 

    from django.conf import settings
    import os 

    filePath = verifyDirPath( settings.MEDIA_ROOT ) 
    if not filePath: return JsonError('invalid path : %s' % settings.MEDIA_ROOT )

    fileroot = request.user.__str__() + datetime.datetime.now().strftime("_%y%m%d_")

    actionFiles = {}
    try:     
        for key, fileObj in request.FILES.items():
            
            path = os.path.join(filePath, fileroot + fileObj.name ) 
            actionFiles[ key ] = path 
            
            dest = open(path, 'wb')
            if fileObj.multiple_chunks:
                for c in fileObj.chunks():
                    dest.write(c)
            else:
                dest.write(fileObj.read())
            dest.close()
            
        request.POST[ "actionFiles" ] = actionFiles
        
    except: 
        return JsonError( 'fileLoad error: ' + fileObj.name  )


    return protoExecuteAction(request)
