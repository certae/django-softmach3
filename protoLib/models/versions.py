'''
Created on Feb 1, 2016

@author: dario
'''


from .protomodel import ProtoModelBase 
from django.db import models
from .usermodel import AUTH_USER_MODEL


class VersionTitle(models.Model):
    """
    """
    versionCode = models.CharField(max_length=50, null=True, blank=True, editable=False, default = '0')

    versionBase = models.CharField(max_length=50, null=True, blank=True, editable=False, default = '0')
    description = models.TextField(verbose_name=u'Descriptions', blank=True, null=True)

    smCreatedBy = models.ForeignKey(AUTH_USER_MODEL, null=True, blank=True, related_name='+', editable=False)
    smCreatedOn = models.DateTimeField( auto_now_add =True, editable=False, null=True, blank=True )

    smModifiedBy = models.ForeignKey(AUTH_USER_MODEL, null=True, blank=True, related_name='+', editable=False)
    smModifiedOn = models.DateTimeField( auto_now =True, editable=False, null=True, blank=True)

    smRegStatus = models.CharField(max_length=50, null=True, blank=True, editable=False)


    def __str__(self):
        return "%s %s" % ( self.versionCode )   
    
    protoExt = { 
        "gridConfig" : {
            "listDisplay": ["__str__", "description", "smCreatedBy"]      
        }
    } 


