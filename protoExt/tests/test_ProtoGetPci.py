# -*- coding: utf-8 -*-

import json

from django.contrib.auth import  login
from django.contrib.auth.models import AnonymousUser
from django.test import TestCase

from protoExt.models import ViewDefinition
from protoExt.tests.data_protolib_userprofile_pci import DATA_PCI_protoLib_UserProfile
from protoExt.utils.utilsBase import compare_dictionaries
from protoExt.views import validateRequest
from protoExt.views.protoGetPci import protoGetPCI
from protoLib.tests.dataSetup import createAuthExt , createPostRequest


class ProtoGetPciTest(TestCase):

    def setUp(self):
        
        createAuthExt()
        createPostRequest( self )

        self.userdata = { 'viewCode' : 'protoLib.UserProfile' }
        self.request.POST = self.userdata


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

        viewCode = self.userdata['viewCode']
        ViewDefinition.objects.filter( code = viewCode ).delete()

        reponse = protoGetPCI( self.request )        
        returnMessage = json.loads( reponse.content.decode('utf-8'))

        self.assertTrue(returnMessage['success'])

        metaData = returnMessage['metaData']
        self.assertEqual( metaData['idProperty'], 'id' )

        protoMeta = returnMessage['protoMeta']
        self.assertEqual( protoMeta['viewCode'], viewCode )
        self.assertEqual( protoMeta['viewEntity'], viewCode )
        self.assertTrue( len( returnMessage['protoMeta']['fields'])  > 0 ) 

        permissions = returnMessage['permissions']
        self.assertTrue( permissions['list'] )

        cmpResult = compare_dictionaries( returnMessage, DATA_PCI_protoLib_UserProfile )
        self.assertTrue( cmpResult, 'return dict is not conform' )
  
