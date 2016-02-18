

from django.contrib import admin


class ProjectAdmin( admin.ModelAdmin ):
    from prototype.actions import doImportSchema
    actions = [ doImportSchema  ]

    # from prototype.actions import doImportSchema, doImportOMS
    # actions = [ doSetContext, doImportSchema, doImportOMS  ]
    # pass 
