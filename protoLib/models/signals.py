# -*- coding: utf-8 -*-

from protoLib.models import UserProfile, TeamHierarchy
from django.contrib.auth.models import User


def user_post_save(sender, instance, created, **kwargs):
    """Create a user profile when a new user account is created"""
    if created == True:
        p = UserProfile()
        p.user = instance
        p.save()

from django.db.models.signals import post_save
post_save.connect(user_post_save, sender=User)



def login_teamtree_update(sender, user, **kwargs):
    """
    A signal receiver which updates the treehierarchy.
    """
    uProfile = UserProfile.objects.get_or_create(user = user )[0]

    if uProfile.userTeam is None:
        # verifica el grupo  ( proto por defecto )
        uProfile.userTeam = TeamHierarchy.objects.get_or_create(code='proto')[0]
        uProfile.save()

    uOrgTree = uProfile.userTeam.treeHierarchy

#     # TODO: permisos adicionales, probar 
#     for item in pUser.usershare_set.all() :
#         uOrgTree += ',' + item.userTeam.treeHierarchy

    # Organiza los ids
    uProfile.userTree = ','.join(set(uOrgTree.split(',')))
    uProfile.save()


from django.contrib.auth.signals import user_logged_in 
user_logged_in.connect(login_teamtree_update)

