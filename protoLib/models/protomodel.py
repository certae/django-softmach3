# -*- coding: utf-8 -*-

from django.db import models
from jsonfield2 import JSONField
from .usermodel import AUTH_USER_MODEL

from protoLib.models import TeamHierarchy 
from protoLib.middleware import CurrentUserMiddleware
from protoLib.getStuff import getUserTeam

from .protomanager import ProtoManager, ProtoJSONManager

import uuid 


smControlFields = [
    'smOwningUser', 'smOwningTeam', 'smOwningUser_id', 'smOwningTeam_id', \
    'smCreatedBy',  'smModifiedBy', 'smCreatedBy_id',  'smModifiedBy_id', \
    'smCreatedOn', 'smModifiedOn', \
    'smWflowStatus', 'smRegStatus', \
    'smNaturalCode', 'smUUID']

class ProtoModelBase(models.Model):
    """
    Tabla modelo para la creacion de entidades de usuario     ( sm  security mark )
    related_name="%(app_label)s_%(class)s"
    """ 

    smNaturalCode = models.CharField(max_length=50, null=True, blank=True, editable=True)
    smRegStatus = models.CharField(max_length=50, null=True, blank=True, editable=False)
    smWflowStatus = models.CharField(max_length=50, null=True, blank=True, editable=False)

    smOwningUser = models.ForeignKey(AUTH_USER_MODEL, null=True, blank=True, related_name='+', editable=False)
    smOwningTeam = models.ForeignKey(TeamHierarchy, null=True, blank=True, related_name='+', editable=False)

    smCreatedBy = models.ForeignKey(AUTH_USER_MODEL, null=True, blank=True, related_name='+', editable=False)
    smModifiedBy = models.ForeignKey(AUTH_USER_MODEL, null=True, blank=True, related_name='+', editable=False)

    smCreatedOn = models.DateTimeField( auto_now_add =True, editable=False, null=True, blank=True )
    smModifiedOn = models.DateTimeField( auto_now =True, editable=False, null=True, blank=True)

    smUUID = models.UUIDField( default=uuid.uuid4, editable=False)

    objects = ProtoManager()

    # Security indicator used to control permissions
    _protoObj = True

    class Meta:
        abstract = True

        # https://docs.djangoproject.com/en/1.8/ref/models/options/#permissions
        permissions = (
            ("list_%(class)", "Can list available %(class)s"),
        )
        
    def save(self, *args, **kwargs):
        # Disabled for loaddata
        isNew = kwargs.get('created', True) 
        isRaw = kwargs.get('raw', False)          

        if not isRaw :
            cuser = CurrentUserMiddleware.get_user( False )
            
            if not self.smNaturalCode:
                self.smNaturalCode - self.__str__()
                 
            if cuser: 
                setattr(self, 'smModifiedBy', cuser)
    
                # Insert not self.pk:
                if isNew:   
                    setattr(self, 'smCreatedBy', cuser)
                    setattr(self, 'smOwningUser', cuser)
                    setattr(self, 'smOwningTeam', getUserTeam( cuser))
        
        super(ProtoModelBase, self).save(*args, **kwargs)


class ProtoModelExt(ProtoModelBase):
    """
    Tabla modelo para la creacion de entidades de usuario  ( sm  security mark )
    Con manejo de campos json 
    """ 

    smInfo = JSONField(default={})
    objects = ProtoJSONManager(json_fields = ['smInfo'])

    _protoJson = True

    class Meta:
        abstract = True



        