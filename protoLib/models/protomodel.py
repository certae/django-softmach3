# -*- coding: utf-8 -*-

from django.db import models
from jsonfield2 import JSONField, JSONAwareManager
from protoLib.models import TeamHierarchy
from django.contrib.auth.models import User

import uuid 


class ProtoModelBase(models.Model):
    """
    Tabla modelo para la creacion de entidades de usuario     ( sm  security mark )
    related_name="%(app_label)s_%(class)s
    """ 

    smOwningUser = models.ForeignKey(User, null=True, blank=True, related_name='+', editable=False)
    smOwningTeam = models.ForeignKey(TeamHierarchy, null=True, blank=True, related_name='+', editable=False)

    smCreatedBy = models.ForeignKey(User, null=True, blank=True, related_name='+', editable=False)
    smModifiedBy = models.ForeignKey(User, null=True, blank=True, related_name='+', editable=False)

    smRegStatus = models.CharField(max_length=50, null=True, blank=True, editable=False)
    smWflowStatus = models.CharField(max_length=50, null=True, blank=True, editable=False)

    smCreatedOn = models.DateTimeField( auto_now_add =True, editable=False, null=True, blank=True )
    smModifiedOn = models.DateTimeField( auto_now =True, editable=False, null=True, blank=True)

    smUUID = models.UUIDField( default=uuid.uuid4, editable=False)

    # Security indicator used to control permissions
    _protoObj = True

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        pass 
        super(ProtoModel, self).save(*args, **kwargs)




class ProtoModel(ProtoModelBase):
    """
    Tabla modelo para la creacion de entidades de usuario  ( sm  security mark )
    Con manejo de campos json 
    """ 

    metaDefinition = JSONField(default={})
    objects = JSONAwareManager(json_fields = ['metaDefinition'])


    class Meta:
        abstract = True

