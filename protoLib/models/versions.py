'''
Created on Feb 1, 2016

@author: dario
'''


from django.db import models
from django.contrib.contenttypes.models import ContentType
from protoLib.models.protomodel import ProtoModelBase


class VersionTitle(ProtoModelBase):
    """
    """
    versionCode = models.CharField(max_length=50, null=True, blank=True, editable=True, default='0')
    versionBase = models.ForeignKey('self', null=True, blank=True, )

    description = models.TextField( verbose_name=u'Descriptions', blank=True, null=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True

    def __str__(self):
        return "%s" % (self.versionCode)

    protoExt = {
        "gridConfig": {
            "listDisplay": ["__str__", "description", "smCreatedBy"]
        }, 
        "actions": [
            { "name": "doCopyVersion", "selectionMode" : "single"}, 
            { "name": "doDeleteVersion", "selectionMode" : "single"}, 
        ],
                
    }



class VersionHeader(ProtoModelBase):
    """
    Entity list for include or exclude in versioning 
    """

    modelCType = models.ForeignKey(ContentType, blank=False, null=False)
    exclude = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def __str__(self):
        return "%s" % (self.modelCType.__str__())

