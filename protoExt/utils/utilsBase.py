# -*- encoding: utf-8 -*-

# some common routines
# Compiled by : Dgt 11/11  - 15/06

import os, re, json 

from django.utils.encoding import smart_str
from django.utils import six
from protoExt.utils.utilsConvert import slugify2



def compare_dictionaries(dict1, dict2):
    """
    Object (dict) comparaison 
    """
#     return 0 if x==y else (-1 if x<y else 1)    
    if dict1 == None or dict2 == None:
        return False

    if type(dict1) is not dict or type(dict2) is not dict:
        return False

    if dict1.__eq__( dict2 ):
        return True

    shared_keys = set(dict2.keys()) & set(dict2.keys())

    if not ( len(shared_keys) == len(dict1.keys()) and len(shared_keys) == len(dict2.keys())):
        return False


    dicts_are_equal = True
    for key in dict1.keys():
        
        if type(dict1[key]) != type(dict2[key]): 
            dicts_are_equal = False 

        elif type(dict1[key]) is dict:
            dicts_are_equal =  compare_dictionaries(dict1[key],dict2[key])
 
        elif type(dict1[key]) is list:
            dicts_are_equal = compare_lists( dict1[key], dict2[key] )

        else:
            dicts_are_equal =  (dict1[key] == dict2[key])

        if not dicts_are_equal: 
            return False 
        
    return dicts_are_equal
 
def compare_lists(list1, list2):
    """
    Minimal list comparaison, 
    Las listas deben venir en el mismo orden 
    """

    if len( list1 ) != len( list2 ):
        return False 

    if len( list1 ) == 0:
        return True 

    if list1.__eq__( list2 ):
        return True

    lists_are_equal = True
    for ix in range(len(list1)):

        if list1[ix] in list2 :
            continue 

        if type( list1[ix] ) != type( list2[ix] ):
            lists_are_equal = False

        elif type(list1[ix]) is dict:
            lists_are_equal =  compare_dictionaries(list1[ix],list2[ix])
 
        elif type(list1[ix]) is list:
            lists_are_equal = compare_lists( list1[ix], list2[ix] )

        else:
            lists_are_equal =  (list1[ix] == list2[ix])

        if not lists_are_equal: 
            return False 

    return lists_are_equal
 

def traceError():
    from django.conf import settings

    if settings.DEBUG:
        import traceback 
        traceback.print_exc()
    else: 
        import logging
        logging.basicConfig( filename = settings.LOG_FILE, level=logging.DEBUG)        
        logging.info("Exception has occured" ,exc_info=1)    


def random_string_generator(size=6, chars=None):
    import string, random
    if not chars: chars = string.ascii_uppercase
    return ''.join(random.choice(chars) for x in range(size))  # @UnusedVariable


def verifyList(obj, defList = []):
#   Los objetos del admin son en su mayoria del tipo tuple,
#   Es necesario convertirlos a listas por facilidad de trabajo
    if isinstance( obj , six.string_types ):
        try:
            obj = json.loads(obj)
        except :
            obj = []
    elif isinstance( obj, tuple  ):
        obj = list( obj )

    if isinstance( obj, list ):
        if  len( obj ) == 0 :
            obj  = defList
        return obj

    else:
        return []

def verifyStr( vrBase , vrDefault ):
    sAux = vrBase or vrDefault
    return  u'%s' % sAux


def parseEmailAddress(fullemail, delimitorLeft = '<', delimitorRight = '>'):
    """
        split a full name/email pair to name/email tuple
        matches :
        # julien@bouquillon.com
        # Julien Bouquillon <julien@bouquillon.com>
    """

    if delimitorLeft == '(':
        delimitorLeft = '\\('
    if delimitorRight == ')':
        delimitorRight = '\\)'

    reg = re.compile('([^%s\n]+) ?%s?([^%s\r\n]+)?%s?' % (delimitorLeft, delimitorLeft, delimitorRight, delimitorRight) )

    matches = reg.findall(fullemail)

    if matches:
        (name, email) = matches[0]
        if email == '':
            email = name
        return (name, email)

    return None


def guessNextPath(dst, slugify2 = True, idx = 0, checkExists = True):
    """ return a renamed path if provided one already exists
        if slugify2, file name is slugified first (fs encodings problems quick & dirty workaround)
    """
    newpath = dst
    if idx == 0:
        (path, file) = os.path.split(newpath)
        (file, ext) =  os.path.splitext(file)
        slug = slugify2(file)

        newpath = os.path.join(path, '%s%s' % (slug, ext))

    if checkExists and os.path.isfile(newpath):
        idx += 1
        name, ext = os.path.splitext(newpath)
        newpath = '%s-copy%s' % (name, ext)
        return guessNextPath(newpath, slugify2, idx, checkExists)

    return newpath


def unique_id(more = ''):
    import time
    a = str(time.time())
    import random
    a += '-%s' % str(random.randint(2000, 10000))
    a += '-%s' % str(random.randint(0, 2000))
    a += more
    return a



def reduceDict(old_dict, keep_keys):
    """ keep only keep_keys in the dict (return a new one) 
        old_dict : {}
        keep_keys : []
    """
    return { keep_k: old_dict[keep_k] for keep_k in keep_keys }


def dict2tuple(indict):
    atuple = tuple()
    for item in indict:
        atuple += ((item, indict[item]),)
    #print atuple
    return atuple


def list2dict(alist , key ):
    # Convierte una lista de objetos en dict usando key como llave del dict.
    aDict = {}
    for item in alist:

        #Verifica si es un dict
        if isinstance( item, dict ):
            aDict[ item[key] ]  = item

        # si es un string lo crea con el key por defecto
        elif isinstance( item, str ):
            aDict[ item  ]  = { key : { key : item }}

    return aDict


def CleanFilePath(inFileName):
    """ assure qu'un nom de fichier n'est bien qu'un nom de fichier (remove slashes) """
    inFileName = os.path.basename(inFileName)
    inFileName = inFileName.replace('/', '')
    inFileName = inFileName.replace('\\', '')
    return inFileName


def CheckPathSecurity(testPath, rootPath):
    if not os.path.realpath(testPath).startswith(rootPath):
        raise Exception("forbidden path %s !" % os.path.realpath(testPath))


def PathToList(inPath, template_type="", showExt = True):
    mylist = []
    for file in os.listdir(inPath):
        if file in ['.', '..', '']:
            continue
        if not os.path.isfile(os.path.join(inPath, file)):
            continue
        if not showExt:
            file = os.path.splitext(file)[0]
        mydict = {"name": file, "type": template_type}
        mylist.append(mydict)
    return mylist


def strip_html(inHtml):
    # regularExp
    #    import re
    inHtml = re.sub(r'<br>', '\n', inHtml)
    inHtml = re.sub(r'</td><td>', ' - ', inHtml)
    inHtml = re.sub(r'</tr>', '\n\n', inHtml)
    inHtml = re.sub(r'</table>', '\n\n', inHtml)
    inHtml = re.sub(r'</p>', '\n\n', inHtml)
    inHtml = re.sub(r'<[^>]*?>', '', inHtml)
    inHtml = re.sub(r'<style>[^>]*</style>', '', inHtml)

    return inHtml

def strip_accents(inStr):
    inStr = u'%s' % inStr
    drep = {}
    drep["e"] = u'éêèë'
    drep["a"] = u'àâä'
    drep["i"] = u'îï'
    drep["c"] = u'ç'
    drep["u"] = u'ùû'
    drep["o"] = u'ôòö'

    drep["E"] = u'ÉÊÈË'
    drep["A"] = u'ÀÂÄ'
    drep["I"] = u'ÎÏ'
    drep["C"] = u'Ç'
    drep["U"] = u'ÙÛ'
    drep["O"] = u'ÔÒÖ'

    for k in drep.keys():
        for ch in drep[k]:
            inStr = inStr.replace(ch, k)

    # De todas formas lo estandariza
    return slugify2( inStr )

def strip_euro(inStr):
    inStr = u'%s' % inStr
    inStr = inStr.replace(u'€', u'euro(s)')
    return inStr




# Utilizado para campos q no tienen relacion en el modelo,
class VirtualField(object):
    def __init__(self, name):
        self.name = name



def getReadableError( e ):
    sAux = '<b>ErrType:</b> ' + type( e ).__name__ + '<br>'
    sAux +=  smart_str( e )

#    if len( e.args ) > 1: sAux += '<br>' +  str( '; '.join( e.args ))
    return sAux + '<br>'


def strNotNull(  sValue, sDefault ):
    if (sValue is None):
        if (sDefault is None):
            return "_"
        else:
            return sDefault
    else:
        return sValue


def copyProps ( objBase, objNew ):
    "Adiciona las propiedades a un objeto base igual q Ext.apply "
    "Todo: xxx.update : un metodo directo para hacerlo   destination.__dict__.update(source.__dict__) "
    for mProp in objNew:
        objBase[ mProp ] = objNew[ mProp ]

    return objBase



def copyModelProps ( objfrom, objto, props  ):
    """copia valores de una instancia de modelo a otro
    """
    for n in props:
        if hasattr(objfrom, n):
            v = getattr(objfrom, n)
            try: 
                setattr(objto, n, v);
            except:
                continue

    return objto


import unicodedata
def stripAccents(s):
    return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))




def explode(s):
    ''' Uso:
    explode( 'fName(p1,p2)' )
    ['fName', 'p1,p2']

    alternativas mas poderosas
        http://docs.python.org/2/library/ast.html#ast.parse

    import re
    '''

    pattern = r'(\w[\w\d_]*)\((.*)\)$'
    match = re.match(pattern, s)
    if match:
        return list(match.groups())
    else:
        return []



def repStr(string_to_expand, length):
    #Repeat to length  ( indent, fill, ... )
    return (string_to_expand * ((length/len(string_to_expand))+1))[:length]



class Enum(tuple):
    """
    How to use it (forward and reverse lookup, keys, values, items, etc.)

    >>> State = Enum(['Unclaimed', 'Claimed'])
    >>> State.Claimed
    1

    >>> State[1]
    'Claimed'

    >>> State
    ('Unclaimed', 'Claimed')

    >>> range(len(State))
    [0, 1]

    >>> [(k, State[k]) for k in range(len(State))]
    [(0, 'Unclaimed'), (1, 'Claimed')]

    >>> [(k, getattr(State, k)) for k in State]
    [('Unclaimed', 0), ('Claimed', 1)]
    """
    __getattr__ = tuple.index


def getClassName( cName ):
    # Formatea un string tipo titulo
    return ''.join( slugify2( cName ).title().split('-') )
