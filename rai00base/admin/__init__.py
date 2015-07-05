# -*- coding: utf-8 -*-

from django.contrib import admin

from rai00base.models import DomaineAffaires
from rai00base.actions import  doImportRAI, doMatchRAI

class AdmDomaineAffaires( admin.ModelAdmin ):
    actions = [ doImportRAI, doMatchRAI  ]

admin.site.register( DomaineAffaires, AdmDomaineAffaires )


# ------------------------------------------------

from rai00base.models import ModeleRaccordement
from rai00base.actions import  doFindReplace

class AdmModeleRaccordement( admin.ModelAdmin ):
    actions = [ doFindReplace ]

admin.site.register( ModeleRaccordement, AdmModeleRaccordement )


# ------------------------------------------------

from rai00base.models import Modele
from rai00base.actions import  doMatrixRacc

class AdmModele( admin.ModelAdmin ):
    actions = [ doMatrixRacc ]

admin.site.register( Modele, AdmModele )



# ------------------------------------------------

from rai00base.models import Entite 
from rai00base.actions import  doAddModel

class AdmEntite( admin.ModelAdmin ):
    actions = [ doAddModel ]

admin.site.register( Entite, AdmEntite )