# -*- coding: utf-8 -*-

from protoLib.models.smbase import logEvent

class protoLog():

    def __init__(self, logUser, logTeam, logKey ):
        self.logUser = logUser
        self.logTeam = logTeam
        self.logKey  = logKey 


    def info( self,  logNotes = '', logObject = '', logInfo = '' ):
        self.logType = 'INF'
        logEvent( logObject, logInfo, self.logUser, self.logTeam, logNotes, self.logType, self.logKey)


    def error( self, logNotes = '', logObject = '', logInfo = '' ):
        self.logType = 'ERR'
        logEvent( logObject, logInfo, self.logUser, self.logTeam, logNotes, self.logType, self.logKey)



def activityLog(action, user, option, info):
    # TODO:
    # info es un json con el detalle de la opcion { rows, meta, etc .... }
    # Verificar en profile si tiene o no tiene log
    # verificar la definicion de la pcl si hace o no log
    # verificar el tipo de accion ( ej: logear solo los borrados .... )

    userProfile = getUserProfile( user )
    dLog = protoLog( user, userProfile.userTeam , option )
    dLog.info( info ) 


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



