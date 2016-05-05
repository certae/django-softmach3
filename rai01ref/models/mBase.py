# -*- coding: utf-8 -*-

from django.db import models
from protoLib.models import ProtoModelBase
from prototype.protoRules import BASE_TYPES, CRUD_TYPES, docProperty2Field
from protoExt.utils.utilsConvert import slugify2
from jsonfield2.fields import JSONField
from protoLib.models.protomanager import JSONAwareManager


""" 
The document type are :  'Artefact', 'Capacity', 'Requirement'
"""

DOCUMENTS = [(s, s) for s in ('Artefact', 'Capacity', 'Requirement')]



class DocType(ProtoModelBase):
    """ 
    Type definition for 3 categories : capacities, artefacts, requiremtns 
    DGT: 1504 El manejo jerarquico podria ser determinado en el tipo 
        - allowHierarchy,  
        - childTypes  [ lista de tipos permitidos en los hijos ] 
    """
    document = models.CharField(blank= False, null= False, max_length= 11, choices= DOCUMENTS )
    dtype = models.CharField(blank= False, null= False, max_length= 200)

    category = models.CharField(max_length=50, blank=True, null=True)

    notes  = models.TextField(blank = True, null = True)
    description  = models.TextField(blank = True, null = True)

    def __str__(self):
        return slugify2(self.document + '-' + self.dtype)

    class Meta:
        app_label = 'rai01ref'
        unique_together = ('document', 'dtype')


    protoExt = {
        "actions": [
            { "name": "doRaiMenu" , "selectionMode" : "multiple" },
        ],
        "gridConfig" : {
            "listDisplay": [ "document", "dtype", "description", "__str__",],
            "others": {
                "filtersSet": [
                {
                    "name": "Artefacts",
                    "customFilter": [{
                        "property": "document",
                        "filterStmt": "^ARTERFACT"
                    }]
                },{
                    "name": "Capacities",
                    "customFilter": [{
                        "property": "document",
                        "filterStmt": "^Capacity"
                    }]
                },{
                    "name": "Requirements",
                    "customFilter": [{
                        "property": "document",
                        "filterStmt": "^Requirement"
                    }]
                }
                ],
            }
        }
    }



class DocAttribute(ProtoModelBase):
    """ 
    Propiedades segun cada tipo de documento 
    DGT: 1504 Si manejara relaciones, podria encadenar diferentes tipos de artefacto 
         - isReference,  referenceDocument 
    """
    docType = models.ForeignKey('DocType', blank=True, null=True)
    code = models.CharField(blank=False, null=False, max_length=200)

    """baseType, prpLength:  Caracteristicas generales q definen el campo """
    baseType = models.CharField(blank=True, null=True, max_length=50, choices=BASE_TYPES, default='string')
    prpLength = models.IntegerField(blank=True, null=True)
    prpScale = models.IntegerField(blank=True, null=True)

    """vType : validation type ( formatos predefinidos email, .... ) """
    vType = models.CharField(blank=True, null=True, max_length=50, choices=BASE_TYPES, default='string')

    """prpDefault: Puede variar en cada instancia """ 
    prpDefault = models.CharField(blank=True, null=True, max_length=50)
    
    """prpChoices:  Lista de valores CSV ( idioma?? ) """ 
    prpChoices = models.TextField(blank=True, null=True)

    """isRequired: tiene q ver con el llenado de datos"""
    isRequired = models.BooleanField(default=False)

    """isSensitive: Should increase security level """  
    isSensitive = models.BooleanField(default=False)

    crudType = models.CharField(blank=True, null=True, max_length=20, choices=CRUD_TYPES)
    description = models.TextField(blank=True, null=True)

    class Meta:
        app_label = 'rai01ref'
        unique_together = ('docType', 'code' )

    def __str__(self):
        return slugify2( str( self.docType ) + '-' + self.code)      

    unicode_sort = ('docType', 'code', )

    protoExt = {
        "gridConfig" : {
            "listDisplay": [ "docType", "code", "description", ],
        }
    }





class DocModel(ProtoModelBase):
    """ 
    Base table for different types of documents rai00base, instances will each have their own table to inherit this,
    Calling the menu will be made in the table will be made with: type, this parameter will serve to the selection table for the definition of the model fields that correspond to the definition of the type be sought

    Tabla de base para los diferentes tipos de documentos de rai00base,  las instancias tendran cada una su propia tabla q heredara de esta,
    La llamada al menu se hara con el la tabla se hara con :type, este parametro ira a la seleccion de la tabla,  para la definicion del modelo se buscaran los campos q corresponden a la definicion del tipo
    """

    """El docType_id determina el grupo ( filtro y valor por defecto )"""
    docType = models.ForeignKey('DocType', blank=True, null=True, related_name = '+')

    code = models.CharField( max_length=200, null=False, blank=False)
    description = models.TextField(blank = True, null = True)


    """ UDP Implementation """
    info = JSONField(default={})
    objects = JSONAwareManager(json_fields=['info'])


    @property
    def iconCls(self):
        return 'rai_{}'.format( self.docType ) 


    # User Defined Document 
    _uddObject = True
    _jField = 'info'


    def __str__(self):
        return slugify2( self.code )  

    class Meta:
        app_label = 'rai01ref'
        abstract = True

    @staticmethod
    def getJfields( idType = None  ):
        """ 
        Necessary for buid pci after doRaiMenu
        Search fields and the title to complete the model
        """ 

        fDict = {
            'fullPath': {
                'name': 'fullPath', 
                'type': 'string', 
                'readOnly': True, 
                'crudType': 'readOnly'
            }        
        }

        if idType is not None: 
            try: 
                docType = DocType.objects.get( pk = idType )
                docType = docType.dtype
            except: 
                return fDict, ''
    
            jFields = DocAttribute.objects.filter( docType = idType )

        else: 
            jFields = DocAttribute.objects.all()
            docType = 'Documents'
            

        for pProperty in jFields:

            fCode =  slugify2( pProperty.code ) 
            fDict[ 'info__' + fCode  ] = docProperty2Field( fCode, pProperty.__dict__ , 'info'  )


        return fDict, docType 
