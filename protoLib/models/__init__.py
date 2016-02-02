# -*- coding: utf-8 -*-

from .usermodel import User, AUTH_USER_MODEL

from .smbase import TeamHierarchy, UserProfile, EntityMap
from .protomodel import ProtoModelBase, ProtoModelExt
from .protomanager import ProtoJSONManager
from .protoContext import UserContext 
from .versions import VersionTitle  


# ---------  SIGNALS 

from .signals import user_post_save, login_teamtree_update 

# --  Load fixture problem PK Conflict  
# from django.db.models.signals import post_save
# post_save.connect(user_post_save, sender=AUTH_USER_MODEL)

from django.contrib.auth.signals import user_logged_in 
user_logged_in.connect(login_teamtree_update)

