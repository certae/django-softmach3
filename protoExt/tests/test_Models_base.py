# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.test import TestCase

from protoExt.models import CustomDefinition, ViewDefinition
from protoLib.getStuff import getDjangoModel, getUserProfile
from protoLib.models.smbase import TeamHierarchy, UserProfile


class GetDjangoModelTest(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_method_with_no_dot_in_name(self):
        returnMessage = getDjangoModel('UserProfile')
        self.assertTrue(returnMessage is not None)

    def test_method_with_single_dot_in_name(self):
        returnMessage = getDjangoModel('protoLib.UserProfile')
        self.assertTrue(returnMessage is not None)

    def test_method_with_two_dots_in_name(self):
        returnMessage = getDjangoModel('protoLib.UserProfile.ExtraStuffInName')
        self.assertTrue(returnMessage is not None)

    def test_method_with_user_none(self):
        self.assertRaises(Exception, getDjangoModel, 'SomeInvalidName')


class TeamHierarchyTest(TestCase):

    def setUp(self):
        teamhierarchydata = {
            'code': 'SomeValue',
            'description': 'Description of TeamHierarchy',
        }

        self.teamHierarchy = TeamHierarchy(**teamhierarchydata)
        self.teamHierarchy.save()

    def tearDown(self):
        self.teamHierarchy.delete()

    def test_verifying_string_representation(self):
        self.assertEqual(self.teamHierarchy.code, str(self.teamHierarchy))



class UserProfileTest(TestCase):
    def setUp(self):
        userdata = {
            'username': 'testuser',
            'first_name': 'Bob',
            'last_name': 'Tremblay',
            'email': 'bob.tremblay@courriel.ca',
        }


        self.user_test = User(**userdata)
        self.user_test.save()

#       Crea el profile manualmente 
        self.userProfile = getUserProfile( self.user_test )

        entry = User.objects.get(id = self.user_test.id)
        self.userProfile = UserProfile.objects.get(id = entry.id)


    def tearDown(self):
        self.user_test.delete()
        self.userProfile.delete()

    def test_user_post_save(self):
        self.assertIsNotNone(self.userProfile)

    def test_verifying_string_representation(self):
        self.assertEqual(self.userProfile.user.username, str(self.user_test))


# class UserShareTest(TestCase):
#     def setUp(self):
#         userdata = {
#             'username': 'test_user',
#             'first_name': 'Bob',
#             'last_name': 'Tremblay',
#             'email': 'bob.tremblay@courriel.ca'
#         }
# 
#         self.user_test = User(**userdata)
#         self.user_test.save()
# 
#         teamhierarchydata = {
#             'code': 'SomeValue',
#             'description': 'Description of TeamHierarchy',
#             'parentNode': None,
#         }
# 
#         self.teamHierarchy = TeamHierarchy(**teamhierarchydata)
#         self.teamHierarchy.save()
# 
#         usersharedata = {
#             'user': self.user_test,
#             'userTeam': self.teamHierarchy
#         }
# 
#         self.userShare = UserShare(**usersharedata)
#         self.userShare.save()
# 
#     def tearDown(self):
#         self.userShare.delete()
#         self.teamHierarchy.delete()
#         self.user_test.delete()
# 
#     def test_verifying_string_representation(self):
#         self.assertEqual(self.userShare.user.username + '-' + self.userShare.userTeam.code, str(self.userShare))


class ViewDefinitionTest(TestCase):
    def setUp(self):
        ViewDefinitiondata = {
            'code': 'test_code',
            'description': 'description ViewDefinition',
            'metaDefinition': {}, 
            'active': True,
            'overWrite': True
        }
        self.ViewDefinition = ViewDefinition(**ViewDefinitiondata)
        self.ViewDefinition.save()

    def tearDown(self):
        self.ViewDefinition.delete()

    def test_verifying_string_representation(self):
        self.assertEqual('test_code', str(self.ViewDefinition))


class CustomDefinitionTest(TestCase):
    def setUp(self):
        customdefinitiondata = {
            'code': 'test_code',
            'description': 'description ViewDefinition',
            'metaDefinition': {},
            'active': True,
            'overWrite': True
        }
        self.customDefinition = CustomDefinition(**customdefinitiondata)
        self.customDefinition.save()

    def tearDown(self):
        self.customDefinition.delete()

    def test_verifying_string_representation(self):
        self.assertEqual('test_code', str(self.customDefinition))


# class DiscreteValueTest(TestCase):
#     def setUp(self):
#         pass
# 
#     def tearDown(self):
#         pass
# 
#     def test_verifying_string_representation_with_title_as_none(self):
#         discretevaluedata = {
#             'code': 'test_code',
#             'value': 'test_value',
#             'description': 'description of discrete value',
#             'title': None
#         }
#         self.discreteValue = DiscreteValue(**discretevaluedata)
#         self.discreteValue.save()
# 
#         self.assertEqual('test_code', str(self.discreteValue))
# 
#         self.discreteValue.delete()
# 
#     def test_verifying_string_representation_with_title_not_none(self):
#         discretevaluedata = {
#             'code': 'test_code',
#             'value': 'test_value',
#             'description': 'description of discrete value',
#             'title': DiscreteValue()
#         }
#         self.discreteValue = DiscreteValue(**discretevaluedata)
#         self.discreteValue.save()
# 
#         self.assertEqual('.test_code', str(self.discreteValue))
# 
#         self.discreteValue.delete()
# 
# 
# class PtFunctionTest(TestCase):
#     def setUp(self):
#         ptfunctiondata = {
#             'code': 'test_code',
#             'modelName': 'name of model',
#             'arguments': 'test arguments',
#             'functionBody': 'body of function',
#             'tag': 'test tag',
#             'description': 'description of function'
#         }
#         self.ptFunction = PtFunction(**ptfunctiondata)
#         self.ptFunction.save()
# 
#     def tearDown(self):
#         self.ptFunction.delete()
# 
#     def test_verifying_string_representation(self):
#         self.assertEqual(self.ptFunction.code + '.' + self.ptFunction.tag, str(self.ptFunction))


