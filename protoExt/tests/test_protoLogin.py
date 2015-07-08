# -*- encoding: UTF-8 -*-

import json
from django.test import TestCase

from django.http import HttpRequest
from django.contrib.auth import authenticate

from protoExt.views.protoLogin import protoGetUserRights, protoGetPasswordRecovery
from protoExt.views.protoLogin import resetpassword, changepassword, protoLogout 

from protoLib.tests.dataSetup import createAuthBase, MySession

class protoLogin_Test(TestCase):

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

    def test_protoGetUserRights_returns_error_when_method_is_not_post(self):
        self.request.method = 'GET'

        reponse = protoGetUserRights( self.request )
        returnMessage = json.loads( reponse.content.decode('utf-8'))
        self.assertFalse(returnMessage['success'])

    def test_protoGetUserRights_returns_error_when_user_is_invalid(self):
        userdata = {'login': 'A', 'password': 'x'}
        self.request.POST = userdata
        
        reponse = protoGetUserRights( self.request )
        returnMessage = json.loads( reponse.content.decode('utf-8'))
        self.assertFalse(returnMessage['success'])


    def test_protoGetUserRights_returns_error_when_user_is_inactive(self):
        self.user.is_active = False 
        self.user.save()
        
        reponse = protoGetUserRights( self.request )
        returnMessage = json.loads( reponse.content.decode('utf-8'))
        self.assertFalse(returnMessage['success'])


    def test_protoGetUserRights_ok(self):
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


    def test_protoGetPasswordRecovery_ok(self):
        reponse = protoGetPasswordRecovery( self.request )        
        self.assertEqual(reponse.url, '/')


#   ====  resetpassword 
    def test_resetpassword_returns_error_when_method_is_not_get(self):
        reponse = resetpassword( self.request )
        returnMessage = json.loads( reponse.content.decode('utf-8'))
        self.assertFalse(returnMessage['success'])

    def test_resetpassword_notoken(self):
        userdata = {'a': '1', 't': 'x'}
        self.request.GET = userdata
        self.request.method = 'GET'

        reponse = resetpassword( self.request )
        returnMessage = json.loads( reponse.content.decode('utf-8'))
        self.assertFalse(returnMessage['success'])


    def test_resetpassword_token(self):
        link = '/protoExtReset'
        userdata = {'a': '1', 't': 'f5074df647fd3e7698d99004b4c18dcf'}
        self.request.GET = userdata
        self.request.method = 'GET'

        reponse = resetpassword( self.request )
        self.assertEqual(reponse.url, link)

    def test_resetpassword_direct(self):
        link = '/protoExtReset'
        userdata = {}
        self.request.GET = userdata
        self.request.method = 'GET'

        reponse = resetpassword( self.request )
        self.assertEqual(reponse.url, link)

#   ====  changepassword
    def test_changepassword_returns_error_when_method_is_not_post(self):
        self.request.method = 'GET'
        reponse = changepassword( self.request )
        returnMessage = json.loads( reponse.content.decode('utf-8'))
        self.assertFalse(returnMessage['success'])

    def test_changepassword_nocurrent(self):
        userdata = {'login': 'A', 'current': 'x', 'newPassword1': 'a', 'newPassword2': 'x'}
        self.request.GET = userdata
        self.request.method = 'GET'

        reponse = changepassword( self.request )
        returnMessage = json.loads( reponse.content.decode('utf-8'))
        self.assertFalse(returnMessage['success'])


    def test_changepassword_nomatch(self):
        userdata = {'login': 'A', 'current': '1', 'newPassword1': 'a', 'newPassword2': 'x'}
        self.request.GET = userdata
        self.request.method = 'GET'

        reponse = changepassword( self.request )
        returnMessage = json.loads( reponse.content.decode('utf-8'))
        self.assertFalse(returnMessage['success'])


    def test_changepassword_ok(self):
        userdata = {'login': 'A', 'current': '1', 'newPassword1': '1', 'newPassword2': '1'}
        self.request.POST = userdata

        reponse = changepassword( self.request )
        returnMessage = json.loads( reponse.content.decode('utf-8'))
        self.assertTrue(returnMessage['success'])

#   ====  logout 
    def test_protoLogout_ok(self):
        self.request.user = self.user 
        reponse = protoLogout( self.request )
        returnMessage = json.loads( reponse.content.decode('utf-8'))
        self.assertTrue(returnMessage['success'])

