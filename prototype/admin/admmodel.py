
from django.contrib import admin
from prototype.actions import doModelPrototype,  doExportPrototype, doExportProtoJson, doExport2Json , doImport4Json, doModelDiagram 


class ModelAdmin( admin.ModelAdmin ):
    actions = [ doModelPrototype, doModelDiagram, doExportPrototype, doExportProtoJson, doExport2Json, doImport4Json ]
