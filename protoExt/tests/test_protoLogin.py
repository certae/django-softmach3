# -*- encoding: UTF-8 -*-

import json
from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory
from protoLib.tests.dataSetup import createAuthBase

from django.http import HttpRequest
from django.contrib.auth import authenticate, login
from django.contrib.sessions.backends.base import SessionBase

from protoExt.views.protoLogin import protoGetUserRights, protoGetPasswordRecovery

class MySession(SessionBase):
    def cycle_key(self):
        pass


class protoGetUserRights_Test(TestCase):

    def setUp(self):
        createAuthBase()

        userdata = {'login': 'A', 'email': 'sm-certae@gmail.com', 'password': '1' }
        self.user = authenticate(username=userdata['login'], password=userdata['password'])

        self.request = HttpRequest()
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

    def test_returns_error_when_user_is_invalid(self):
        userdata = {'login': 'A', 'password': 'x'}
        self.request.POST = userdata
        
        reponse = protoGetUserRights( self.request )
        returnMessage = json.loads( reponse.content.decode('utf-8'))
        self.assertFalse(returnMessage['success'])


    def test_returns_error_when_user_is_inactive(self):
        self.user.is_active = False 
        self.user.save()
        
        reponse = protoGetUserRights( self.request )
        returnMessage = json.loads( reponse.content.decode('utf-8'))
        self.assertFalse(returnMessage['success'])


    def test_can_retrieve_user_rights(self):
        reponse = protoGetUserRights( self.request )        
        returnMessage = json.loads( reponse.content.decode('utf-8'))
        self.assertTrue(returnMessage['success'])


#   ===== protoGetPasswordRecovery_Test
    def test_protoGetPasswordRecovery_returns_error_when_method_is_not_post(self):
        self.request.method = 'GET'

        reponse = protoGetPasswordRecovery( self.request )
        returnMessage = json.loads( reponse.content.decode('utf-8'))
        self.assertFalse(returnMessage['success'])

    def test_protoGetPasswordRecovery_returns_error_when_user_is_invalid(self):
        userdata = {'login': 'A', 'email': 'x'}
        self.request.POST = userdata
        
        reponse = protoGetPasswordRecovery( self.request )
        returnMessage = json.loads( reponse.content.decode('utf-8'))
        self.assertFalse(returnMessage['success'])

    def test_protoGetPasswordRecovery_returns_error_when_user_is_inactive(self):
        self.user.is_active = False 
        self.user.save()
        
        reponse = protoGetPasswordRecovery( self.request )
        returnMessage = json.loads( reponse.content.decode('utf-8'))
        self.assertFalse(returnMessage['success'])


    def test_can_get_protoGetPasswordRecovery(self):
        reponse = protoGetPasswordRecovery( self.request )        
        self.assertEqual(reponse.url, '/')


#   ====  resetpassword 
    def test_resetpassword_returns_error_when_method_is_not_get(self):
        self.request.method = 'POST'

        reponse = resetpassword( self.request )
        returnMessage = json.loads( reponse.content.decode('utf-8'))
        self.assertFalse(returnMessage['success'])

    # def test_returns_error_when_user_is_invalid(self):
    #     userdata = {'login': 'A', 'email': 'x'}
    #     self.request.POST = userdata
        
    #     reponse = protoGetPasswordRecovery( self.request )
    #     returnMessage = json.loads( reponse.content.decode('utf-8'))
    #     self.assertFalse(returnMessage['success'])

    # def test_returns_error_when_user_is_inactive(self):
    #     self.user.is_active = False 
    #     self.user.save()
        
    #     reponse = protoGetPasswordRecovery( self.request )
    #     returnMessage = json.loads( reponse.content.decode('utf-8'))
    #     self.assertFalse(returnMessage['success'])

    # def test_can_get_pwd_recovery(self):
    #     reponse = protoGetPasswordRecovery( self.request )        
    #     self.assertEqual(reponse.url, '/')

