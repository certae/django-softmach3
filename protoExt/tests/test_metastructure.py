# -*- coding: utf-8 -*-

from django.test import TestCase

from protoLib.tests.dataSetup import createAuthExt
from protoExt.meta import verifyMeta


class TestMetaStructure(TestCase):

    def setUp(self):
        createAuthExt()


    def tearDown(self):
        pass

    
    def test_vereifyMeta_createpci(self):

        ptType = 'pcl'

        oMeta =  verifyMeta( {}, ptType )[0]
        
        for x in ["gridConfig", "gridSets", "formConfig", "custom", "businessRules"]: 
            if type ( oMeta.get( x )) != type( {} ):
                self.assertTrue( False, '%s not in meta' % ( x, ) )
            
        for x in ["fields", "fieldsBase", "fieldsAdm", "actions", "detailsConfig", "sheetConfig", "defaultTo"]: 
            if type ( oMeta.get( x )) != type( [] ):
                self.assertTrue( False, '%s not in meta' % ( x, ) )

        
    def test_vereifyMeta_create_tnode(self):

        ptType = 'actionDef'
        tNode = {
            '__ptConfig': {
                '__ptType': 'actionDef',
                'name': 'action01'
            },
            'text': 'action01',
            'children': [],
            '__ptType': 'actionDef',
            'id': 'ext-gen1673'
        }
        
        tNode =  verifyMeta( {}, ptType, tNode )[1]
        tNode1 = tNode.get('children')[0] 

        # 'children': [{'text': 'actionParams', 'children': [], }],
        self.assertEqual(tNode1.get('text'), 'actionParams')
            
