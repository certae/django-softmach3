# -*- coding: utf-8 -*-

from django.contrib  import admin
from reversion.helpers import patch_admin

# -----------------------------------------     

from protoExt.models import ViewDefinition
admin.site.register(ViewDefinition)
patch_admin(ViewDefinition)

# -----------------------------------------     

from .models import CustomDefinition
admin.site.register(CustomDefinition)
patch_admin(CustomDefinition)

# -----------------------------------------     
