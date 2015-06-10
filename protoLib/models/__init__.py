# -*- coding: utf-8 -*-

from .usermodel import User, AUTH_USER_MODEL

from .smbase import TeamHierarchy, UserProfile 
from .protomodel import ProtoModelBase, ProtoModelExt
from .protorepos import ProtoDefinition, CustomDefinition

# from .protoutils import 
# from .protowf0 import 

# ---------  SIGNALS 

from .signals import user_post_save, login_teamtree_update 

from django.db.models.signals import post_save
post_save.connect(user_post_save, sender=AUTH_USER_MODEL)

from django.contrib.auth.signals import user_logged_in 
user_logged_in.connect(login_teamtree_update)


# TODO: Django’s comments, log, taggit  
