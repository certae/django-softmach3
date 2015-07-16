# -*- coding: utf-8 -*-

import json

from django.test import TestCase

from protoExt.tests.data_protolib_teamhierarchy_detailtree import DATA_protoLib_TeamHierarchy_DetailTree
from protoExt.utils.utilsBase import compare_lists
from protoExt.views.protoGetPciDetailsTree import protoGetDetailsTree
from protoLib.tests.dataSetup import createAuthExt, createPostRequest


class ProtoGetDetailsTreeTest(TestCase):

    def setUp(self):
        
        createAuthExt()
        createPostRequest( self )

        self.userdata = { 'viewCode' : 'protoLib.TeamHierarchy' }
        self.request.POST = self.userdata


    def tearDown(self):
        pass

    def test_protogetdetailstree(self):

        reponse = protoGetDetailsTree( self.request )        
        returnMessage = json.loads( reponse.content.decode('utf-8'))

        cmpResult = compare_lists( returnMessage, DATA_protoLib_TeamHierarchy_DetailTree  )
        self.assertTrue( cmpResult, 'return list is not conform' )
