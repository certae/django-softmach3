# -*- coding: utf-8 -*-

from django.contrib import admin
from protoLib.actions import doCopyVersion, doDeleteVersion  


class VersionAdm( admin.ModelAdmin ):
    actions = [ doCopyVersion, doDeleteVersion ]
