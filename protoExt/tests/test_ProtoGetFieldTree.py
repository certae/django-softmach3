# -*- coding: utf-8 -*-

import json

from django.test import TestCase

from protoExt.views.protoGetPciFieldTree import protoGetFieldTree
from protoLib.tests.dataSetup import createAuthExt, createPostRequest
from protoExt.tests.data_protolib_userprofile_fieldtree import DATA_protoLib_UserProfile_FieldTree
from protoExt.utils.utilsBase import compare_lists


class ProtoGetFieldTreeTest(TestCase):

    def setUp(self):
        
        createAuthExt()
        createPostRequest( self )

        self.userdata = { 'viewCode' : 'protoLib.UserProfile' }
        self.request.POST = self.userdata

    def tearDown(self):
        pass

    def test_protogetfieldtree_pci(self):

        reponse = protoGetFieldTree( self.request )        
        returnMessage = json.loads( reponse.content.decode('utf-8'))

        cmpResult = compare_lists( returnMessage, DATA_protoLib_UserProfile_FieldTree  )
        self.assertTrue( cmpResult, 'return list is not conform' )
