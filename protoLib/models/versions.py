'''
Created on Feb 1, 2016

@author: dario
'''


from django.db import models
from .usermodel import AUTH_USER_MODEL
from protoLib.middleware import CurrentUserMiddleware
from django.contrib.contenttypes.models import ContentType


class VersionTitle(models.Model):
    """
    """
    versionCode = models.CharField(max_length=50, null=True, blank=True, editable=True, default='0')

    versionBase = models.ForeignKey('VersionTitle', null=True, blank=True, )
    description = models.TextField( verbose_name=u'Descriptions', blank=True, null=True)
    active = models.BooleanField(default=True)

    smCreatedBy = models.ForeignKey(AUTH_USER_MODEL, null=True, blank=True, related_name='+', editable=False)
    smCreatedOn = models.DateTimeField(auto_now_add=True, editable=False, null=True, blank=True)

    smModifiedBy = models.ForeignKey(AUTH_USER_MODEL, null=True, blank=True, related_name='+', editable=False)
    smModifiedOn = models.DateTimeField(auto_now=True, editable=False, null=True, blank=True)

    def __str__(self):
        return "%s %s" % (self.versionCode)

    protoExt = {
        "gridConfig": {
            "listDisplay": ["__str__", "description", "smCreatedBy"]
        }
    }

    def save(self, *args, **kwargs):

        cuser = CurrentUserMiddleware.get_user(False)

        if cuser:
            setattr(self, 'smModifiedBy', cuser)

            # Insert
            if not self.pk:
                setattr(self, 'smCreatedBy', cuser)

        super(VersionTitle, self).save(*args, **kwargs)


class VersionHeaders(models.Model):
    """
    Para poder buscar las entidades, hay q comenzar por los padres  
    """

    modelCType = models.ForeignKey(ContentType, blank=False, null=False)

    def __str__(self):
        return "%s %s" % (self.modelCType.__str__())
