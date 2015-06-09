# -*- coding: utf-8 -*-

# TODO: Django’s comments, log, taggit  

import django


from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.utils.functional import lazy


# Django 1.5+ compatibility
if django.VERSION >= (1, 5):
    AUTH_USER_MODEL = settings.AUTH_USER_MODEL
    try:
        from django.contrib.auth import get_user_model
        User = lazy(get_user_model, AUTH_USER_MODEL)
    except ImproperlyConfigured:
        pass
else:
    AUTH_USER_MODEL = 'auth.User'
    from django.contrib.auth.models import User
    

from .smbase import *
from .protomodel import * 
from .protorepos import * 
from .protoutils import * 
from .protowf0 import * 
