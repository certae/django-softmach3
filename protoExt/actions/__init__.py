# -*- coding: utf-8 -*-


def doAddUser(modeladmin, request, queryset, parameters):
    """ 
    Add user  
    parameters : sUser,sPwd,sMail,sTeam,[sGroups]
    """

#   El QSet viene con la lista de Ids  
    from protoExt.actions.addUser import actionAddUser   
    return actionAddUser(request, queryset, parameters)


def doFindReplace(modeladmin, request, queryset, parameters):
    """ 
    find and replace sobre la tabla actual 
    parameters   campo,  findText, replaceText 
    """

#   El QSet viene con la lista de Ids  
    if queryset.count() < 1:
        return  {'success':False, 'message' : 'Multiple selection required'}

    if len(parameters) != 3: 
        return  {'success':False, 'message' : 'required: fieldName, findText, replaceText' }

    from protoLib.actions.findReplace import actionFindReplace  
    return actionFindReplace(request, queryset, parameters)

