# -*- coding: utf-8 -*-

"""
Quick test debuger  
"""

def protoQuickTest(request):
    pass 

#     from protoExt.tests.test_metastructure import TestMetaStructure
#     t1 = TestMetaStructure()
#     t1.test_vereifyMeta_createpci()
#     t1.test_vereifyMeta_create_tnode()

    from protoExt.tests.test_ProtoGetPci import ProtoGetPciTest
    t1 = ProtoGetPciTest()
    t1.request = request 
    t1.userdata = { 'viewCode' : 'protoLib.UserProfile' }
    t1.request.method = 'POST'
    t1.request.POST = t1.userdata
     
    t1.test_protoGetPCI_newpci()

