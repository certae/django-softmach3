# -*- encoding: UTF-8 -*-

import json
from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory
from protoLib.tests.dataSetup import createAuthBase

from django.http import HttpRequest
from django.contrib.auth import authenticate, login
from django.contrib.sessions.backends.base import SessionBase

from protoExt.views.protoLogin import protoGetUserRights

class MySession(SessionBase):
    def cycle_key(self):
        pass


class LoginTest(TestCase):
    fixtures = ['auth.json']

    def setUp(self):

        createAuthBase()

        userdata = {
            'login': 'A',
            'password': '1'
        }

        self.user = authenticate(username=userdata['login'], password=userdata['password'])
        self.request = HttpRequest()

        # self.factory = RequestFactory()
        # self.viewName = ''
        # request = self.factory.post( self.viewName, data )

        self.request.session = MySession()
        self.request.method = 'POST'
        self.request.POST = userdata

    def tearDown(self):
        pass

    def test_returns_error_when_method_is_not_post(self):
        self.request.method = 'GET'
        reponse = protoGetUserRights( self.request )
        returnMessage = json.loads( reponse.content.decode('utf-8'))
        self.assertFalse(returnMessage['success'])

    def test_can_retrieve_user_rights(self):
        
        reponse = protoGetUserRights( self.request )        
        returnMessage = json.loads( reponse.content.decode('utf-8'))
        self.assertTrue(returnMessage['success'])


#     def test_can_authenticate_valid_user(self):
#         self.assertTrue(self.user.is_active)
# 
#     def test_fails_to_authenticate_invalid_user(self):
#         user = authenticate(username='WrongUsername', password='InvalidPassword')
#         self.assertTrue(user is None)
# 
#     def test_can_login_user(self):
#         status = False
#         self.assertTrue(self.user.is_active)
#         self.assertTrue(self.user is not None)
#         try:
#             login(self.request, self.user)
#             status = True
#         except:
#             pass
#         self.assertTrue(status)


#     def test_returns_error_when_user_does_not_exist(self):
#         userdata = {
#             'login': 'Bob',
#             'password': 'BobPasswd'
#         }
# 
#         self.user = authenticate(username=userdata['login'], password=userdata['password'])
#         self.request.POST = userdata
#         returnMessage = json.loads(protoGetUserRights(self.request).content)
#         self.assertFalse(returnMessage['success'])



# class LoginProtoExt(TestCase):
# 
#     def setUp(self):
#         # Every test needs access to the request factory.
#         self.factory = RequestFactory()
#         self.viewName = ''
# 
#         createAuthBase()
# 
#     def test_login_A(self):
#         
#         data = { 'login' : 'A', 'password' : 1 }
#         request = self.factory.post( self.viewName, data )
#         request.user = AnonymousUser()
#         request.session = {}        
#         reponse = protoGetUserRights( request )        
# 
#         print( type( reponse ) ) 
#         print( reponse )
# 
# 
#     def test_login_B(self):
#         pass 
# 
#     def test_login_X(self):
#         pass 
#     
# 
# 
# class ValidaRequest(TestCase):
# 
#     # authenticate(username=userName, password=userPwd)
#     def setUp(self):
#         # Every test needs access to the request factory.
#         self.factory = RequestFactory()
#         self.viewName = ''
#         self.data = ''
# 
#         createAuthBase()
# 
#     def test_valida_A(self):
# 
#         user = autenticateUser( 'A', '1')
#         request = self.factory.post( self.viewName, self.data )
#         request.user = user
#     
#     def test_valida_Anonymous(self):
# 
#         request = self.factory.post( self.viewName, self.data )
#         request.user = AnonymousUser()

