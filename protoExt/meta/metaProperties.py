# -*- coding: utf-8 -*-

"""
 Objetos utilizados por la pci,

 Sirve para generar y validar la estructura de un json a partir de la definicion q se haga aqui
 tambien debe servir para la creacion del arbol de la plc y las validaciones necesarias

 El marcador ( atrr ) del objeto corresponde al "__ptType" y es el nombre del objeto aqui definido

 La definicion tiene las siguientes propiedades

      description
      lists
      objects
      properties              # Son valores simples: string, number, bool
      roProperties            # readOnly en la pcl, deben preexistir en properties

 Los objetos de tipo list contienen ademas, esto permite agregar instancias en la pcl

       listOf

 Tambien se puede aplicar un valor por defecto, por
 ejemplo en listDisplay  = ['__str__']

      prpDefault : ['__str__']

 Si se desea cambiar el tipo de definicion:

       __ptType  lleva a la definicion correcta

 Para la edicion en la pcl contienen

       __ptStyle  [ jsonText, colList ]

 --- Una plantilla de la form

{
    "description": "Lista de acciones backend",
    "listOf" : "actionDef"
    "properties": [],
    "roProperties" : [],
    "objects": [],
    "lists": [],
    "roProperties": []
},

-- Determina el nombre del nodo en las listas

"nodeName" : "filterName",

-- Permite agregar un template en caso de nodos json

"__ptStyle" : "jsonText"

"addTemplate" : "{\"listDisplay\":{},\"name\": \"@name\"}",

--  Creacion de nodos

"allowAdd" : true            //  requiere un listOf
"listOf" : "filtersSetDef",


--  FieldSet
 El layout column permite un manejo flexible
 fluid:  Si no se especifica el "columnWidth"  es flexible
 xCol :Dependiendo el numero de columnas el "columnWidth"  puede ser 1, 0.5, 0.33
 fix  : Se especifica el "width"  ( si se especifica el width prima sobre la definicion )


"""


META_PROPERTIES = {
    
    "versionMeta" : '14.0201', 
    "metaVersion.help": "Version interna de la meta",
    "userVersion.help": "Version de usuario ( editable )",

    "exportCsv.help": "Permite exportar la definicion de fields en formato csv",
    "exportCsv.type": "boolean",

    "localSort.help": "Ordenamiento local, por defecto para prototipos",
    "localSorttype": "boolean",

    "pageSize,help": "buffer de lectura ( 50 por defecto )",
    "pageSize.type": "number",

    "qbeHelp.type": "boolean",
    "qbeHelp.help": "determina si aparece o no el trigger para el select distinct",

    "required.type": "boolean",
    "readOnly.type": "boolean",
    "primary.type": "boolean",

    "viewEntity.help": "Opcion de base de la pci (apunta directamente al modelo Django  app.modelo)",
    "viewCode.help": "Definicion de view interface - puede ser = al protoConcpeto o definir un nivel adicional app.modelo.vista",
    "description.help": "Text descriptivo",
    "viewIcon.help": "iconName tal como se define en el css",
    "shortTitle.help": "Titulo del menu y de la forma" ,
    "idProperty.help": "Campo q sirve como Id en el modelo, Django definie por defecto un Id, no es necesario definirlo explitamente",

    "protoEntity.help": "Corresponde a la entidadBase en los prototipos ( prototype.protoTable.xxx ) acompana a protoEntityId",

    "pciStyle": "grid",
    "pciStyle.help": "Presentation style [ form,  grid, tree]",
    "pciStyle.choices": ["grid", "form", "tree"],

    "treeRefField.help": "AutoRef field",

    "gridSelectionMode.choices": ["multiple", "simple", "single" ],
    "gridSelectionMode.help":  "multiple*: multiple selection con check o control; simple: selection on/off ; single: solo ultimo seleccionado",

    "denyAutoPrint.type": "boolean",
    "denyAutoPrint.help": "Impide la impresion automatica de la grilla",

    "masterField": "pk",

    "menuText.help": "titulo en el menu ( toolbar )",
    "detailName.help": "key del detalle usada para encadenar los reportes ",

    "conceptDetail.help": "Entidad detalle de la relacion ( [App.]Model o [App.]Model.View )",
    "masterField.help": "Campo en el maestro para q contiene el criterio para el filtro del detalle, (normalmente Pk si es un detalle directo)",
    "detailField.help": "Campo del detalle para hacer el filtro, normalmente el nombre de la tabla padre en minuscula",
    "detailTitleLbl.help": "Titulo en el detalle para indicar el filtro actual",

    "masterTitleField.help": "Campo en el maestro que se utiliza para construir el titulo de la vista filtrada en el detalle",
    "detailTitleField.help": "Campo en el detalle donde se copia el valor del titulo del maestro ( default de la llave padre en la edicion )",

    "propertyPrefix": "udp",
    "propertyPrefix.help": "prefijo de las propiedades definidas por el usuario ( en el nombre del campo aparencen upd__xxxxx)",
    "propertyName.help": "campo que contiene la llave de la propiedad",
    "propertyValue.help": "campo que contiene el valor",

    "propertyRef.help": "REQUERIDO: Campo en la udp q apunta a la tabla base",
    "keyField.help": "Campo leido del registro de base<br>** Solo se debe setear cuando la udp no es un MD",
    "udpTable.help": "Tabla que contiene las upds, <b>** Si es un vinculo directo corresponde al related_name q es el set de detalles, normalmente la tablaUdp comenzando por minuscula",

    "sheetSelector.help": "Campo de criterio para seleccionar el template, vacio para una unica plantilla por defecto DEFAULT",
    "template.help": "Definicion de la plantilla",

    "templateFp.help": "Templante FirstPage",
    "templateLp.help": "Templante LastPage",

    "templateBb.help": "Templante BeforeBlock",
    "templateAb.help": "Templante AfterBlock",

    "templateBb": "<spam>------------------------------------</spam><br>",
    "templateAb": "<spam>====================================</spam><br>",

    "templateEr.help": "EveryRow",

    "templateFp": "'<!DOCTYPE html>' + '<html>' + '<head>' + '<meta content=\"text/html; charset=UTF-8\" http-equiv=\"Content-Type\" />' + '<link href=\"/static/css/print.css\" rel=\"stylesheet\" type=\"text/css\" media=\"screen,print\" />' + '<title>PtReport : {{reportTitle}}</title>' + '</head>' + '<body>'",

    "templateLp": "'</body>' + '</html>'",

    "direction": "sort order",
    "direction.choices": ["ASC", "DESC" ],

    "physicalName.help": "Nombre fisico o funcion por ejemplo @str( f1,f2 )",
    "required": False,
    "required.help": "Requiere valores la forma",
    "allowDecimals.help": "NO USAR : si permite o no decimales, si decimalPReciosion = 0 implica falso",
    "autoscroll": True,
    "autoscroll.help": "t/f",

    "choices.help": "lista de valores separados por coma para el combobox",

    "collapsed": False,
    "collapsed.help": "t/f aparece contraido",
    "collapsed.type": "boolean",

    "collapsible": False,
    "collapsible.help": "t/f",
    "collapsible.type": "boolean",

    "cellToolTip.help": "Presenta contenido del campo como micro ayuda",
    "cellToolTip.type": "boolean",

    "cellLink.help": "Show microhelp",
    "cellLink.type": "boolean",

    "qbeField.help": "QBE field",
    "qbeField.type": "boolean",

    "xtype.help": "Tipo de objeto en el frontEnd ( puede ser manipulado con el vType)",
    "xtype.choices": ["", "textfield", "combobox", "checkbox", "numberfield", "textarea", "datefield" ],

    "prpScale": 0,
    "prpScale.help": "Cantidad de decimales permitidos ( 0 para enteros 2 para decimales )",
    "prpDefault.help": "valor por defecto",

    "fieldLabel.help": "label en la forma",
    "format.help": "mascara del campo ( automatico para las fechas, horas y numeros )",
    "fsLayout": "fluid",
    "fsLayout.choices": ["fluid", "1col", "2col", "3col" ],
    "fsLayout.help": "distribucion de los campos en el contenedor",

    "header.help": "Encabezado de la collumna en modo grilla ( default para fieldLabel ) " ,

    "height.type": "number",
    "height.help": "The height value in pixels",
    "helpPath.help": "se define como : /help/xxxx.html  esta en: /static/help",

    "hidden.help": "componente oculto",
    "hidden.type": "boolean",

    "hideLabel.help": "presenta los campos sin label, util cuando se configura grupos como firstName, lastName",
    "hideSheet.help": "Oculta la ficha descriptiva",

    "hideRowNumbers.help": "Oculta la columna que numera los campos",
    "hideRowNumbers.type": "boolean",

    "hideCheckSelect.type": "boolean",
    "hideCheckSelect.help": "Permite seleccionar multiples registros",

    "filterSetABC.help": "Genera automaticamente filtro alfabetico sobre la columna seleccionada",

    "labelAlign": "left",
    "labelAlign.choices": ["left", "top"],
    "labelAlign.help": "opciones left top",

    "labelWidth.help": "ancho del label",

    "maxHeight.help": "The max value in pixels",
    "maxWidth.help": "The max value in pixels",

    "maxHeight.type": "number",
    "maxWidth.type": "number",

    "minHeight.help": "The minimum value in pixels",
    "minWidth.help": "The minimum value in pixels",

    "minHeight.type": "number",
    "minWidth.type": "number",

    "height.type": "number",
    "width.type": "number",

    "flex.type": "number",
    "flex.help": "Recalcula el ancho en funcion de la forma y el peso ( flex) asignado",

    "readOnly": False,
    "readOnly.help": "campo de solo lectura",
    "title.help": "Titulo del componente",
    "tooltip.help": "microayuda del componente ",

    "sortable.help": "t/f",
    "sortable.type": "boolean",

    "type.help": "Tipo de dato de la Db ",
    "type.choices": [ "", "string", "text", "bool", "int", "decimal", "combo", "date",  "datetime", "time", "autofield", "html", "foreignid",  "foreigntext"  ],

    "vType.help": "TODO: Tipo de dato de validacion  ",
    "vType.choices": [ "", "email", "ip4", "ip6", "tel", "postalCodeCA", "postalCodeUSA"  ],

    "width.help": "The width value in pixels",

    "wordWrap.type": "boolean",
    "wordWrap.help": "ver el contenido en mas de una linea",

    "sheetType.help": "Tipo de hoja ( usada para reportes ) ",
    "sheetType.choices": [ "", "printerOnly", "gridOnly"],

    "detailName.help": "Nombre correspondiente a un detalle declarado en la opcionBase correspondiente ( padre )",

    "actionType.help": "Tipo de accion ( metodos backend ) ",
    "actionType.choices": [ "user", "insTrigger", "updTrigger", "delTrigger", "wflow"],
    "refreshOnComplete.type": "boolean",

    "paramType.help": "Tipo de dato del parametro",
    "paramType.choices": [ "", "string", "bool", "number"],

    "cpFromField.help": "Copy the contents of a field in another, in the case of default or zooms",
    "cpFromZoom.help": "Field pointing to the referenced model (no points to zoom as several fields can use the same zoom)",

    "crudType.help": "Field Behavior editing in Db",
    "crudType.choices": [ "", "editable", "readOnly", "insertOnly", "updateOnly", "screenOnly", "storeOnly" ],

    "selectionMode.help": "En las acciones determina el tipo de seleccion en la grilla",
    "selectionMode.choices": [ "none", "single", "multiple" ], 

    "actioConfirm": False,
    "actioConfirm.help": "t/f",
    "actioConfirm.type": "boolean",

}