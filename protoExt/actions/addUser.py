#  Dario GomezT 1303  Creacion automatica de usuarios, team, grupo 

# -*- coding: utf-8 -*-


from django.contrib.auth.models import User, Group
from protoLib.models import  TeamHierarchy, UserProfile


def actionAddUser( request,  queryset , parameters ):
    """
    Permite crear el usuario y asociarlo a un grupo y un team 
    """ 

    sUser   = parameters[0]['value'] 
    sPwd    = parameters[1]['value'] 
    sMail   = parameters[2]['value'] or ''
    sTeam   = parameters[3]['value'] or ''
    sGroups = parameters[4]['value'] or 'users'
    groups = [ gr.strip() for gr in sGroups.split(',') ]

    result, message = addProtoUser(sUser, sPwd, sMail, sTeam, groups )
            
    return  {'success': result  , 'message' :  message }



def actionAddUsers( request,  queryset , parameters ):
    """
    Permite crear el usuario y asociarlo a un grupo y un team 
    """ 

    sUsers  = parameters[0]['value'] 
    sResult = ''

    for sUserLine in sUsers.splitlines(): 

        aUsers = sUserLine.split(',')
        if len( aUsers ) < 5: 
            continue 

        sUser, sPwd, sMail, sTeam = aUsers[0:4]
        groups = aUsers[4:]

        result, message = addProtoUser(sUser, sPwd, sMail, sTeam, groups )

        if result : 
            sResult += sUser + ' Ok,'
        else:
            sResult += sUser + ' Failed,'
    
    return  {'success': True  , 'message' :  sResult }


def addProtoUser(sUser, sPwd, sMail, sTeam, groups ):

    sUser   =  sUser.strip()
    sPwd    =  sPwd.strip()
    sMail   =  sMail.strip()
    sTeam   =  sTeam.strip()

    if len( sUser ) == 0: 
        return True, 'Ok'  
            
#   User   ------------ 
    try:
        user = User.objects.get(username=sUser)
    except User.DoesNotExist:
        user = User(username= sUser)
        # User.objects.create_user( )

    try: 

        user.is_staff = True
        user.is_active = True

        if len( sMail ) > 0:  user.email = sMail 
        if len( sPwd ) > 0:  user.set_password( sPwd ) 
        user.save()


    #   User Profile   ------------
        if len( sTeam ) > 0: 
            uProfile = UserProfile.objects.get_or_create(user=user)[0]
            uProfile.userTeam = TeamHierarchy.objects.get_or_create(code= sTeam )[0]
            uProfile.save()


    #   Groups    ------------ 
        for gr in groups:
            gr = gr.strip() 
            group = Group.objects.get_or_create(name = gr )[0]
            user.groups.add( group )

        return  True ,  'Ok'
    except :
        return  False ,  'Failed'