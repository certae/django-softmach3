# -*- coding: utf-8 -*-

from django.db import models
from jsonfield2 import JSONField, JSONAwareManager


from protoLib.models.protomodel import ProtoModelBase 
from protoLib.models.protomanager import ProtoUserManager, ProtoJSONManager


"""
DGT: Repositorios para manejo definiciones  
"""


class ViewDefinition(models.Model):
    """
    Esta tabla guarda las definiciones de las pcls y del menu,
    es un contenedor generico para manejar documentos json modificados de lo q
    en principio es la definicion de base de los modelos 
    
    Por lo tanto no debe depender del usuario ( team ) ya que es la definicion 
    de la aplicacion. 
    
    Es importante mantener las diferentes versions, **usar reversion en el admin** 
    """

    code = models.CharField(unique=True, blank=False, null=False, max_length=200)
    description = models.TextField(verbose_name=u'Description', blank=True, null=True)

    # Si no esta activo no permite la ejecucion 
    # overWrite indica que debe generarse cada vez, 
    active = models.BooleanField(default = True)
    overWrite = models.BooleanField(default = False)

    metaDefinition = JSONField(default={})
    objects = JSONAwareManager(json_fields = ['metaDefinition'])


    def __str__(self):
        return self.code

    protoExt = {
        "gridConfig" : {
            "listDisplay": ["__str__", "description", "active", "overWrite"],
        }
    }



class CustomDefinition(ProtoModelBase):
    """
    maneja las definiciones por usuarios
    aqui se guardan los menus personalizados, y las customOptions
    """

    code = models.CharField(blank=False, null=False, max_length=200)
    description = models.TextField(verbose_name=u'Descriptions', blank=True, null=True)

    # Compatibilidad con ViewDefinition
    active = models.BooleanField(default=True)
    overWrite = models.BooleanField(default=False)

    metaDefinition = JSONField(default={})

    objects = ProtoUserManager()

    def __str__(self):
        return self.code

    class Meta:
        unique_together = ('code', 'smOwningUser', )

    protoExt = {
        "gridConfig" : {
            "listDisplay": ["__str__", "description", "smOwningUser"]
        }
    }


# --  Load fixture problem PK Conflict, marcar raw !!!   
from django.db.models.signals import post_save
from protoLib.models import UserContext
from protoExt.signals import context2customdefinition 
 
post_save.connect(context2customdefinition, sender = UserContext)
