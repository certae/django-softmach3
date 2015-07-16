# -*- coding: utf-8 -*-

from django.test import TestCase
from protoLib.getStuff import getUserProfile



class GetUserProfileTest(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_method_with_user_none(self):
        self.assertIsNone(getUserProfile(None))


class ActivityLogTest(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_method_with_user_none(self):
        self.assertIsNone(activityLog('', '', '', ''))
