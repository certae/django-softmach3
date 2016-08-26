# -*- coding: utf-8 -*-

from django.contrib  import admin
from reversion.helpers import patch_admin
import reversion

from protoExt.models import ViewDefinition, CustomDefinition


admin.site.register(ViewDefinition)
admin.site.register(CustomDefinition)

patch_admin(ViewDefinition)
patch_admin(CustomDefinition)



from protoExt.actions import doSetContext
admin.site.add_action(doSetContext)


# -----------------------------------------   AddUser  

from protoExt.actions import doAddUser, doAddUsers 
from protoLib.models import UserProfile

class UserProfileAdmin( reversion.VersionAdmin ):
    actions = [ doAddUser, doAddUsers ]

    protoExt = {
        "actions": [
            { "name": "doAddUser",
              "selectionMode" : "none",
              "refreshOnComplete" : True,
              "actionParams": [
                 {"name" : "User", "type" : "string", "required": True, "tooltip" : "UserName" }, 
                 {"name" : "Pwd", "type" : "string", "required": False, "tooltip" : "Pwd" }, 
                 {"name" : "EMail", "type" : "string", "required": False, "tooltip" : "Email" }, 
                 {"name" : "Team", "type" : "string", "required": False, "tooltip" : "Tean" }, 
                 {"name" : "Groups", "type" : "string", "required": False, "tooltip" : "gr1,gr2,..." }, 
                ] 
            },
            { "name": "doAddUsers",
              "selectionMode" : "none",
              "refreshOnComplete" : True,
              "actionParams": [
                 {"name" : "Users", "type" : "text", "required": True, "tooltip" : "Usr, Pwd, email, team, group1, .. group(n)" }, 
                ] 
            },
        ], 
    }
    

try: 
    admin.site.unregister( UserProfile ) 
except: 
    pass 

admin.site.register( UserProfile, UserProfileAdmin )
