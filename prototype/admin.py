# This is an auto-generated model module by CeRTAE OMS PlugIn

from import_export import resources
from import_export.admin import ImportExportActionModelAdmin # ImportExportModelAdmin

from reversion.helpers import patch_admin
from .models import ProtoTable
from django.contrib import admin

# -----------------------------------------   Model  
from .actions import doModelPrototype, doDiagram, doExportPrototype, doExportProtoJson, doExport2Json , doImport4Json, doModelDiagram 
from .models import Project,  Model, Property,  Relationship  #, Prototype

class ModelAdmin( admin.ModelAdmin ):
    actions = [ doModelPrototype, doModelDiagram, doExportPrototype, doExportProtoJson, doExport2Json, doImport4Json ]

admin.site.register(Model, ModelAdmin)

# ------------------------------------------  Entity
from .actions import  doEntityPrototype
from .models import Entity


class EntityResource(resources.ModelResource):
    class Meta:
        model = Entity

class EntityAdmin( ImportExportActionModelAdmin ):
    actions = [ doEntityPrototype  ]
    resource_class = EntityResource

admin.site.register(Entity, EntityAdmin )
patch_admin(Entity)


# ------------------------------------------  Entity
from .actions import doImportSchema, doImportOMS

class ProjectAdmin( admin.ModelAdmin ):
    actions = [ doImportSchema, doImportOMS  ]

admin.site.register(Project, ProjectAdmin )


# ------------------------------------------

from .models import Diagram

class DiagramAdmin( admin.ModelAdmin ):
    actions = [  doDiagram  ]

admin.site.register(Diagram , DiagramAdmin)


admin.site.register(Property )
#admin.site.register(PropertyEquivalence )

admin.site.register(Relationship )
admin.site.register( ProtoTable )

patch_admin(Project)
patch_admin(Model)
patch_admin(Property)
patch_admin(Relationship)
patch_admin(Diagram)

#admin.site.register( Prototype )

#admin.site.register( Diagram )
#admin.site.register( DiagramEntity )

#admin.site.register( Service )
#admin.site.register( ServiceRef )
