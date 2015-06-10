# -*- coding: utf-8 -*-

from django.contrib  import admin
from protoLib.models import User, AUTH_USER_MODEL


# -----------------------------------------   AddUser  

from protoLib.models import UserProfile
from .adminUserProf import UserProfileAdmin
 
admin.site.register( UserProfile, UserProfileAdmin )


# -----------------------------------------     

from protoLib.models import ProtoDefinition, TeamHierarchy
from protoLib.models import CustomDefinition

 
from .adminProtoDef import protoDefinitionAdmin
from .adminOrgTree import orgTreeAdmin

 
admin.site.register(ProtoDefinition, protoDefinitionAdmin)
admin.site.register(TeamHierarchy)
admin.site.register(CustomDefinition)

 
from .adminUsr import AdminUser
User.protoExt = AdminUser
 
 
# de aut
# from django.contrib.auth.models import Permission, Message
# admin.site.register( Permission )
# admin.site.register( Message )
 
 
from django.contrib.contenttypes.models import ContentType
admin.site.register(ContentType)
 
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
 
 
