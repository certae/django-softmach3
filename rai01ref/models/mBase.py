# -*- coding: utf-8 -*-


from django.db import models
from protoLib.models import ProtoModelBase
from prototype.protoRules import BASE_TYPES, CRUD_TYPES, docProperty2Field
from protoExt.utils.utilsConvert import slugify2
from jsonfield2.fields import JSONField
from protoLib.models.protomanager import JSONAwareManager
from protoLib.models.versions import VersionHeader, VersionTitle


""" 
    Los tipos de documentos son 'ARTEFACT', 'CAPACITY', 'REQUIREMENT'

    COMPOSITION podria corresponder a los arcos entre dos ARTEFACT, 
                dependiendo el tipo de arco los campos podrian ser diferentes, 
                luego el tipo de artefacto determinaria el tipo de arcos q pueda manejar 
                en un proceso pueden ser conexiones, en un modelo relacional puede ser la cardinalidad 

"""

DOCUMENTS = [(s, s) for s in ('ARTEFACT', 'CAPACITY', 'REQUIREMENT')]



class RaiVersionTitle(VersionTitle):

    versionHeaders = [ 
        "ra01ref.artefact",
        "ra01ref.artefactcapacity",
        "ra01ref.artefactcomposition",
        "ra01ref.artefactrequirement",
        "ra01ref.artefactsource",
        "ra01ref.capacity",
        "ra01ref.docattribute",
        "ra01ref.doctype",
        "ra01ref.domain",
        "ra01ref.projectartefact",
        "ra01ref.projectcapacity",
        "ra01ref.projectrequirement",
        "ra01ref.requirement",
        "ra01ref.source",
         ]

    versionExclude = [ 
        "ra01ref.projet", 
        ]


    protoExt = {
        "gridConfig": {
            "listDisplay": ["__str__", "description", "smCreatedBy"]
        }, 
        "actions": [
            { "name": "doCopyVersion", "selectionMode" : "single"}, 
            { "name": "doDeleteVersion", "selectionMode" : "single"}, 
        ],
        "contextTo": [{
            "deftModel": "ra01ref.domain",
            "deftField": "smVersion_id",
            },{
            "deftModel": "ra01ref.artefact",
            "deftField": "smVersion_id",
            },{
            "deftModel": "ra01ref.artefactcapacity",
            "deftField": "smVersion_id",
            },{
            "deftModel": "ra01ref.artefactcomposition",
            "deftField": "smVersion_id",
            },{
            "deftModel": "ra01ref.artefactrequirement",
            "deftField": "smVersion_id",
            },{
            "deftModel": "ra01ref.artefactsource",
            "deftField": "smVersion_id",
            },{
            "deftModel": "ra01ref.capacity",
            "deftField": "smVersion_id",
            },{
            "deftModel": "ra01ref.projectartefact",
            "deftField": "smVersion_id",
            },{
            "deftModel": "ra01ref.projectcapacity",
            "deftField": "smVersion_id",
            },{
            "deftModel": "ra01ref.projectrequirement",
            "deftField": "smVersion_id",
            },{
            "deftModel": "ra01ref.requirement",
            "deftField": "smVersion_id",
            },{
            "deftModel": "ra01ref.source",
            "deftField": "smVersion_id",
            },{
            "deftModel": "ra01ref.doctype",
            "deftField": "smVersion_id",
            },{
            "deftModel": "ra01ref.docattribute",
            "deftField": "smVersion_id",
        }],
    }



class ProtoModelRai(ProtoModelBase):
    """ Versioning model """ 

    smVersion = models.ForeignKey('RaiVersionTitle', blank=False, null=False, default=1)

    class Meta:
        app_label = 'rai01ref'
        abstract = True


class DocType(ProtoModelRai):
    """ 
    Definicion de los tipos segun las 3 categorias ( capacidades, artefactos, exigencias )
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
        unique_together = ('document', 'dtype','smVersion')


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
                        "filterStmt": "^CAPACITY"
                    }]
                },{
                    "name": "Requirements",
                    "customFilter": [{
                        "property": "document",
                        "filterStmt": "^REQUIREMENT"
                    }]
                }
                ],
            }
        }
    }



class DocAttribute(ProtoModelRai):
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
        unique_together = ('docType', 'code','smVersion' )

    def __str__(self):
        return slugify2( str( self.docType ) + '-' + self.code)      

    unicode_sort = ('docType', 'code', )

    protoExt = {
        "gridConfig" : {
            "listDisplay": [ "docType", "code", "description", ],
        }
    }


class Domain(ProtoModelRai):
    code = models.CharField(blank= False, null= False, max_length= 200)
    description = models.TextField(blank = True, null = True)

    class Meta:
        app_label = 'rai01ref'
        unique_together = ( 'code', )

    def __str__(self):
        return slugify2( self.code)      

    unicode_sort = ('code',)



""" Tabla de base para los diferentes tipos de documentos de rai00base,  las instancias 
tendran cada una su propia tabla q heredara de esta, 
La llamada al menu se hara con el la tabla se hara con :type, este parametro ira 
a la seleccion de la tabla,  para la definicion del modelo se buscaran los campos q corresponden 
a la definicion del tipo  
"""
class DocModel(ProtoModelRai):

    """El docType_id determina el grupo ( filtro y valor por defecto )"""
    docType = models.ForeignKey('DocType', blank=True, null=True, related_name = '+')

    code = models.CharField( max_length=200, null=False, blank=False)
    domain  = models.ForeignKey('Domain', blank= True, null= True, related_name = '+') 

    description = models.TextField(blank = True, null = True)

    """ Guarda la definicion de campos leida de RaiAttribute """
    info = JSONField(default={})
    objects = JSONAwareManager(json_fields=['info'])


    # User Defined Document 
    _uddObject = True
    _jField = 'info'


    def __str__(self):
        return slugify2( self.docType.dtype + '-' + self.code )  


    class Meta:
        app_label = 'rai01ref'
        abstract = True
        unique_together = ('docType','code','smVersion' )

    @staticmethod
    def getJfields( idType ):
        """ Busca los campos y el titulo para completar el modelo 
        """ 

        fDict = {}

        try: 
            docType = DocType.objects.get( pk = idType )
        except: 
            return fDict, ''


        jFields = DocAttribute.objects.filter( docType = idType )

        for pProperty in jFields:

            fCode =  slugify2( pProperty.code ) 
            fDict[ 'info__' + fCode  ] = docProperty2Field( fCode, pProperty.__dict__ , 'info'  )

        """Retorna los campos y el titulo"""
        return fDict, docType.dtype 
