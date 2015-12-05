# -*- coding: utf-8 -*-

from django.test import TestCase

from protoExt.utils.logger import activityLog
from protoLib.models.smbase import getUserProfile
from protoLib.tests.dataSetup import createAuthExt, createPostRequest


class GetUserProfileTest(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_method_with_user_none(self):
        self.assertIsNone(getUserProfile(None))


class ActivityLogTest(TestCase):

    def setUp(self):
        createAuthExt()
        createPostRequest( self )

    def tearDown(self):
        pass

    def test_logger(self):
       
        activityLog( action = '', user = self.user, option = '', info = '')
