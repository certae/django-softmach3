# -*- coding: utf-8 -*-

import  json

from django.http import HttpResponse
from django.db.models import Max

from protoLib.getStuff import getDjangoModel 
from protoExt.utils.utilsWeb import JsonError 


# TODO: Sequences 

def getFieldIncrement(request):
    success = False
    # fieldName = request.GET['fieldName']
    # viewEntity = request.GET['viewEntity']
    # try: 
    #     model = getDjangoModel(viewEntity)
    # except :
    #     return JsonError('model not found:' + viewEntity)
    
    # fieldType = model._meta.get_field(fieldName).get_internal_type()
    # increment = 0
    # if fieldType == 'IntegerField':
    #     maxid = model.objects.aggregate(Max('id'))
    #     if maxid['id__max']:
    #         increment = maxid['id__max'] + 1
    #     else:
    #         increment = 1
    # else:
    #     return JsonError('Invalid field type')
    
    # if increment > 0:
    #     success = True
        
    # jsondict = {
    #     'success': success,
    #     'increment': increment
    # }
    
    # json_data = json.dumps(jsondict)
    # return HttpResponse(json_data, content_type="application/json")
