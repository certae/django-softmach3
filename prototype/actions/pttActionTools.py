'''
Created on 2013-12-21

@author: dario
'''

from protoExt.utils.utilsConvert import slugify2 

TypeEquivalence = { 
        'bool'      :   'BooleanField',
        'string'    :   'CharField', 
        'date'      :   'DateField', 
        'datetime'  :   'DateTimeField', 
        'decimal'   :   'DecimalField',
        'float'     :   'FloatField',
        'int'       :   'IntegerField',
        'text'      :   'TextField',
        'time'      :   'TimeField',
        'jsonfield' :   'JSONField',
    }



def getViewCode( pEntity, viewTitle = None ):
    if viewTitle is None:
        viewTitle = pEntity.code
    return slugify2( pEntity.model.code + '-' + viewTitle )
