# -*- coding: utf-8 -*-

from django.db import models
from protoLib.models.usermodel import AUTH_USER_MODEL
from protoLib.getmodels import getNodeHierarchy 

from jsonfield2 import JSONField, JSONAwareManager


class TeamHierarchy(models.Model):
    """
    Jerarquia funcional ( de seguridad ) de la app
    Es la base de la seguridad por registro
    """
    code = models.CharField(unique=True, blank=False, null=False, max_length=200)
    description = models.TextField(verbose_name=u'Descriptions', blank=True, null=True)
    parentNode = models.ForeignKey('TeamHierarchy', blank=True, null=True , related_name='downHierachy')
    site = models.IntegerField(blank=True, null=True)

    @property
    def fullPath(self):
        return getNodeHierarchy(self , 'parentNode', 'id', 'fullPath')

    @property
    def treeHierarchy(self):
        "Returns the full down-hierarchy"
        sTree = str(self.id)
        for item in self.downHierachy.all() :
            sTree += ',' + item.treeHierarchy
        return sTree

    def __str__(self):
        return self.code

    protoExt = { 'fields' : {
          'fullPath': {'readOnly' : True},
          'treeHierarchy': {'readOnly' : True},
     }}



# here is the profile model
class UserProfile(models.Model):
    """
    Es necesario inlcuir el ususario en un BUnit, cada registro copiara el Bunit
    del usuario para dar permisos tambien a la jerarquia ( ascendente )
    """

    
    user = models.OneToOneField(AUTH_USER_MODEL, unique=True)
    userTeam = models.ForeignKey(TeamHierarchy, blank=True, null=True, related_name='userTeam')
    language = models.CharField(blank=True, null=True, max_length=500)

    # System generated hierachie 
    userTree = models.CharField(blank=True, null=True, max_length=500)

    # DGT : Json space, preferencias de usuario ( menuClick, defaultVariables ..... )
    userConfig = JSONField(default={})
    objects = JSONAwareManager(json_fields = ['userConfig'])

    
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
        ], 
    }

    def __str__(self):
        return  self.user.username


