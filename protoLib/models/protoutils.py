# -*- coding: utf-8 -*-

from django.db import models
from protoLib.models import * 
from datetime import datetime 

class UserFiles(ProtoModel):
    
    docfile = models.FileField(upload_to='media/%Y/%m/%d')
    description = models.TextField(verbose_name=u'Description', blank=True, null=True)



class DiscreteValue(models.Model):
    # TODO : Manejo de discretas
    # Ahora se hace como un arbol para por ejemplo manejar el idioma fr.ca  es.ca
    # Arrancar con filtro inicial discreteValue = None

    code = models.CharField(blank=False, null=False, max_length=200)
    value = models.CharField(blank=False, null=False, max_length=200)

    description = models.TextField(blank=True, null=True)
    title = models.ForeignKey('DiscreteValue', blank=True, null=True)

    def __str__(self):
        if self.title is None:
            return self.code
        else:
            return self.title.code + '.' + self.code

    class Meta:
        unique_together = ('title', 'value',)

    protoExt = {
        "gridConfig" : {
            "listDisplay": ["__str__", "description" ]
        }
    }



class ParametersBase(ProtoModel):
    parameterKey = models.CharField(max_length=250 , blank=False, null=False)
    parameterTag = models.CharField(max_length=250 , blank=False, null=False)
    parameterValue = models.CharField(max_length=250 , blank=False, null=False)

    def __str__(self):
        return self.parameterKey + '.' + self.parameterValue



class PtFunction(models.Model):
    """ 
    En esta tabla se guardan funciones q seran ejectudas dinamicamente
    deben reespetar la syntaxis python y se precargaran con funcione de base 
    por ejemplo el perfil de usuario y el acceso a modelos 
    
    Siempre debe retornar algo
    """

    # nombre de la funcion
    code = models.CharField(blank=False, null=False, max_length=200 , unique=True)

    # este modelo se importa y se ofrece a la funcion
    modelName = models.CharField(blank=False, null=False, max_length=200)

    # lista separada por comas de los nombres de los argumentos
    arguments = models.CharField(blank=False, null=False, max_length=400)

    functionBody = models.TextField(blank=True, null=True)

    tag = models.CharField(blank=False, null=False, max_length=200)
    description = models.TextField(verbose_name=u'Descriptions', blank=True, null=True)


    def __str__(self):
        return self.code + '.' + self.tag




class Logger(models.Model):


    LOG_TYPE = (
        ('INF', 'INFO'),
        ('WAR', 'WARNING'),
        ('ERR', 'ERROR'),
    
        ('INS', 'INSERT'),
        ('UPD', 'UPDATE'),
        ('DEL', 'DELETE'),
    )
    
    smCreatedBy = models.ForeignKey(User, null=True, blank=True, related_name='+', editable=False)
    smCreatedOn = models.DateTimeField(auto_now=True , null=True, blank=True, editable=False)
    smOwningTeam = models.ForeignKey(TeamHierarchy, null=True, blank=True, related_name='+', editable=False)

    logType = models.CharField(max_length=10, default= 'INF')
    logObject = models.CharField(max_length=250, null=True, blank=True )
    logNotes = models.CharField(max_length=250, null=True, blank=True )

    logInfo = models.TextField(blank=True, null=True)

    """Long proccess runing"""
    logKey = models.CharField(max_length=5, choices= LOG_TYPE, default= '')

    def __str__(self):
        return self.logType + '.' +  self.logObject 

    protoExt = {
        "actions": [
            { "name": "doClearLog",
              "selectionMode" : "none",
              "refreshOnComplete" : True, 
            },
        ]
    }


def logEvent( logObject, logInfo, logUser, logTeam, logNotes = '', logType = 'INF', logKey = ''):


    dLog = Logger()

    setattr(dLog, 'smCreatedBy', logUser )
    setattr(dLog, 'smOwningTeam', logTeam )
    setattr(dLog, 'smCreatedOn', datetime.now())

    setattr(dLog, 'logInfo', logInfo  )

    if logType: 
        setattr(dLog, 'logType', logType )

    if logObject:
        setattr(dLog, 'logObject', logObject )

    if logNotes: 
        setattr(dLog, 'logNotes', logNotes )

    if logKey: 
        setattr(dLog, 'logKey', logKey )

    try: 
        dLog.save()
    except: 
        pass  
