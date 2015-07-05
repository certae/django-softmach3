# # -*- coding: utf-8 -*-
# 
# from django.db import models
# from protoLib.models import * 
# 
# 
# class WflowAdminResume(ProtoModelExt):
#     """ Contains the latest news summary that require administrator action
#         When creating a record of WFlow you can create an instance of this table or increment the counter
#         You will also have to go shares wFlow tables (parameter = wFlowEntities)
#         and tell the states to verify (parameterTag = 0)
#     """
# 
#     viewEntity = models.CharField(max_length=250 , blank=False, null=False)
#     activityCount = models.IntegerField(blank=False, null=False)
# 
#     def __str__(self):
#         return self.viewEntity + '.' + self.smOwningTeam.__str__()
# 
#     protoExt = {
#         "actions": [
#             { "name": "doWFlowResume",
#               "selectionMode" : "none",
#               "refreshOnComplete" : True
#             },
#         ]
#     }
# 
# 
# class WflowUserReponse(ProtoModelExt):
#     """ Contains the results of administrator actions
#     """
# 
#     viewEntity = models.CharField(max_length=250 , blank=False, null=False)
#     wfAction = models.CharField(max_length=250 , blank=False, null=False)
#     strKey = models.CharField(max_length=250 , blank=False, null=False)
#     adminMsg = models.CharField(max_length=250 , blank=False, null=False)
# 
#     def __str__(self):
#         return self.viewEntity
# 
# 
# class UserFiles(ProtoModelExt):
#     
#     docfile = models.FileField(upload_to='media/%Y/%m/%d')
#     description = models.TextField(verbose_name=u'Description', blank=True, null=True)
# 
# 
# 
# class DiscreteValue(models.Model):
#     # TODO : Manejo de discretas
#     # Ahora se hace como un arbol para por ejemplo manejar el idioma fr.ca  es.ca
#     # Arrancar con filtro inicial discreteValue = None
# 
#     code = models.CharField(blank=False, null=False, max_length=200)
#     value = models.CharField(blank=False, null=False, max_length=200)
# 
#     description = models.TextField(blank=True, null=True)
#     title = models.ForeignKey('DiscreteValue', blank=True, null=True)
# 
#     def __str__(self):
#         if self.title is None:
#             return self.code
#         else:
#             return self.title.code + '.' + self.code
# 
#     class Meta:
#         unique_together = ('title', 'value',)
# 
#     protoExt = {
#         "gridConfig" : {
#             "listDisplay": ["__str__", "description" ]
#         }
#     }
# 
# 
# 
# 
# class PtFunction(models.Model):
#     """ 
#     En esta tabla se guardan funciones q seran ejectudas dinamicamente
#     deben reespetar la syntaxis python y se precargaran con funcione de base 
#     por ejemplo el perfil de usuario y el acceso a modelos 
#     
#     Siempre debe retornar algo
#     """
# 
#     # nombre de la funcion
#     code = models.CharField(blank=False, null=False, max_length=200 , unique=True)
# 
#     # este modelo se importa y se ofrece a la funcion
#     modelName = models.CharField(blank=False, null=False, max_length=200)
# 
#     # lista separada por comas de los nombres de los argumentos
#     arguments = models.CharField(blank=False, null=False, max_length=400)
# 
#     functionBody = models.TextField(blank=True, null=True)
# 
#     tag = models.CharField(blank=False, null=False, max_length=200)
#     description = models.TextField(verbose_name=u'Descriptions', blank=True, null=True)
# 
# 
#     def __str__(self):
#         return self.code + '.' + self.tag
# 
# 
# 
