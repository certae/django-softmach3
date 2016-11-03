#!/usr/bin/env python
'''
Created on Nov 2, 2016

@author: dario
'''
from protoExt.utils.utilsBase import getClassName
from protoExt.utils.utilsConvert import slugify3


class TreeGraph():

    def __init__(self):

        self.tblStyle = False
        self.lnkStyle = '\n'

        self.dotSource = 'digraph bp {'
        self.dotSource += 'fontname="Helvetica";fontsize = 8;\n'
        self.dotSource += 'node [shape=box,style=rounded,width=0,height=0,concentrate=true];\n'

    def getDiagramDefinition(self, queryset):

        self.diagrams = []

        for pNode in queryset:

            gDiagram = {
                'code': getClassName(pNode.code),
                'label': pNode.code,
                'showBorder': getattr(pNode, 'showBorder', False),
                'arcs': [],
                'labels': set()
            }

            self.getDependency(pNode, gDiagram)

            self.diagrams.append(gDiagram)

    def getDependency(self, pNode, gDiagram):

        # Initial hierarchy
        pArc0 = pNode.code

        # Void infinit loop
        if pArc0 in gDiagram['labels']:
            gDiagram['arcs'].append({
                'n0': pArc0,
                'n1': pArc0
            })
            return

        # Add Parent
        gDiagram['labels'].add(pArc0)

        for pChild in pNode.ref_set.all():

            pArc1 = pChild.code

            gDiagram['arcs'].append({
                'n0': pArc0,
                'n1': pArc1
            })

            self.getDependency(pChild, gDiagram)
#           self.labels.add(pArc1)

    def generateDotModel(self):

        # Dibuja las entidades
        for gDiagram in self.diagrams:

            self.dotSource += '\nsubgraph cluster_{0} {{\n'.format(
                gDiagram.get('code'))
            self.dotSource += 'style=dotted;'

            self.dotSource += 'label="{0}";\n'.format(
                gDiagram.get('label', ''))

            # Labels
            for gArc in gDiagram['labels']:
                self.dotSource += '{0} [label="{1}"]\n'.format(
                    slugify3(gArc), gArc)
            self.dotSource += '\n'

            for gArc in gDiagram['arcs']:
                self.dotSource += '  {0} -> {1} {2}'.format(
                    slugify3(gArc['n0']), slugify3(gArc['n1']), self.lnkStyle)

            self.dotSource += '}\n'
        self.dotSource += '}'

        return self.dotSource
