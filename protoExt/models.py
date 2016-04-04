# -*- coding: utf-8 -*-

from django.db import models
from jsonfield2 import JSONField, JSONAwareManager

from protoLib.models.protomodel import ProtoModelBase, ProtoModelExt
from protoLib.models.protomanager import UserPermissionManager


"""
DGT: Repositorios para manejo definiciones  
"""


class Parameters(ProtoModelExt):
    """
    System parameters 
    """
    parameterKey = models.CharField(max_length=250 , blank=False, null=False)
    parameterTag = models.CharField(max_length=250 , blank=True, null=True)
    parameterValue = models.CharField(max_length=250 , blank=False, null=False)

    def __str__(self):
        return self.parameterKey + '.' + self.parameterValue


class ViewDefinition(models.Model):
    """
    This table stores the definitions of pcls, is a generic container to handle the definition of views.
    Therefore it should not depend on the user (team) because it is the definition of the application. 
    It is important to keep the different versions, use ** ** reversion in admin
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
    custom menus  and CustomOptions
    The difference vs userProfile  is that here there are several records by key
    """

    code = models.CharField(blank=False, null=False, max_length=200)
    description = models.TextField(verbose_name=u'Descriptions', blank=True, null=True)

    # Compatibilidad con ViewDefinition
    active = models.BooleanField(default=True)
    overWrite = models.BooleanField(default=False)

    metaDefinition = JSONField(default={})

    objects = UserPermissionManager()

    def __str__(self):
        return self.code

    class Meta:
        unique_together = ('code', 'smOwningUser' )

    protoExt = {
        "gridConfig" : {
            "listDisplay": ["__str__", "description", "smOwningUser"]
        }
    }


# --  Load fixture problem PK Conflict, marcar raw !!!   
from django.db.models.signals import post_save

# from protoLib.models import ContextUser
# from protoExt.signals import context2customdefinition 
# post_save.connect(context2customdefinition, sender = ContextUser)


