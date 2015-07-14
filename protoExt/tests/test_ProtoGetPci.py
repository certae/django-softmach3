# -*- coding: utf-8 -*-

from django.test import TestCase
from django.contrib.auth import authenticate, login
import json

from protoExt.views.protoGetPci import protoGetPCI
from protoLib.tests.dataSetup import createAuthExt , MySession
from django.test.client import RequestFactory
from django.contrib.auth.models import AnonymousUser
from protoExt.views import validateRequest 
from protoExt.models import ViewDefinition


class ProtoGetPciTest(TestCase):

    def setUp(self):
        
        createAuthExt()

        userdata = {'login': 'A', 'password': '1' }
        self.user = authenticate(username=userdata['login'], password=userdata['password'])

        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.request = self.factory.post('/protoGetPCI')
        self.request.session = MySession()
        self.request.user = self.user
        self.request.method = 'POST'

        userdata = { 'viewCode' : 'protoLib.UserProfile' }
        self.request.POST = userdata


    def tearDown(self):
        pass

#   ===== validateRequest_Test
    def test_validateRequest_returns_error_when_method_is_not_post(self):
        self.request.method = 'GET'

        reponse = validateRequest( self.request )[1]
        returnMessage = json.loads( reponse.content.decode('utf-8'))
        self.assertFalse(returnMessage['success'])

    def test_validateRequest_returns_error_when_user_is_invalid(self):
        self.request.user = AnonymousUser()
        
        reponse = validateRequest( self.request )[1]
        returnMessage = json.loads( reponse.content.decode('utf-8'))
        self.assertFalse(returnMessage['success'])


    def test_validateRequest_returns_error_when_user_is_none(self):
        self.request.user = None
        
        reponse = validateRequest( self.request )[1]
        returnMessage = json.loads( reponse.content.decode('utf-8'))
        self.assertFalse(returnMessage['success'])


    def test_validateRequest_returns_error_when_user_is_inactive(self):
        self.user.is_active = False 
        self.user.save()
        
        reponse = validateRequest( self.request )[1]
        returnMessage = json.loads( reponse.content.decode('utf-8'))
        self.assertFalse(returnMessage['success'])


    def test_validateRequest_returns_no_error(self):

        reponse = validateRequest( self.request )[1]
        result = reponse is None
        self.assertTrue( result )

    def test_validateRequest_returns_cBase_wellformed(self):
        localViewCode = 'protoLib.UserProfile'

        userdata = { 'viewCode' : localViewCode }
        self.request.POST = userdata

        cBase = validateRequest( self.request )[0]
        self.assertEqual( cBase.viewCode, localViewCode  )

    def test_validateRequest_returns_cBase_malformed(self):
        localViewCode = ' protoLib.UserProfile. '
        wellViewCode = 'protoLib.UserProfile'

        userdata = { 'viewCode' : localViewCode }
        self.request.POST = userdata

        cBase = validateRequest( self.request )[0]
        self.assertEqual( cBase.viewCode, wellViewCode  )


    def test_validateRequest_returns_cBase_viewname(self):
        localViewCode = 'protoLib.UserProfile.admin'
        localViewEntity = 'protoLib.UserProfile'

        userdata = { 'viewCode' : localViewCode }
        self.request.POST = userdata

        cBase = validateRequest( self.request )[0]
        self.assertEqual( cBase.viewEntity, localViewEntity  )


    def test_validateRequest_returns_cBase_userprofile(self):

        cBase = validateRequest( self.request )[0]
        self.assertEqual( cBase.userProfile.userTeam_id, 1  )

    def test_validateRequest_returns_cBase_teamhierarcy_none(self):

        cBase = validateRequest( self.request )[0]
        self.assertTrue( cBase.userProfile.userTree is None ) 


    def test_validateRequest_returns_cBase_userTree(self):

        # Login Build userTree   ( login_teamtree_update )        
        login( self.request, self.request.user )  

        cBase = validateRequest( self.request )[0]
        self.assertEqual( len( cBase.userProfile.userTree.split(',') ), 2 )


#   ===== protoGetPCI_Test  ( standart validateRequest )
    def test_protoGetPCI_returns_error_when_method_is_not_post(self):
        self.request.method = 'GET'

        reponse = protoGetPCI( self.request )
        returnMessage = json.loads( reponse.content.decode('utf-8'))
        self.assertFalse(returnMessage['success'])

    def test_protoGetPCI_returns_error_when_user_is_invalid(self):
        self.request.user = AnonymousUser()
        
        reponse = protoGetPCI( self.request )
        returnMessage = json.loads( reponse.content.decode('utf-8'))
        self.assertFalse(returnMessage['success'])


    def test_protoGetPCI_returns_error_when_user_is_none(self):
        self.request.user = None
        
        reponse = protoGetPCI( self.request )
        returnMessage = json.loads( reponse.content.decode('utf-8'))
        self.assertFalse(returnMessage['success'])


    def test_protoGetPCI_returns_error_when_user_is_inactive(self):
        self.user.is_active = False 
        self.user.save()
        
        reponse = protoGetPCI( self.request )
        returnMessage = json.loads( reponse.content.decode('utf-8'))
        self.assertFalse(returnMessage['success'])


#   ===== protoGetPCI_Test 
    def test_protoGetPCI_invalidmodel(self):
        localViewCode = 'protoLib.xxx'
        userdata = { 'viewCode' : localViewCode }
        self.request.POST = userdata

        reponse = protoGetPCI( self.request )        
        returnMessage = json.loads( reponse.content.decode('utf-8'))
        self.assertFalse(returnMessage['success'])


    def test_protoGetPCI_model_noApp(self):
        localViewCode = 'UserProfile'
        userdata = { 'viewCode' : localViewCode }
        self.request.POST = userdata

        reponse = protoGetPCI( self.request )        
        returnMessage = json.loads( reponse.content.decode('utf-8'))
        self.assertTrue(returnMessage['success'])


    def test_protoGetPCI_newpci(self):

        # se asegura de q no exista          
        ViewDefinition.objects.all().delete()

        reponse = protoGetPCI( self.request )        
        self.assertEqual(reponse.url, '/')
  
#  
#     def test_protogetpci_success(self):
#  
#         self.request.POST['viewCode'] = 'prototype.Project'
#         self.returnMessage = json.loads(protoGetPCI(self.request).content)
#  
#         self.assertTrue(self.returnMessage['success'])
#  
#     def test_protogetpci_viewcode(self):
#         self.assertEqual(self.request.POST['viewCode'], self.returnMessage['protoMeta']['viewCode'])
#  
#     def test_protogetpci_viewentity(self):
#         self.assertEqual(self.request.POST['viewCode'], self.returnMessage['protoMeta']['viewEntity'])
 
# 
# class ProtoSaveProtoObjTest(TestCase):
#     fixtures = ['auth.json']
# 
#     def setUp(self):
#         self.request = HttpRequest()
#         self.request.method = 'POST'
#         self.request.POST['login'] = 'adube'
#         self.request.POST['password'] = '123'
#         self.request.user = authenticate(username=self.request.POST['login'], password=self.request.POST['password'])
# 
#         self.request.POST['viewCode'] = '__menu'# custom = True
#         self.request.POST['protoMeta'] = json.dumps({
#             "text": "prototype",
#             "qtip": "",
#             "qtitle": "",
#             "iconCls": "",
#             "id": "protoMenu-ext-gen1448",
#             "index": 0,
#             "expanded": True,
#             "children": [{
#                 "text": "Relationship",
#                 "qtip": "",
#                 "qtitle": "",
#                 "iconCls": "icon-1",
#                 "id": "protoMenu-ext-gen1449",
#                 "index": 0,
#                 "expanded": False,
#                 "children": [],
#                 "leaf": True,
#                 "viewCode": "prototype.Relationship"
#             }, {
#                 "text": "Entity",
#                 "qtip": "",
#                 "qtitle": "",
#                 "iconCls": "icon-1",
#                 "id": "protoMenu-ext-gen1450",
#                 "index": 1,
#                 "expanded": False,
#                 "children": [],
#                 "leaf": True,
#                 "viewCode": "prototype.Entity"
#             }, {
#                 "text": "Property",
#                 "qtip": "",
#                 "qtitle": "",
#                 "iconCls": "icon-1",
#                 "id": "protoMenu-ext-gen1451",
#                 "index": 2,
#                 "expanded": False,
#                 "children": [],
#                 "leaf": True,
#                 "viewCode": "prototype.Property"
#             }, {
#                 "text": "Project",
#                 "qtip": "",
#                 "qtitle": "",
#                 "iconCls": "icon-1",
#                 "id": "protoMenu-ext-gen1452",
#                 "index": 3,
#                 "expanded": False,
#                 "children": [],
#                 "leaf": True,
#                 "viewCode": "prototype.Project"
#             }, {
#                 "text": "Model",
#                 "qtip": "",
#                 "qtitle": "",
#                 "iconCls": "icon-1",
#                 "id": "protoMenu-ext-gen1453",
#                 "index": 4,
#                 "expanded": False,
#                 "children": [],
#                 "leaf": True,
#                 "viewCode": "prototype.Model"
#             }],
#             "leaf": False,
#             "viewCode": "protoMenu-ext-gen4397"
#         })
# 
#     def tearDown(self):
#         pass
# 
#     def test_protosaveprotoobj_with_method_not_post(self):
#         self.request.method = 'GET'
#         response = json.loads(protoSaveProtoObj(self.request).content)
#         self.assertFalse(response['success'])
# 
#     def test_protosaveprotoobj_custom_viewcode(self):
#         response = json.loads(protoSaveProtoObj(self.request).content)
#         self.assertTrue(response['success'])
# 
#     def test_protosaveprotoobj_prototype_viewcode(self):
#         self.request.POST['viewCode'] = 'prototype.ProtoTable.t-model-t-other-entity'  # prototype = True
#         response = json.loads(protoSaveProtoObj(self.request).content)
#         self.assertFalse(response['success'])
# 
# 
# class ProtoGetFieldTreeTest(TestCase):
#     fixtures = ['auth.json']
# 
#     def setUp(self):
#         self.request = HttpRequest()
#         self.request.method = 'POST'
#         self.request.POST['login'] = 'adube'
#         self.request.POST['password'] = '123'
#         self.request.user = authenticate(username=self.request.POST['login'], password=self.request.POST['password'])
#         self.request.POST['id'] = 'root'
#         self.request.POST['node'] = 'root'
#         self.request.POST['sort'] = json.dumps({"property": "text", "direction": "ASC"})
#         self.request.POST['viewCode'] = 'prototype.Project'
# 
#     def tearDown(self):
#         pass
# 
#     def test_protogetfieldtree(self):
#         response = json.loads(protoGetFieldTree(self.request).content)
#         # pprint(response)
#         for element in response:
#             self.assertFalse(element['checked'])
