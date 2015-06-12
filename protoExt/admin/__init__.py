# -*- coding: utf-8 -*-

from django.contrib  import admin
from reversion.helpers import patch_admin
import reversion

from protoExt.models import ViewDefinition, CustomDefinition


admin.site.register(ViewDefinition)
admin.site.register(CustomDefinition)

patch_admin(ViewDefinition)
patch_admin(CustomDefinition)


# -----------------------------------------   AddUser  

from protoExt.actionsusr import doAddUser 
from protoLib.models import UserProfile

class UserProfileAdmin( reversion.VersionAdmin ):
    actions = [ doAddUser ]

try: 
    admin.site.unregister( UserProfile ) 
    admin.site.register( UserProfile, UserProfileAdmin )
except: 
    pass 
