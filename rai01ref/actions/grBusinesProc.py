#!/usr/bin/env python
"""
Prototype to DOT (Graphviz) converter by Dario Gomez
Table format from  django-extensions 
"""

from protoExt.utils.utilsBase import getClassName
from protoExt.utils.utilsConvert import slugify3


class BusinessProcess():

    def __init__(self):

        self.tblStyle = False
        self.lnkStyle = '\n'

        self.dotSource = 'digraph bp {'
        self.dotSource += 'fontname="Helvetica";fontsize = 8;\n'
        self.dotSource += 'rankdir = LR;\nnode [shape=box,style=rounded,width=0,height=0,concentrate=true];\n'

        # self.dotSource += 'start [label=" ",shape=circle,width=0.3]\n'
        self.dotSource += 'end [label=" ",shape=circle,width=0.3,style=bold]\n'

    def getDiagramDefinition(self, queryset):

        self.diagrams = []

        for pDiag in queryset:

            gDiagram = {
                'code': getClassName(pDiag.code),
                'label': pDiag.code,
                'showBorder': getattr(pDiag, 'showBorder', False),
                'arcs': [],
                'labels': set()
            }

            # Initial and final nodes
            for pDiagComposition in pDiag.artefactcomposition_set.all():

                #  Initial node == container => Start
                pArc0 = pDiagComposition.inputArt.code
                gDiagram['labels'].add(pArc0)

                #  Final node == null => End
                try:
                    pArc1 = pDiagComposition.outputArt.code
                    gDiagram['labels'].add(pArc1)
                except:
                    pArc1 = 'End'

                gDiagram['arcs'].append({
                    'n0': pArc0,
                    'n1': pArc1
                })

            self.diagrams.append(gDiagram)

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

                if gArc == gDiagram['label']:
                    self.dotSource += '{0} [label="{1}",shape=ellipse]\n'.format(
                        slugify3(gArc), gArc)
                else:
                    self.dotSource += '{0} [label="{1}"]\n'.format(
                        slugify3(gArc), gArc)
            self.dotSource += '\n'

            for gArc in gDiagram['arcs']:
                self.dotSource += '  {0} -> {1} {2}'.format(
                    slugify3(gArc['n0']), slugify3(gArc['n1']), self.lnkStyle)

            self.dotSource += '}\n'
        self.dotSource += '}'

        return self.dotSource
