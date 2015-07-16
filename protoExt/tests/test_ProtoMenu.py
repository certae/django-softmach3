# -*- coding: utf-8 -*-

import json

from django.test import TestCase

from protoExt.views.protoMenu import protoGetMenuData
from protoLib.tests.dataSetup import createAuthExt, createPostRequest
from protoExt.utils.utilsBase import compare_lists


class ProtoMenuTest(TestCase):
    """
    Verifica el autoMenu 
    """

    def setUp(self):
        createAuthExt()
        createPostRequest( self )


    def tearDown(self):
        pass

    def test_protogetmenudata(self):


        reponse = protoGetMenuData( self.request )        
        returnMessage = json.loads( reponse.content.decode('utf-8'))

        automenu = 0 
        for menu in returnMessage: 
            if menu['text'] == 'AutoMenu':
                automenu = 1
                break  
        
        if automenu: 
            if len( menu['children'] ) > 0:
                automenu = 2 
        
        self.assertEqual(automenu, 2, 'AutoMenu not found')
