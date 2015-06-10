# -*- coding: utf-8 -*-


from django.db import models
from jsonfield2.managers import JSONAwareQuerySet

from protoLib.middleware import CurrentUserMiddleware
from .smbase import UserProfile 

class ProtoManager(models.Manager):

 
    def get_queryset(self):
        cuser = CurrentUserMiddleware.get_user( False )

        Qs = super(ProtoManager, self).get_queryset() 
        
        if not cuser or cuser.is_superuser :
            return Qs
            
        if not cuser.has_perm( "%s.%s_%s" % ( self.model._meta.app_label, 'list', self.model._meta.model_name )):
            return Qs.none()  

        userProfile = UserProfile.objects.get_or_create( user = cuser)[0]
        return Qs.filter(smOwningTeam__in=  userProfile.userTree.split(',') )



class ProtoJSONManager(ProtoManager):
     
    def __init__(self, json_fields=[], *args, **kwargs):
        self.json_fields = json_fields
        super(ProtoJSONManager, self).__init__(*args, **kwargs)
 
    def get_queryset(self):
        return JSONAwareQuerySet(self.json_fields, self.model)    