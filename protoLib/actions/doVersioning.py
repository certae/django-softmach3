# -*- coding: utf-8 -*-

from protoLib.models.versions import VersionHeaders
import uuid


def doDeleteVersion(modeladmin, request, queryset, parameters):
    """ 
    Borra los datos de una version existente
    """

    result = getdetailSet(modeladmin, request, queryset)
    if type(result) is not set:
        return result

#   Get selected version
    v1 = queryset[0].versionCode

    return _doDelVersion(result, v1)


def _doDelVersion(result, v1):

    #  Delete old versions
    for pEntity in result:
        pEntity.objects.filter(smVersion=v1).delete()

    return {'success': True, 'message':  'Ok'}


def doCreateVersion(modeladmin, request, queryset, parameters):
    """ 
    Clear una copia de la informacion bajo una nueva version 
    """

    result = getdetailSet(modeladmin, request, queryset)
    if type(result) is not set:
        return result

    # Se manejan uan estructuras por tabla con dos listas ordenadas {
    # 'entidad' : [ [], [] ] }
    idEquiv = {}

#   Get selected version
    v0 = queryset[0].versionBase
    v1 = queryset[0].versionCode


    _doDelVersion(result, v1)

    for pEntity in result:

        entityName = pEntity._meta.db_table

        # Dependant entity
        # Si anulo la entidad dependiente, solo pasan los campos del padre, el hijo no se copia 
        # La solucion es buscar cuando un registro del padre es invocado por el hijo 
        # if len(pEntity._meta.parents) > 0: continue

        # Duplicate entity?
        if idEquiv.get(entityName, '') != '':
            continue

        # Listas de ids
        idList0 = []
        idList1 = []

        #  Hace la copia
        for reg in pEntity.objects.filter(smVersion=v0):

            # Excepcion para el manejode relaciones heredadas de propiedades ( relationship - property )
            try:
                parentLink = ( entityName == 'prototype_property' ) and reg.isForeign
            except: parentLink = False 
            if parentLink: continue

            idList0.append(reg.pk)

            reg.smUUID = uuid.uuid4()
            reg.smVersion = v1

            # https://docs.djangoproject.com/en/1.9/topics/db/queries/#copying-model-instances             
            reg.pk = None
            reg.id = None
            reg.save()

            idList1.append(reg.id)

        # Guarda la estructura con las listas de equivalencia de ids
        idEquiv[entityName] = [idList0, idList1]

    # Busca todas los foreignkey  por UUID y los actualiza
    for pEntity in result:

        entityName = pEntity._meta.db_table

        # FK identification          
        relFields = []
        for f in pEntity._meta.get_fields():
            if f.is_relation and (f.many_to_one and f.related_model):
                relName = f.related_model()._meta.db_table
                if not relName in idEquiv.keys(): continue
                relFields.append( (f, relName) )
        
        if len(relFields) == 0: 
            continue 

        for reg in pEntity.objects.filter(smVersion=v1):

            # Excepcion para el manejode relaciones heredadas de propiedades ( relationship - property )
            try:
                parentLink = ( entityName == 'prototype_property' ) and reg.isForeign
            except: parentLink = False 
            if parentLink: continue

            for f, relName in relFields:
       
                # get entity idsVersionTitle
                idRef0 = getattr( reg , f.column)
                idList0, idList1 = idEquiv.get(relName, [[], []])

                ix = idList0.index(idRef0)
                setattr( reg , f.column, idList1[ ix ])

            reg.save()


    return {'success': True, 'message': 'Ok'}


def getdetailSet(modeladmin, request, queryset):

    #   El QSet viene con la lista de Ids
    if queryset.count() != 1:
        return {'success': False, 'message': 'One version needed !!'}

    detailSet = set()

#   Get Version Headers
    for entity in VersionHeaders.objects.all():
        addDetailToVersionList(detailSet,  entity.modelCType.model_class())

    return detailSet


def addDetailToVersionList(detailSet, model):

    # Version Allow
    try:
        model._meta.get_field('smVersion')
    except:
        return 

    detailSet.add(model)

    # Se podrian definir todos los detalles, para el debuger  
    for detail in model._meta.get_all_related_objects():
        addDetailToVersionList(detailSet, detail.related_model)




# TODO DGT Indentificar llaves en prototypes ---------------------------------


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

        # DGT TODO Field identification for version copy in prototypes 
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

        TODO DGT: This the base for protoype version copy, bcause we need to get the fk 
        Verificar su es un repositorio dinamico, prototypo o artefacto 
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

