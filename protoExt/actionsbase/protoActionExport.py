# -*- coding: utf-8 -*-


def protoExport(request):


    if not request.user.is_authenticated():
        return JsonError('readOnly User')

    if request.method != 'POST':
        return JsonError('invalid message')

    protoMeta = request.POST.get('protoMeta', '')
    protoMeta = json.loads(protoMeta)

    protoFilter = request.POST.get('protoFilter', '')
    baseFilter = request.POST.get('baseFilter', '')
    sort = request.POST.get('sort', '')

#   Obtiene las filas del modelo
    Qs, orderBy, fakeId, refAllow = getQSet(protoMeta, protoFilter, baseFilter , sort , request.user)

    # El refAllow no es necesario para reportes
    refAllow = refAllow and False

    if orderBy:
        pRows = Qs.order_by(*orderBy)
    else:
        pRows = Qs.all()

#   Prepara las cols del Query
    try:
        pList = Q2Dict(protoMeta , pRows, fakeId)
    except Exception as e:
        message = getReadableError(e)
        pList = [ message ]

    filename = protoMeta.get('viewCode', '') + '.csv'
    fullpath = getFullPath(request, filename)

    import codecs
    with codecs.open(fullpath , 'w', 'utf-8') as outfile:
        outfile.write(getLineCsv(pList[0].keys()))
        for row in pList:
            outfile.write(getLineCsv(row.values()))

    return  JsonSuccess({ 'message':  filename })
