

from django.contrib import admin
from protoExt.actions import doSetDefaults 

from prototype.actions import doImportSchema, doImportOMS

class ProjectAdmin( admin.ModelAdmin ):
    actions = [ doSetDefaults, doImportSchema, doImportOMS  ]
