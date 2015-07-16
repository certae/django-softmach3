# -*- coding: utf-8 -*-

import json

from django.contrib.auth import authenticate
from django.test import TestCase
from django.test.client import RequestFactory

from protoExt.views.protoSaveProtoObj import protoSaveProtoObj
from protoLib.tests.dataSetup import createAuthExt, MySession
from protoExt.views.protoGetPci import protoGetPCI
from protoExt.models import CustomDefinition


class ProtoSaveProtoObjTest(TestCase):

    def setUp(self):

        createAuthExt()

        userdata = {'login': 'A', 'password': '1' }
        self.user = authenticate(username=userdata['login'], password=userdata['password'])

        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.request = self.factory.post('/protoSaveProtoObj')
        self.request.session = MySession()
        self.request.user = self.user
        self.request.method = 'POST'

        self.userdata = { 'viewCode' : 'protoLib.UserProfile' }
        self.request.POST = self.userdata

    def tearDown(self):
        pass


    def test_protosaveprotoobj_save_pci(self):
        """
        Agrega un campo a la definicion de la pcl,
        Guarda la definicion           
        Lee y verifica el campo 
        """
        from protoExt.tests.data_protolib_userprofile_pci import DATA_PCI_protoLib_UserProfile
        
        oMeta = DATA_PCI_protoLib_UserProfile['protoMeta']
        oMeta['gridConfig']['listDisplay'].append('userTeam') 
        
        sMeta = json.dumps( oMeta )
        self.userdata = { 
            'viewCode' : 'protoLib.UserProfile', 
            'protoMeta' : sMeta  
        }
        self.request.POST = self.userdata

        reponse = protoSaveProtoObj( self.request )
        returnMessage = json.loads( reponse.content.decode('utf-8'))
        self.assertTrue(returnMessage['success'])
        
        self.userdata = { 
            'viewCode' : 'protoLib.UserProfile', 
            'protoMeta' : sMeta  
        }
        self.request.POST = self.userdata

        reponse = protoGetPCI( self.request )
        returnMessage = json.loads( reponse.content.decode('utf-8'))
        self.assertTrue(returnMessage['success'])

        oMeta = returnMessage['protoMeta']
        self.assertEqual( len(oMeta['gridConfig']['listDisplay'] ), 2, 'listdisplau !=2')
        

    def test_protosaveprotoobj_custom_test(self):
        """
        Elimina datos de CustomDefinition 
        Guarda la definicion           
        Lee CustomDefinition y verifica el campo 
        """

        self.userdata = { 
            'viewCode' : '_custom_test', 
            'protoMeta' : '[0]'  
        }
        self.request.POST = self.userdata
        CustomDefinition.objects.filter(code = self.userdata['viewCode'] ).delete()

        reponse = protoSaveProtoObj( self.request )
        returnMessage = json.loads( reponse.content.decode('utf-8'))
        self.assertTrue(returnMessage['success'])
 
        cData = CustomDefinition.objects.get( 
             code = self.userdata['viewCode'], 
             smOwningUser = self.request.user 
        )
        self.assertEqual( cData.metaDefinition[0], 0)
 
