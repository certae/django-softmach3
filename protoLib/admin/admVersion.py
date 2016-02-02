# -*- coding: utf-8 -*-

from django.contrib import admin
from protoLib.actions import doCreateVersion, doDeleteVersion  


class VersionAdm( admin.ModelAdmin ):
    actions = [ doCreateVersion, doDeleteVersion ]
