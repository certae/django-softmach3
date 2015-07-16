# -*- coding: utf-8 -*-

from django.test import TestCase
from django.contrib.auth import authenticate, login

import json
 

class ProtoSaveProtoObjTest(TestCase):

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

        self.userdata = { 'viewCode' : 'protoLib.UserProfile' }
        self.request.POST = self.userdata

    def tearDown(self):
        pass


    def test_protosaveprotoobj_custom_menu(self):

        self.request.POST['viewCode'] = '__menu'# custom = True
        self.request.POST['protoMeta'] = json.dumps()

    def test_protosaveprotoobj_with_method_not_post(self):
        self.request.method = 'GET'
        response = json.loads(protoSaveProtoObj(self.request).content)
        self.assertFalse(response['success'])

    def test_protosaveprotoobj_custom_viewcode(self):
        response = json.loads(protoSaveProtoObj(self.request).content)
        self.assertTrue(response['success'])

    def test_protosaveprotoobj_prototype_viewcode(self):
        self.request.POST['viewCode'] = 'prototype.ProtoTable.t-model-t-other-entity'  # prototype = True
        response = json.loads(protoSaveProtoObj(self.request).content)
        self.assertFalse(response['success'])

