

from .protomodel import ProtoModelBase 
from django.contrib.contenttypes.models import ContentType
from django.db import models
from protoLib.models.protomanager import UserPermissionManager


class ContextVar(ProtoModelBase):

    modelCType = models.OneToOneField(ContentType, unique=True, blank=False, null=False)

    # Default name for var      
    propName = models.CharField(blank=False, null=False, max_length=500, default = '')
    propDescription = models.TextField(blank=True, null=True)

    # Legacy ( all true ) 
    isDefault = models.BooleanField(default=True) 
    isFilter = models.BooleanField(default=True) 

    # Dont use Versioning      
    _useVersion = False 


    def __str__(self):
        return "%s" % ( self.modelCType.__str__() )   
    
    protoExt = { 
        "gridConfig" : {
            "listDisplay": ["__str__", "propName", "propDescription" ]      
        }
    } 



class ContextEntity(ProtoModelBase):

    contextVar = models.ForeignKey(ContextVar, blank=False, null=False)
    entity = models.ForeignKey(ContentType, blank=False, null=False)

    # Default name for var      
    propName = models.CharField(blank=True, null=True, max_length=200, default = '')
    active = models.BooleanField(default=True) 

    # Dont use Versioning      
    _useVersion = False 
    

    def __str__(self):
        return "%s %s" % ( self.modelCType.__str__(), self.entity.__str__() )   
    
    protoExt = { 
        "gridConfig" : {
            "listDisplay": ["__str__", "propName" ]      
        }
    } 

    class Meta:
        unique_together = ('contextVar', 'entity' )



class ContextUser(ProtoModelBase):

    contextVar = models.ForeignKey(ContextVar, blank=False, null=False)

    # Default name for var
    propValue = models.CharField(blank=False, null=False, max_length=200)      
    active = models.BooleanField(default=True) 

    # Dont use Versioning      
    _useVersion = False 

    objects = UserPermissionManager()
    

    def __str__(self):
        return "%s %s" % ( self.modelCType.__str__(), self.propValue )   
    
    protoExt = { 
        "gridConfig" : {
            "listDisplay": ["__str__", "propValue"  ]      
        }
    } 

    class Meta:
        unique_together = ('contextVar', 'smOwningUser'  )


