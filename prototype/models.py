# -*- coding: utf-8 -*-

# FUTURE: Agregar tags 

from django.db import models

from protoLib.models import ProtoModelBase, ProtoModelExt, ProtoJSONManager 
from jsonfield2 import JSONField

from .protoRules import  ONDELETE_TYPES, BASE_TYPES, CRUD_TYPES, DB_ENGINE
from taggit.managers import TaggableManager

from protoExt.utils.utilsConvert import slugify2
from django.conf import settings

import reversion


PROTO_PREFIX = settings.PROTO_PREFIX

"""
    la generacion de las VISTAS se hace como una creacion de una pcl,
    
    La pci contedra ahora : 
        - lista de campos desde los cuales heredar; 
        - detalles q puede definir; 
    
    el tipo de pcl definira la estructura
    
    La estructura se enviara desde el BackEnd cuando se requiera; 
    La validacion de la pci se hace en el backend
    La validacion de campos se hace con seguridad en el backend ) fieldLevel security  
    
    Configuarar los menus adicionales  ( parametricos?? )
        grupo, 
        boton 
        procedimiento
        tipo de ventana 
        datos 
        
    Menu de protipos permitira 
        Detalles 
        Campos absorbidos
    
    La edicion de la pcl cerrara y abrira la opcion

    Las acciones,
        General 
        Model ( dependen del modelo, no se requiere declararlas en el admin ) 
"""
   
class Project(ProtoModelExt):
    
    """Corresponds to a corporate conceptual level MCCD"""
    code = models.CharField(blank=False, null=False, max_length=200)
    description = models.TextField(blank=True, null=True)

    """Info from Db """
    dbEngine = models.CharField(blank=True, null=True, max_length=20, choices=DB_ENGINE, default='sqlite3')
    dbName = models.CharField(blank=True, null=True, max_length=200)
    dbUser = models.CharField(blank=True, null=True, max_length=200)
    dbPassword = models.CharField(blank=True, null=True, max_length=200)
    dbHost = models.CharField(blank=True, null=True, max_length=200)
    dbPort = models.CharField(blank=True, null=True, max_length=200)

    def __str__(self):
        return slugify2(self.code) 

    class Meta:
        unique_together = ('code', 'smOwningTeam')
        # permissions = (( "read_domain", "Can read project"), )        

    protoExt = { 
        "defaultTo": [{
                "deftModel": "prototype.model",
                "deftField": "project_id",
                "name": "prototype.model"
            }, {
                "deftModel": "prototype.entity",
                "deftField": "model__project_id",
                "name": "prototype.entity"
            }, {
                "deftModel": "prototype.diagram",
                "deftField": "project_id",
                "name": "prototype.diagram"
            }, {
                "deftModel": "prototype.property",
                "deftField": "entity__model__project_id",
                "name": "prototype.property"
            }],                 
        "actions": [
#             { "name": "doImportSchema" },
#             { "name": "doImportOMS", "selectionMode" : "single",
#               "actionParams": [
#                  {"name" : "fileName", "type" : "string", "required": False, "tooltip" : "option de menu (msi)" }
#                 ] 
#             }
        ],
        "gridConfig" : {
            "listDisplay": ["__str__", "description", "smOwningTeam"]      
        }, 
        "sheetConfig": [{
            "sheetType": "printerOnly",
            "nameSpace": "proj,  ; ",
            "name": "exportWiki",
            "pageExpr": ", code",
            "template": "prototype/wikiproject.txt"
        }],
    } 


class Model(ProtoModelExt):
    """
    Los modelos corresponde a una solucion especifica,  
    varios modelos pueden estar enmarcados en un dominio
    
    Los modelos son la unidad para generar una solucion ejecutable, 
    los modelos pueden tener prefijos especificos para todas sus componentes ( entidades ) 
    """
    project = models.ForeignKey('Project', blank=False, null=False)
    code = models.CharField(blank=False, null=False, max_length=200)

    category = models.CharField(max_length=50, blank=True, null=True)
    modelPrefix = models.CharField(blank=True, null=True, max_length=50)
    description = models.TextField(blank=True, null=True)

    smTags = TaggableManager( blank=True )
    
    class Meta:
        unique_together = ('project', 'code', 'smOwningTeam')
        
    unicode_sort = ('project', 'code',)

    def __str__(self):
        return slugify2(self.code) 
    
    protoExt = { 
        "defaultTo": [{
                "deftModel": "prototype.entity",
                "deftField": "model_id",
                "name": "prototype.entity"
            }, {
                "deftModel": "prototype.property",
                "deftField": "entity__model_id",
                "name": "prototype.property"
            }],                 
        "actions": [
            { "name": "doModelDiagram" },
            { "name": "doModelPrototype" },
            { "name": "doExportProtoModel" },
            { "name": "doImportProtoModel",  
              "actionParams": [
                {"name" : "file", "type" : "filefield", "required": True, "tooltip" : "Select a file to upload" } ]
            },
            { "name": "doExportDjModels" },
            { "name": "doExportDjViews" },            
            
        ],
        "gridConfig" : {
            "listDisplay": ["__str__", "description", "smOwningTeam"]      
        },
        "sheetConfig": [{
            "sheetType": "printerOnly",
            "nameSpace": "proj,;,project__code",
            "name": "exportWiki",
            "pageExpr": ",code",
            "template": "prototype/wikimodel.txt"
        }],
    } 
    

    
class Entity(ProtoModelExt):
    """ 
    Entity corresponds to the PHYSICAL model;  
    """    
    model = models.ForeignKey('Model', blank=False, null=False, related_name='entity_set')
    code = models.CharField(blank=False, null=False, max_length=200)
    
    dbName = models.CharField(blank=True, null=True, max_length=200)
    description = models.TextField(blank=True, null=True)

    # Propieadad para ordenar el __str__ 
    unicode_sort = ('model', 'code',)

    def __str__(self):
        return slugify2(self.model.code + '-' + self.code) 

    class Meta:
        unique_together = ('model', 'code', 'smOwningTeam')

    protoExt = { 
        "actions": [
            { "name": "doEntityPrototype", "selectionMode" : "single",
              "actionParams": [{"name" : "viewCode", "type" : "string", "required": True,
                                "tooltip" : "option de menu (msi)" }
                               ] 
            },
        ],
        "detailsConfig": [
        {
            "__ptType": "detailDef",
            "menuText": "Properties",
            "conceptDetail": "prototype.Property",
            "detailName": "entity",
            "detailField": "entity__pk",
            "masterField": "pk"
        }, {
            "__ptType": "detailDef",
            "menuText": "Relationships",
            "conceptDetail": "prototype.Relationship",
            "detailName": "entity",
            "detailField": "entity__pk",
            "masterField": "pk"
        }, {
            "__ptType": "detailDef",
            "menuText": "Views",
            "conceptDetail": "prototype.Prototype",
            "detailName": "entity",
            "detailField": "entity__pk",
            "masterField": "pk"
        }
        ],
        "gridConfig" : {
            "listDisplay": ["__str__", "description", "smOwningTeam"]      
        }, 
        "sheetConfig": [{
            "sheetType": "printerOnly",
            "nameSpace": "proj,;,model.project.code;,model.code",
            "name": "exportWiki",
            "pageExpr": ",code",
            "template": "prototype/wikientity.txt"
        }],
    } 




class Property(ProtoModelExt):
    """ 
    Propiedades por tabla, definicion a nivel de modelo de datos.
    Las relaciones heredan de las propriedades y definien la cardinalidad 
    """
    entity = models.ForeignKey('Entity', related_name='property_set')

    # -----------  Antiguo property Base 
    code = models.CharField(blank=False, null=False, max_length=200)

    """baseType, prpLength:  Caracteristicas generales q definen el campo """
    baseType = models.CharField(blank=True, null=True, max_length=50, choices=BASE_TYPES, default='string')
    prpLength = models.IntegerField(blank=True, null=True)
    prpScale = models.IntegerField(blank=True, null=True)


    """prpDefault: Puede variar en cada instancia """ 
    prpDefault = models.CharField(blank=True, null=True, max_length=50)
    
    """prpChoices:  Lista de valores CSV ( idioma?? ) """ 
    prpChoices = models.TextField(blank=True, null=True)

    description = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    # -----------  caracteristicas propias de la instancia
    """isPrimary : en el prototipo siempre es artificial, implica isLookUpResult"""  
    isPrimary = models.BooleanField( default=False)
    isLookUpResult = models.BooleanField(default=False)

    """isNullable: tiene q ver con la Db"""    
    isNullable = models.BooleanField(default=False)
    
    """isRequired: tiene q ver con el llenado de datos"""
    isRequired = models.BooleanField(default=False)

    """isReadOnly: ReadOnly field ( frontEnd"""
    isReadOnly = models.BooleanField(default=False)

    """isForeign: indica si la propiedad ha sido definida en  Relationship"""
    isForeign = models.BooleanField( editable=False, default=False)

    """vType : validation type ( formatos predefinidos email, .... ) """
    vType = models.CharField(blank=True, null=True, max_length=50, choices=BASE_TYPES, default='string')

    """isSensitive: Should increase security level """  
    isSensitive = models.BooleanField(default=False)

    """isEssential: Indica si las propiedades saldran en la vista por defecto """ 
    isEssential = models.BooleanField(default=False)

    crudType = models.CharField(blank=True, null=True, max_length=20, choices=CRUD_TYPES)
    dbName = models.CharField(blank=True, null=True, max_length=200)
    
    """solo para ordenar los campos en la entidad"""
    # secuence = models.IntegerField(blank = True, null = True,)

    def save(self, *args, **kwargs):
        if self.isPrimary: 
            self.isRequired = True
            self.isLookUpResult = True 
  
        super(Property, self).save(*args, **kwargs) 

    class Meta:
        unique_together = ('entity', 'code', 'smOwningTeam')

    def __str__(self):
        return slugify2(self.entity.code + '.' + self.code)      

    unicode_sort = ('entity', 'code',)

    protoExt = { 
        "gridConfig" : {
            "listDisplay": ["__str__", "description", "smOwningTeam"]      
        },
        "sheetConfig": [{
            "sheetType": "printerOnly",
            "nameSpace": "proj,;,entity.model.project.code;, entity.model.code;, entity.code",
            "name": "exportWiki",
            "pageExpr": ",code",
            "template": "prototype/wikiproperty.txt"
        }],
    } 


class Relationship(Property):
    """
    * Tipo particula de propiedad q define las relaciones,  la definicion de la cardinlaidad y otras
    """

    """refEntity : entidad referenciada""" 
    refEntity = models.ForeignKey('Entity', related_name='refEntity_set', null=True )

    """relatedName:  Nombre del set en la tabla primaria ( modelacion objeto )  """
    relatedName = models.CharField(blank=True, null=True, max_length=50)

    # Cardanlidad 
    baseMin = models.CharField(blank=True, null=True, max_length=50)
    baseMax = models.CharField(blank=True, null=True, max_length=50)
    
    refMin = models.CharField(blank=True, null=True, max_length=50)
    refMax = models.CharField(blank=True, null=True, max_length=50)

    # Comportamiento en la db ( typeRelation : Fort, Info )   
    onRefDelete = models.CharField(blank=True, null=True, max_length=50, choices=ONDELETE_TYPES)
    typeRelation = models.CharField(blank=True, null=True, max_length=50)

    def __str__(self):
        return slugify2(self.entity.code + '.' + self.code)     

    def save(self, *args, **kwargs):
        self.isForeign = True 
        super(Relationship, self).save(*args, **kwargs) 

    protoExt = { 
        "gridConfig" : {
            "listDisplay": ["__str__", "description", "smOwningTeam" ]      
        },
        "exclude": [ "baseType", "prpLength", "prpDefault", "prpChoices"]
        }


# ---------------------------





class PropertyEquivalence(ProtoModelExt):
    """ 
    Matriz de equivalencias "semantica"  entre propiedades
    
    Este es un caso particular de relacion donde en usa sola busqueda quisiera 
    obtener donde es source y donde es target, 
    
    se podria agregar un manejador q hicer:   where = sourse UNION where target, 
    o q al momento de guardar generara la relacion inversa y actualizara simpre los dos ( privilegiada )     
    """    

    sourceProperty = models.ForeignKey('Property', blank=True, null=True, related_name='sourcePrp')
    targetProperty = models.ForeignKey('Property', blank=True, null=True, related_name='targetPrp')

    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return slugify2(self.sourceProperty.code + ' - ' + self.targetProperty.code)   

    class Meta:
        unique_together = ('sourceProperty', 'targetProperty', 'smOwningTeam')

#     def delete(self, *args, **kwargs):
#       twoWayPropEquivalence( self, PropertyEquivalence, True )
#       super(PropertyEquivalence, self).delete(*args, **kwargs)

    protoExt = { 
#       "menuApp" : "dictionary", 
        "gridConfig" : {
            "listDisplay": ["__str__", "description", "smOwningTeam"]      
        }
    } 

# def propEquivalence_post_save(sender, instance, created, **kwargs):
#     twoWayPropEquivalence( instance, PropertyEquivalence, False )

# post_save.connect(propEquivalence_post_save, sender = PropertyEquivalence)
    
# This way when the save() method is called, 
# it never fires another post_save signal because we've disconnected it.
#
# def do_stuff(sender, **kwargs):
#    post_save.disconnect(do_stuff, sender=User)
#    kwargs['instance'].save()
#    post_save.connect(do_stuff, sender=User)
#
# post_save.connect(do_stuff, sender=User)

#   --------------------------------------------------------------------------------



class Prototype(ProtoModelBase):
    """
    Esta tabla manejar la lista de  prototypos almacenados en customDefinicion, 
    Genera la "proto" pci;  con la lista de campos a absorber y los detalles posibles        
    """
    entity = models.ForeignKey(Entity, blank=False, null=False , related_name='prototype_set')
    
    """Nombre (str) de la vista a buscar en viewDefinition  """
    code = models.CharField(blank=False, null=False, max_length=200, editable=False)

    description = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    metaDefinition = JSONField(blank=True, null=True)
    objects = ProtoJSONManager(json_fields=['metaDefinition'])

    def __str__(self):
        return slugify2(self.code)  
    
    protoExt = { 
        "gridConfig" : {
            "listDisplay": ["__str__", "entity", "smOwningTeam"]      
        }
    } 

    class Meta:
        unique_together = ('code', 'smOwningTeam')


class ProtoTable(ProtoModelBase):
    """
    Esta es el store de los prototipos   
    """
    
    entity = models.ForeignKey(Entity, blank=False, null=False)
    info = JSONField(default={})
    objects = ProtoJSONManager(json_fields=['info'])

    _setNaturalCode =False 

    def __str__(self):
        return self.entity.code + '.' + str( self.pk )   

    def myStr(self, *args, **kwargs):
        # Evalua el string de prototipos con la lista de campos seleccionados 
        sAux = ''
        for arg in args:
            if arg.startswith( 'info__' ): arg = arg[6:]
            sAux = sAux + '.' + slugify2( self.info.get( arg, '' )) 
        if len( sAux ) > 1:  sAux = sAux[1:]
        return  sAux
   
    protoExt = {
        "jsonField" : "info",  
        "gridConfig" : {
            "listDisplay": ["__str__", "smOwningTeam"]      
        }
    } 
    


class Diagram(ProtoModelExt):

    project = models.ForeignKey('Project', blank=False, null=False)
    code = models.CharField(blank=False, null=False, max_length=200)
    
    description = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    title = models.CharField(blank=True, null=True, max_length=100)

    """Para eliminar en caso de q las entidades tengan prefijo ( instrospeccion )"""
    prefix = models.CharField(blank=True, null=True, max_length=20)

    """Nivel de representation ( 'all', 'essential', 'required' , 'primary', 'title' )"""
    graphLevel = models.IntegerField(blank=True, null=True, default = 0)

    """Representation graphique ( record, htmlTable, graph  )"""
    grphMode = models.IntegerField(blank=True, null=True, default = 0)

    """Formalismo de representation ( ObjetRelational, ER, DataRun  )"""
    graphForm = models.IntegerField(blank=True, null=True, default = 0)

    """Show property Type"""
    showPrpType = models.BooleanField(default=False)

    """Show Border"""
    showBorder  = models.BooleanField(default=False)

    """Show ForeignKeys"""
    showFKey  = models.BooleanField(default=False)


    # Propieadad para ordenar el __str__ 
    unicode_sort = ('project', 'code',)

    def as_json(self):
        return dict(
            id=self.pk,
            code=self.code,
            projectID=self.project_id, 
            smUUID=self.smUUID)
        
    def __str__(self):
        return slugify2(self.project.code + '-' + self.code) 

    class Meta:
        unique_together = ('project', 'code', 'smOwningTeam')


    protoExt = { 
        "actions": [
            { "name": "doDiagram" , "selectionMode" : "multiple" },
        ],
    } 



class DiagramEntity(ProtoModelExt):
    """ 
    Entidades del diagrama  
    """    
    diagram = models.ForeignKey('Diagram', blank=False, null=False)
    entity = models.ForeignKey(Entity, blank=False, null=False)

    """Information graphique ( position, color, ... )  """
    info = JSONField(default={})
    objects = ProtoJSONManager(json_fields=['info'])

    # Propieadad para ordenar el __str__ 
    unicode_sort = ('diagram', 'entity',)

    def __str__(self):
        return slugify2(self.diagram.code + '-' + self.entity.code) 

    class Meta:
        unique_together = ('diagram', 'entity', 'smOwningTeam')



reversion.register(Project)
reversion.register(Model)
reversion.register(Entity)
reversion.register(Property)
reversion.register(Relationship)
reversion.register(PropertyEquivalence)
reversion.register(Prototype)
reversion.register(Diagram)
reversion.register(DiagramEntity)
