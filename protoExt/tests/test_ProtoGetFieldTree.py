# -*- coding: utf-8 -*-

from django.test import TestCase
from django.contrib.auth import authenticate

import json
from protoExt.views.protoGetPciFieldTree import protoGetFieldTree
from django.http.request import HttpRequest

xx 

class ProtoGetFieldTreeTest(TestCase):
    fixtures = ['auth.json']

    def setUp(self):
        self.request = HttpRequest()
        self.request.method = 'POST'
        self.request.POST['login'] = 'adube'
        self.request.POST['password'] = '123'
        self.request.user = authenticate(username=self.request.POST['login'], password=self.request.POST['password'])
        self.request.POST['id'] = 'root'
        self.request.POST['node'] = 'root'
        self.request.POST['sort'] = json.dumps({"property": "text", "direction": "ASC"})
        self.request.POST['viewCode'] = 'prototype.Project'

    def tearDown(self):
        pass

    def test_protogetfieldtree(self):
        response = json.loads(protoGetFieldTree(self.request).content)
        # pprint(response)
        for element in response:
            self.assertFalse(element['checked'])
