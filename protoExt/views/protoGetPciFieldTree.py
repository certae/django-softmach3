# -*- coding: utf-8 -*-

from protoExt.utils.utilsBase import traceError, json 

from django.http import HttpResponse

from protoLib.getStuff import getDjangoModel 
from protoExt.utils.utilsWeb import JsonError 
from protoExt.utils.utilsBase import getReadableError

from protoExt.views import validateRequest 
from protoExt.views.prototypeActions import isPrototypePci
from protoExt.views.protoField import isAdmField, setFieldDict
from protoExt.views.protoGrid import setDefaultField



def protoGetFieldTree(request):
    """ return full field tree 
    """

    cBase, msgReturn = validateRequest( request )
    if msgReturn: return msgReturn  
    
    try: 
        cBase.model = getDjangoModel(cBase.viewEntity)
    except :
        return JsonError('model not found: {0}'.format( cBase.viewEntity )) 

    
    fieldList = []
    if isPrototypePci( cBase ): 
        protoEntityId = request.POST.get('protoEntityId')
        if not protoEntityId >= 0: return JsonError('invalid idEntity')

        from prototype.actions.viewDefinition import GetProtoFieldsTree
        fieldList = GetProtoFieldsTree(protoEntityId)


    else: 
        # Se crean los campos con base al modelo ( trae todos los campos del modelo 
        # for field in cBase.model._meta._fields(): # only for django 1.4
        for field in cBase.model._meta.fields:
            try: 
                addFiedToList(fieldList, field , '')
            except Exception as  e:
                traceError()
                return JsonError(getReadableError(e)) 
            
        # Add __str__ 
        myField = { 
            'id'        : '__str__' ,
            'text'      : '__str__' ,
            'checked'   : False,
            'leaf'      : True 
         }
        
        # Defaults values
        setDefaultField(myField, cBase.model , cBase.viewCode)
        
        # FUTURE: FormLink redefinition to original view 
        # myField['zoomModel'] =  cBase.viewCode  
        fieldList.append(myField)

    # Codifica el mssage json 
    context = json.dumps(fieldList)
    return HttpResponse(context, content_type="application/json")



def addFiedToList(fieldList , field, fieldBase):
    """ return parcial field tree  ( Called from protoGetFieldTree ) 
    """

    fieldId = fieldBase + field.name

    # DEfinicion proveniente del dict ( setFieldDict )  
    protoFields = {}
    setFieldDict (protoFields , field)
    pField = protoFields[ field.name ]
    
    # fieldBase indica campos de llaves foraneas       
    if fieldBase != '': 
        # Los campos heredados son siempre ro y no requeridos  
        pField[ 'readOnly' ] = True 
        pField['required'] = False 
        if pField['type'] == 'autofield':
            pField['type'] = 'int'

    pField['id'] = fieldId
    pField['text'] = field.name

    pField['leaf'] = True
    pField['checked'] = False

    # Recursividad Fk 
    if pField['type'] != 'foreigntext':
        pass 

    # no se requiere profundizar en los campos de seguridad ( usr, ... )   
    elif isAdmField(field.name): 
        pass 

    # Evita demasiada recursividad ( 5 niveles debe ser mas q suficiente ) 
    elif fieldId.count('__') > 3:   
        pass 

    else:  

        # si es base, Agrega el campo id del zoom   
        # en los campos heredados no se hace zoom ( no se requiere el id )   
        if (fieldBase == '') :  

            # Obtiene el fkId del diccionario  
            pFieldId = protoFields[ pField['fkId'] ]

            pFieldId['id'] = pFieldId['name']
            pFieldId['text'] = pFieldId['name']  
            pFieldId['required'] = pField.get('required', False)   

            pFieldId['leaf'] = True
            pFieldId['checked'] = False
    
            fieldList.append(pFieldId)

        # itera sobre el campo para heredar de sus padres  
        fkFieldList = []
        relmodel = field.rel.to
        for fAux in relmodel._meta.fields:
            # los id de los campos heredados tampoco se presentan 
            if fAux.name == 'id' :
                continue 
            
            # los campos adm de los heredados no se presentan  
            if isAdmField(fAux.name):
                continue 
            
            addFiedToList(fkFieldList, fAux , fieldId + '__')

        pField['leaf'] = False 
        pField['children'] = fkFieldList
    
    fieldList.append(pField)

