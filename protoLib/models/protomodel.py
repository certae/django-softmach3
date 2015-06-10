# -*- coding: utf-8 -*-

from django.db import models
from jsonfield2 import JSONField, JSONAwareManager
from django.contrib.auth.models import User

from protoLib.models import TeamHierarchy 
from protoLib.middleware import CurrentUserMiddleware

from .protomanager import getUserTeam, ProtoManager 

import uuid 


class ProtoModelBase(models.Model):
    """
    Tabla modelo para la creacion de entidades de usuario     ( sm  security mark )
    related_name="%(app_label)s_%(class)s"
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

    objects = ProtoManager()

    # Security indicator used to control permissions
    _protoObj = True

    class Meta:
        abstract = True
        permissions = (
            ("list_%(class)", "Can list available %(class)s"),
        )
        
    def save(self, *args, **kwargs):
        user = CurrentUserMiddleware.get_user()
        setattr(self, 'smModifiedBy', user)

        # Insert 
        if not self.pk:
            setattr(self, 'smCreatedBy', user)
            setattr(self, 'smOwningUser', user)
            setattr(self, 'smOwningTeam', getUserTeam( user))
        
        super(ProtoModelBase, self).save(*args, **kwargs)


class ProtoModel(ProtoModelBase):
    """
    Tabla modelo para la creacion de entidades de usuario  ( sm  security mark )
    Con manejo de campos json 
    """ 

    metaDefinition = JSONField(default={})
    objects = JSONAwareManager(json_fields = ['metaDefinition'])


    class Meta:
        abstract = True



    