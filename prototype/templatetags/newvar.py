from django.template.base import Library, Node, TemplateSyntaxError

register = Library()

@register.tag
def newvar(parser, token):
    """
    Encadena las variables y retorna una nueva 

    You can use any number of values, separated by spaces. Commas can also
    be used to separate values; if a comma is used, the newvar values are
    interpreted as literal strings.

    {% newvar 'row1' 'row2' as rows %}

    """

    args = token.split_contents()

    if len(args) < 2:
        raise TemplateSyntaxError("'newvar' tag requires at least two arguments")

    if len(args) >= 3:
        # {% newvar ... as foo %} case.
        if args[-2] != "as":
            raise TemplateSyntaxError("newvar requires v1 as v2")

    name = args[-1]
    values = [parser.compile_filter(arg) for arg in args[1:-2]]

    node = NewvarNode(values, name)
    if not hasattr(parser, '_namedNewvarNodes'):
        parser._namednewvarNodes = {}
    parser._namednewvarNodes[name] = node


    return node


class NewvarNode(Node):
    def __init__(self, impvars, asvar=None):
        self.impvars = impvars
        self.asvar = asvar


    def render(self, context):
        outvar = ''.join(map(str, self.impvars))

        if self.asvar:
            context[self.asvar] = outvar
            return ''
