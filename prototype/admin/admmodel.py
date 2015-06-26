
from django.contrib import admin
from prototype.actions import doModelPrototype,  doExportDjModels, doExportDjViews, doExportProtoModel , doImportProtoModel, doModelDiagram 


class ModelAdmin( admin.ModelAdmin ):
    actions = [ doModelPrototype, doModelDiagram, doExportDjModels, doExportDjViews, doExportProtoModel, doImportProtoModel ]
