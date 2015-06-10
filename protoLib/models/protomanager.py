# -*- coding: utf-8 -*-

from django.db import models
from protoLib.models import UserProfile 
from protoLib.middleware import CurrentUserMiddleware


def getUserProfile( cuser): 
    return UserProfile.objects.get_or_create( user = cuser)[0]

def getUserTeam( cuser): 
    return getUserProfile( cuser ).userTeam 



class ProtoManager(models.Manager):

   
    def get_queryset(self):
        cuser = CurrentUserMiddleware.get_user()

        Qs = super(ProtoManager, self).get_queryset() 
        
        if cuser.is_superuser :
            return Qs
            
        if not cuser.has_perm( "%s.%s_%s" % ( self.model._meta.app_label, 'list', self.model._meta.model_name )):
            return Qs.none()  

        userProfile = getUserProfile( cuser)
        return Qs.filter(smOwningTeam__in=  userProfile.userTree.split(',') )

    