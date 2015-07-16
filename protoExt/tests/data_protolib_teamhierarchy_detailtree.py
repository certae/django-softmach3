# -*- coding: utf-8 -*-

"""
Details autogenerada para la entidad protoLib.TeamHierarchy
"""

DATA_protoLib_TeamHierarchy_DetailTree =   [{
  'detailField': 'parentNode__pk',
  'id': 'Teamhierarchy.parentNode',
  'conceptDetail': 'protoLib.TeamHierarchy',
  'leaf': False,
  'masterField': 'pk',
  'children': [{
    'detailField': 'teamhierarchy.parentNode__parentNode__pk',
    'id': 'Teamhierarchy.parentNode/Teamhierarchy.parentNode',
    'conceptDetail': 'protoLib.TeamHierarchy',
    'leaf': False,
    'masterField': 'pk',
    'children': [{
      'id': 'Teamhierarchy.parentNode/Teamhierarchy.parentNode/Teamhierarchy.parentNode',
      'conceptDetail': 'protoLib.TeamHierarchy',
      'detailField': 'teamhierarchy.parentNode__teamhierarchy.parentNode__parentNode__pk',
      'masterField': 'pk',
      'leaf': True
    }, {
      'id': 'Teamhierarchy.parentNode/Teamhierarchy.parentNode/Userprofile.userTeam',
      'conceptDetail': 'protoLib.UserProfile',
      'detailField': 'userprofile.userTeam__teamhierarchy.parentNode__parentNode__pk',
      'masterField': 'pk',
      'leaf': True
    }]
  }, {
    'id': 'Teamhierarchy.parentNode/Userprofile.userTeam',
    'conceptDetail': 'protoLib.UserProfile',
    'detailField': 'userprofile.userTeam__parentNode__pk',
    'masterField': 'pk',
    'leaf': True
  }]
}, {
  'id': 'Userprofile.userTeam',
  'conceptDetail': 'protoLib.UserProfile',
  'detailField': 'userTeam__pk',
  'masterField': 'pk',
  'leaf': True
}]