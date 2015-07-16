# -*- coding: utf-8 -*-

"""
Test protoExt definition in models 
"""
import re

from django.test import TestCase

from protoExt.meta import META_OBJECTS, META_PROPERTIES

from protoExt.models import CustomDefinition, ViewDefinition
from protoLib.models.smbase import TeamHierarchy
from prototype.models import Project, Model, Entity, Property, Relationship, PropertyEquivalence, ProtoTable, Prototype


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



class ProjectPropertiesTest(TestCase):
    def test_structure(self):
        fields = getFields(Project)
        for field in fields:
            for value in Project.protoExt[field]:
                fieldtype = getFieldType(field, value, Project)
                self.assertIn(fieldtype, PossibleTypes)


class ModelPropertiesTest(TestCase):
    def test_structure(self):
        fields = getFields(Model)
        for field in fields:
            for value in Model.protoExt[field]:
                fieldtype = getFieldType(field, value, Model)
                self.assertIn(fieldtype, PossibleTypes)


class EntityPropertiesTest(TestCase):
    def test_structure(self):
        fields = getFields(Entity)
        for field in fields:
            for value in Entity.protoExt[field]:
                fieldtype = getFieldType(field, value, Entity)
                self.assertIn(fieldtype, PossibleTypes)


class PropertyPropertiesTest(TestCase):
    def test_structure(self):
        fields = getFields(Property)
        for field in fields:
            for value in Property.protoExt[field]:
                fieldtype = getFieldType(field, value, Property)
                self.assertIn(fieldtype, PossibleTypes)


class RelationshipPropertiesTest(TestCase):
    def test_structure(self):
        fields = getFields(Relationship)
        for field in fields:
            if field is 'exclude':
                continue
            for value in Relationship.protoExt[field]:
                fieldtype = getFieldType(field, value, Relationship)
                self.assertIn(fieldtype, PossibleTypes)



class PropertyEquivalencePropertiesTest(TestCase):
    def test_structure(self):
        fields = getFields(PropertyEquivalence)
        for field in fields:
            for value in PropertyEquivalence.protoExt[field]:
                fieldtype = getFieldType(field, value, PropertyEquivalence)
                self.assertIn(fieldtype, PossibleTypes)


class PrototypePropertiesTest(TestCase):
    def test_structure(self):
        fields = getFields(Prototype)
        for field in fields:
            for value in Prototype.protoExt[field]:
                fieldtype = getFieldType(field, value, Prototype)
                self.assertIn(fieldtype, PossibleTypes)


class ProtoTablePropertiesTest(TestCase):
    def test_structure(self):
        fields = getFields(ProtoTable)
        for field in fields:
            for value in ProtoTable.protoExt[field]:
                fieldtype = getFieldType(field, value, ProtoTable)
                self.assertIn(fieldtype, PossibleTypes)



