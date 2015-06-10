# -*- coding: utf-8 -*-

from django.db import models
from protoLib.models import * 


class WflowAdminResume(ProtoModelExt):
    """ Contains the latest news summary that require administrator action
        When creating a record of WFlow you can create an instance of this table or increment the counter
        You will also have to go shares wFlow tables (parameter = wFlowEntities)
        and tell the states to verify (parameterTag = 0)
    """

    viewEntity = models.CharField(max_length=250 , blank=False, null=False)
    activityCount = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return self.viewEntity + '.' + self.smOwningTeam.__str__()

    protoExt = {
        "actions": [
            { "name": "doWFlowResume",
              "selectionMode" : "none",
              "refreshOnComplete" : True
            },
        ]
    }


class WflowUserReponse(ProtoModelExt):
    """ Contains the results of administrator actions
    """

    viewEntity = models.CharField(max_length=250 , blank=False, null=False)
    wfAction = models.CharField(max_length=250 , blank=False, null=False)
    strKey = models.CharField(max_length=250 , blank=False, null=False)
    adminMsg = models.CharField(max_length=250 , blank=False, null=False)

    def __str__(self):
        return self.viewEntity



class Pruebas2(ProtoModelExt):
    """ Contains the results of administrator actions
    """

    code = models.CharField(max_length=250 , blank=False, null=False)
#     objects = ProtoManager()


    def __str__(self):
        return self.code
