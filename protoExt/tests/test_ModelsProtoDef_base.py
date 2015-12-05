# -*- coding: utf-8 -*-

"""
Test protoExt definition in models 
"""
import re

from django.test import TestCase

from protoExt.meta import META_OBJECTS, META_PROPERTIES

from protoExt.models import CustomDefinition, ViewDefinition
from protoLib.models.smbase import TeamHierarchy


PossibleTypes = ['list', 'string']
DataTypes = dict()

# {'required': 'boolean', 'sortable': 'boolean', 'hideRowNumbers': 'boolean', 'exportCsv': 'boolean', 'pageSize': 'number', 'primary': 'boolean', 'collapsed': 'boolean', 'height': 'number', 'collapsible': 'boolean', 'maxWidth': 'number', 'readOnly': 'boolean', 'minHeight': 'number', 'cellLink': 'boolean', 'cellToolTip': 'boolean', 'wordWrap': 'boolean', 'maxHeight': 'number', 'denyAutoPrint': 'boolean', 'refreshOnComplete': 'boolean', 'minWidth': 'number', 'flex': 'number', 'width': 'number', 'hideCheckSelect': 'boolean', 'qbeHelp': 'boolean', 'hidden': 'boolean'}
for fields in META_PROPERTIES:
    if '.type' in fields:
        outcomeType = META_PROPERTIES[fields]
        field = re.sub(r'\.type$', '', fields)
        DataTypes[field] = outcomeType


def getFields(modelclass):
    fields = []
    for value in modelclass.protoExt:
        fields.append(value)
        
    return fields


def getObjectType(field, value):
    outcomeType = None
    if 'lists' in META_OBJECTS[field] and value in META_OBJECTS[field]['lists']:
        outcomeType = 'list'
    elif 'properties' in META_OBJECTS[field] and value in META_OBJECTS[field]['properties']:
        outcomeType = DataTypes[value]

    return outcomeType


def getFieldType(field, value, modelclass):
    outcomeType = None
    if field in META_OBJECTS['pcl']['lists']:
        outcomeType = 'list'
    elif field in META_OBJECTS['pcl']['properties']:
        outcomeType = DataTypes[value]
    elif field in META_OBJECTS['pcl']['objects']:
        outcomeType = getObjectType(field, value)

    if outcomeType is None:
        outcomeType = 'string'
    return outcomeType




class TeamHierarchyPropertiesTest(TestCase):
    def test_structure(self):
        fields = getFields(TeamHierarchy)
        for field in fields:
            for value in TeamHierarchy.protoExt[field]:
                fieldtype = getFieldType(field, value, TeamHierarchy)
                self.assertIn(fieldtype, PossibleTypes)


class ViewDefinitionPropertiesTest(TestCase):
    def test_structure(self):
        fields = getFields(ViewDefinition)
        for field in fields:
            for value in ViewDefinition.protoExt[field]:
                fieldtype = getFieldType(field, value, ViewDefinition)
                self.assertIn(fieldtype, PossibleTypes)


class CustomDefinitionPropertiesTest(TestCase):
    def test_structure(self):
        fields = getFields(CustomDefinition)
        for field in fields:
            for value in CustomDefinition.protoExt[field]:
                fieldtype = getFieldType(field, value, CustomDefinition)
                self.assertIn(fieldtype, PossibleTypes)


# class DiscreteValuePropertiesTest(TestCase):
#     def test_structure(self):
#         fields = getFields(DiscreteValue)
#         for field in fields:
#             for value in DiscreteValue.protoExt[field]:
#                 fieldtype = getFieldType(field, value, DiscreteValue)
#                 self.assertIn(fieldtype, PossibleTypes)