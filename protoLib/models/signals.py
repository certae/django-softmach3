# -*- coding: utf-8 -*-

from .smbase import UserProfile, TeamHierarchy


def user_post_save(sender, instance, created, **kwargs):
    """
    DEPRECATED : No es necesaria, el primer login o adduser la crean por defecto 
    Create a user profile when a new user account is created
    """
    if created == True:
        p = UserProfile()
        p.user = instance
        p.save()


def login_teamtree_update(sender, user, **kwargs):
    """
    Update treehierarchy when a user login 
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


