# -*- coding: utf-8 -*-

from django.contrib  import admin
from reversion.helpers import patch_admin
import reversion


# -----------------------------------------   AddUser  

from django.contrib.auth.models import User, Group 
patch_admin(User)
patch_admin(Group)

from protoLib.models import UserProfile
from .adminUserProf import UserProfileAdmin
 
admin.site.register( UserProfile, UserProfileAdmin )

# -----------------------------------------     

from protoLib.models import ProtoDefinition
from .adminProtoDef import protoDefinitionAdmin
admin.site.register(ProtoDefinition, protoDefinitionAdmin)

# -----------------------------------------     


from protoLib.models import TeamHierarchy
admin.site.register(TeamHierarchy)
patch_admin(TeamHierarchy)

# -----------------------------------------     

from protoLib.models import CustomDefinition
admin.site.register(CustomDefinition)
patch_admin(CustomDefinition)
 
# -----------------------------------------     

from protoLib.models import EntityMap
class EntityMapAdmin(reversion.VersionAdmin):
    pass
 
admin.site.register(EntityMap, EntityMapAdmin)
 
 
# de aut
# from django.contrib.auth.models import Permission, Message
# admin.site.register( Permission )
# admin.site.register( Message )
 

 
 
# from protoLib.models import  PtFunction
# admin.site.register(PtFunction)
# from protoLib.models import EntityMap, FieldMap
# admin.site.register(EntityMap)
# admin.site.register(FieldMap)
 
 
# -----------------------------------------   WflowAdminResume
#  
# from protoLib.actions import doWFlowResume
# from protoLib.models import WflowAdminResume
#  
# class WflowAdminResumeAdmin(admin.ModelAdmin):
#     actions = [ doWFlowResume, ]
#  
# admin.site.register(WflowAdminResume, WflowAdminResumeAdmin)
#  
# # -----------------------------------------   Log 
#  
# from protoLib.actions import doClearLog 
# from protoLib.models import Logger
#  
# class LoggerAdmin( admin.ModelAdmin ):
#     actions = [ doClearLog ]
#  
# admin.site.register(Logger, LoggerAdmin )
 
 
