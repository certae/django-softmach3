# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from datascripts.protoExt import BasicImportHelper

importer = BasicImportHelper()

def createAuthBase():
    """
    Usr1 : admin 
    Usr2 : group base con todos los permisos 
    Usr3 : no permissions 
    """

    from django.contrib.auth.models import Group, Permission

    auth_group_1 = Group()
    auth_group_1.name = 'base'
    auth_group_1.save()

    for perm in Permission.objects.all(): 
        auth_group_1.permissions.add( perm )


    # Usr1 : admin 
    auth_user_1 = User()
    auth_user_1.username = 'A'
    auth_user_1.email = 'dariogomezt@gmail.com'
    auth_user_1.is_superuser = True
    auth_user_1.is_staff = True
    auth_user_1.is_active = True
    auth_user_1.password = 'x'
    auth_user_1.save()

    # Usr2 : group base with all permissions   
    auth_user_2 = User()
    auth_user_2.username = 'B'
    auth_user_2.email = ''
    auth_user_2.is_superuser = False
    auth_user_2.is_staff = True
    auth_user_2.is_active = True
    auth_user_2.password = 'x'
    auth_user_2.save()

    auth_user_2.groups.add(auth_group_1)

    # Usr3 : group base with not permissions   
    auth_user_3 = User()
    auth_user_3.username = 'C'
    auth_user_3.is_superuser = False
    auth_user_3.is_staff = True
    auth_user_3.is_active = True
    auth_user_3.password = 'x'
    auth_user_3.save()


def createAuthExt():

    # Processing model: TeamHierarchy

    from protoLib.models.smbase import TeamHierarchy

    protoLib_teamhierarchy_1 = TeamHierarchy()
    protoLib_teamhierarchy_1.code = 'A'
    protoLib_teamhierarchy_1.parentNode = None
    protoLib_teamhierarchy_1.save()

    protoLib_teamhierarchy_2 = TeamHierarchy()
    protoLib_teamhierarchy_2.code = 'A.1'
    protoLib_teamhierarchy_2.parentNode = protoLib_teamhierarchy_1
    protoLib_teamhierarchy_2.save()

    protoLib_teamhierarchy_3 = TeamHierarchy()
    protoLib_teamhierarchy_3.code = 'B'
    protoLib_teamhierarchy_3.parentNode = None
    protoLib_teamhierarchy_3.save()

    # Processing model: UserProfile

    from protoLib.models.smbase import UserProfile

    protoLib_userprofile_1 = UserProfile()
    protoLib_userprofile_1.user =  importer.locate_object(User, "id", User, "id", 1) 
    protoLib_userprofile_1.userTeam = protoLib_teamhierarchy_1
    protoLib_userprofile_1.language = None
#     protoLib_userprofile_1.userTree = '1,2'
    protoLib_userprofile_1.userConfig = {}
    protoLib_userprofile_1 = importer.save_or_locate(protoLib_userprofile_1)

    protoLib_userprofile_2 = UserProfile()
    protoLib_userprofile_2.user =  importer.locate_object(User, "id", User, "id", 2) 
    protoLib_userprofile_2.userTeam = protoLib_teamhierarchy_2
    protoLib_userprofile_2.language = ''
#     protoLib_userprofile_2.userTree = '2'
    protoLib_userprofile_2.userConfig = {}
    protoLib_userprofile_2 = importer.save_or_locate(protoLib_userprofile_2)

    protoLib_userprofile_3 = UserProfile()
    protoLib_userprofile_3.user =  importer.locate_object(User, "id", User, "id", 3) 
    protoLib_userprofile_3.userTeam = protoLib_teamhierarchy_3
    protoLib_userprofile_3.language = ''
#     protoLib_userprofile_3.userTree = '3'
    protoLib_userprofile_3.userConfig = {}
    protoLib_userprofile_3 = importer.save_or_locate(protoLib_userprofile_3)
    
    