from django.contrib import admin

from .models import DocAttribute, DocType, Artefact, Source, Requirement, Capacity
from .models import Projet
from reversion.helpers import patch_admin
# from .models import ArtefactCapacity, ArtefactComposition, ArtefactRequirement, ArtefactSource 
# from .models import ProjectArtefact, ProjectCapacity, ProjectRequirement 


admin.site.register( DocAttribute )


# admin.site.register( ArtefactCapacity )
# admin.site.register( ArtefactComposition )
# admin.site.register( ArtefactRequirement )
# admin.site.register( ArtefactSource  )

admin.site.register( Projet )
# admin.site.register( ProjectArtefact )
# admin.site.register( ProjectCapacity )
# admin.site.register( ProjectRequirement  )
admin.site.register( Source )



from .actions import doRaiMenu
class MyDocType( admin.ModelAdmin ):
    actions = [ doRaiMenu  ]

admin.site.register( DocType, MyDocType )


from .actions import doBusinessProcessDiagram, doTreeDiagram,  doUpdateMeta
class MyArtefac( admin.ModelAdmin ):
    actions = [ doBusinessProcessDiagram, doTreeDiagram, doUpdateMeta  ]

admin.site.register( Artefact, MyArtefac  )


# Documents 
class MyDocument( admin.ModelAdmin ):
    actions = [ doTreeDiagram, doUpdateMeta  ]

admin.site.register( Requirement, MyDocument )
admin.site.register( Capacity, MyDocument )


