from django.template import Library, Node
register = Library()


class PydevDebugNode(Node):
    def render(self, context):
        try:
            import pydevd #@UnresolvedImport
            pydevd.connected = True
            pydevd.settrace()
            return ''
        except:
            # It might be more clear to just let this exception pass through
            return 'Debugger was not turned on'

@register.tag
def pydev_debug(parser, token):
    return PydevDebugNode()


# from django import template
# 
# register = template.Library()
# 
# @register.filter
# def pydev_debug(*args, **kwargs ):
#     # In pydev, doing pydevd|ctrl+space will show template for pydevd.settrace() 
#     # with code below with the proper path to emulate breakpoint.
#     import sys
#     sys.path.append(r'path/to/eclipse/plugins/org.python.pydev/pysrc')
#     
#     import pydevd  # @UnresolvedImport
#     pydevd.settrace() #Emulate breakpoint