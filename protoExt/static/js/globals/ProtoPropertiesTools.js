/* 
 * Property Definition  
 *      help         : description 
 *      type    
 *      choices      : lista de valores en caso de ser string 
 *      required     : 
 * 
 *  prpDefault solo se aplcia si no existe y es requerida  
 */


_SM.getSimpleProperties = function( oData, ptType ){
    // The type definition is : xxx.type = [ 'boolean' | 'date' | 'string' | 'number' ] 
    // Retorna los valores simples, verificando los tipos de cada propiedad
    // Solo deben llegar objetos, si llega un array no hay props q mostrar
    if (_SM.typeOf(oData) == 'array') {
        return [];
    }

    // Inicializa con el type
    var cData = {}, cValue;
    
    if (ptType) {
        cData.__ptType = ptType;
    }

    for (var lKey in oData ) {
        cValue = oData[lKey];

        // Los objetos o arrays son la imagen del arbol y no deben ser tenidos en cuenta, generarian recursividad infinita
        if (_SM.typeOf(cValue) in _SM.objConv(['object', 'array'])) {
            continue;
        }

        // Si son valores codificados, los decodifica y los agrega
        if ( lKey in _SM.objConv(['__ptValue', '__ptList'])) {
            try {
                cData = Ext.decode(cValue);
            } catch (e) {
                // console.log( "Error de encodage", cValue )
            }

        } else {
            cValue = _SM.verifyPrpType(lKey, cValue);
            if (cValue) {
                cData[lKey] = cValue;
            }
        }
    }
    return cData;

};


_SM.verifyPrpType = function(   lKey,  cValue ){
    /* Verifica los tipos de las  propiedades
     * recibe el valor y el tipo y verifica si 
     * corresponden entre si
     * 
     * Intenta la conversion, sin no regresa nulo 
     */ 
    
    var pType = _SM._MetaProperties[ lKey + '.type' ]; 
    if ( ! pType )  { 
        if ( typeof ( cValue ) == 'string') { return cValue.replace(/~+$/, '');  }
        else { return cValue; }      
    }
    
    if ( pType == typeof( cValue ) ) 
    { return cValue;  }    
    
    switch ( pType ) {
    case "boolean":
        if  ( (typeof( cValue ) == 'number') ){ cValue = cValue.toString(); }
        if  ( (typeof( cValue ) == 'string') ){
            if ( cValue.substr(0,1).toLowerCase()  in _SM.objConv([ 'y', 's', '1','o', 't' ]) )
            { return true; } else { return false; } 
        } else { return false; }  
    case "number":
        return parseFloat( cValue );
    case "null":
        return null; 
    default:
        return cValue;
    }
}



_SM.prepareProperties = function( record , myMeta,  propPanel  ){
    /* Pepara la tabla de propiedades
     * retorna propPanel
     */

    var template = {};

    // var parentType = ''
    // if ( record.parentNode ) parentType  =  record.parentNode.data.text

    // La data configurada
    var __ptConfig  =  _SM.clone( record.data.__ptConfig ),
        __ptType = record.data.__ptType,
        __ptText = record.data.text, 
        myFieldDict = _SM.getFieldDict( myMeta );

    if ( __ptType  in _SM.objConv( [ 'field', 'formField' ]) ) {

        // Default Data ( aplica los defaults a la pcl y luego a la definicion del campo )
        template = _SM.getTemplate( __ptType, false, myFieldDict[ __ptText  ] );
        __ptConfig[ 'name' ]  = __ptText;

    // } else if ( __ptType  in _SM.objConv( [ 'detailDef', 'sheetConfig' ]) ) {
        // template = _SM.getTemplate( __ptType, false  )

    }  else {
        // Default Data ( El nombre del nodo es el tipo de datos real )
        template = _SM.getTemplate( __ptType , false  );
    }

    // Default Data ( aplica los defaults a la definicion del campo )
    __ptConfig = Ext.apply(  template.__ptConfig, __ptConfig   );

    // Solo maneja las propiedades propias de la version
    __ptConfig = _SM.clearPhantonProps( __ptConfig,  __ptType );

    propPanel.setSource( __ptConfig );
    propPanel.setCombos( template.__ppChoices );
    propPanel.setTypes( template.__ppTypes );

    propPanel.readOnlyProps = ['__ptType', 'name'].concat ( template.__roProperties );
    propPanel.sourceInfo = template.__ptHelp;

};




_SM.getTemplate = function( ptType, forForm,  metaField  )  {
    // TODO:  agregar en la definicion del campo un colList para hacer un combo automatico con los nombres de campo
    //@forForm boolean for Form Definition

    var prps = {}, qtips = {}, choices = {}, ppTypes = {};
    var prpName, prpValue, prpHelp, prpChoices, prpDict, prpType;

    // Lee la plantilla de la variable publica
    var objConfig = _SM._MetaObjects[ ptType ] || {};

    // Recorre el vector de propieades
    // puede ser solo el nombre o la tupla name, value
    // [ 'x' , { 'name' : 'xxx' , 'value' : '' }]
    for (var ix in objConfig.properties  ) {
        var prp  = objConfig.properties[ ix ];

        // Trae los valores directamente
        if ( _SM.typeOf( prp ) == 'object' ) {
            prpName = prp.name;
            prpValue = prp.value;
        } else {
            prpName = prp;
            prpValue =  _SM._MetaProperties[ prpName ] || null;
        }


        prpHelp =  _SM._MetaProperties[ prpName + '.help'];
        prpChoices =  _SM._MetaProperties[ prpName + '.choices'];
        prpType =  _SM._MetaProperties[ prpName + '.type'];

        // Para presentacion en la forma o en las propiedades
        if (forForm) {
            if ( prpValue )  prps[ prpName ] = prpValue;

        } else {
            prps[ prpName ] = prpValue || '';
            qtips[ prpName ] = prpHelp;
            if ( prpChoices )   choices[ prpName ] = prpChoices;
            if ( prpType )   ppTypes[ prpName ] = prpType;
        }


    }

    // Si es un campo obtiene los defaults de fields
    if ( metaField ) {
        prpDict = _SM.getFormFieldDefinition( metaField );
        prps = Ext.apply( prps, prpDict   );
    }

    // Garantiza q no venga una definicion generica ( solo para los formFields )
    if ( forForm && ( ! prps.xtype  )) prps.xtype = ptType;
    if ( ( prps.xtype == 'formField' ) &&  ( ptType == 'formField' )) prps.xtype = 'textfield';


    return {'__ptConfig' : prps,
            '__ptHelp' : qtips,
            '__ppChoices' : choices,
            '__ppTypes' : ppTypes,
            '__roProperties' : objConfig.roProperties || []
            };

}



_SM._MetaProperties =  {

    "metaVersion.help" : "Internal meta version", 
    "userVersion.help" : "Application version",
     
    "exportCsv.help"   : "Csv export enabled?",   
    "exportCsv.type" : "boolean", 

    "localSort.help" : "local sort?, (n/a for prototypes)", 
    "localSorttype" : "boolean",
     
    "pageSize,help" : "Page size", 
    "pageSize.type": "number", 

//QBE    
    "qbeHelp.type":"boolean",
    "qbeHelp.help": "visible trigger for select distinct (interne)",

//  Types
    "required.type" : "boolean", 
    "readOnly.type"  : "boolean",
    "primary.type" : "boolean", 
    
// PCI
    "viewEntity.help" : "Backend model (Django)",
    "viewCode.help"  : "Definicion de view code -  app.model.view", 
    "description.help"  : "Description", 
    "viewIcon.help"  : "iconName  (css name)",
    "shortTitle.help" : "Menu and form title" ,
    "idProperty.help" : "Id property (future use)",

    "protoEntity.help" : "Default prototype entity ( prototype.protoTable.xxx )  (Internal use with protoEntityId)",
     
    "pciStyle" : "grid", 
    "pciStyle.help" : "Presentation mode [ form,  grid, tree]", 
    "pciStyle.choices": ["grid", "form", "tree"],

    "gridSelectionMode.choices": ["multi", "simple", "single" ], 
    "gridSelectionMode.help":  "multi*: multiple selection with check; simple: selection on/off ; single: Last selected", 

    "denyAutoPrint.type" : "boolean", 
    "denyAutoPrint.help" : "deny auto print (future use)", 

// Detalles 
    "masterField" : "pk",

    "menuText.help"         : "Menu title ( toolbar )", 
    "detailName.help"       : "Detail key (for report detail)", 
    
    "conceptDetail.help"    : "Detail concept ( [App.]Model o [App.]Model.View )",
    "masterField.help"      : "Master field for MD navigation (normaly Pk)",
    "detailField.help"      : "Detail field for filter (normaly conceptName)", 
    "detailTitleLbl.help"   : "Detail title for filter", 

    "masterTitleField.help" : "Master field title (filter name)", 
    "detailTitleField.help" : "Master field title (copy from master title in detail edition)", 

//  Udps 
    "propertyPrefix" : "udp", 
    "propertyPrefix.help" : "udp prefix (upd__xxxxx)", 
    "propertyName.help" : "udp property name",
    "propertyValue.help" : "udp property value",

    "propertyRef.help" : "udp concept ref",    
    "keyField.help" : "udp source<br>** Only for non MD udp (internal use)",
    "udpTable.help" : "udp concept name , <strong>** if direct link then related_name, normaly udpTable</strong>", 

// sheets
    "sheetSelector.help": "field sheet selecto, null for DEFAULT sheet",
    "template.help": "template definition", 

    "templateFp.help": "Templante FirstPage", 
    "templateLp.help": "Templante LastPage",
     
    "templateBb.help": "Templante BeforeBlock", 
    "templateAb.help": "Templante AfterBlock", 

    "templateBb": "<spam>------------------------------------</spam><br>", 
    "templateAb": "<spam>====================================</spam><br>", 

    "templateEr.help": "EveryRow", 

    "templateFp":'<!DOCTYPE html><html><head><meta content="text/html; charset=UTF-8" http-equiv="Content-Type" /><link href="/static/css/print.css" rel="stylesheet" type="text/css" media="screen,print" /><title>PtReport : {{reportTitle}}</title></head><body>',
    "templateLp":'</body></html>',

    "direction": "sort order",
    "direction.choices": ["ASC", "DESC" ],

//  Fields
    "physicalName.help" : "phisical name or function  @str( f1,f2 )", 
    "required": false,
    "required.help": "Required field",
    "allowDecimals.help": "Dont use!!! : allow decimal (internal use)",
    "autoscroll": true,
    "autoscroll.help": "t/f",

    "choices.help": "comma separed values for combo selection",
    
    "collapsed": false,
    "collapsed.help": "t/f collapsed",
    "collapsed.type": "boolean",

    "zoomMultiple": false, 
    "zoomMultiple.type": "boolean", 
    "zoomMultiple.help": "Multiple selection on add",

    "collapsible": false,
    "collapsible.help": "t/f",
    "collapsible.type": "boolean",

    "cellToolTip.help": "Use this field form line tooltip",
    "cellToolTip.type": "boolean",

    "cellLink.help": "Is a cellLink?",
    "cellLink.type": "boolean",

    "xtype.help" : "frontend widget (use vType also)",
    "xtype.choices": ["", "textfield", "combobox", "checkbox", "numberfield", "textarea", "datefield" ],
    
    "prpScale": 0,
    "prpScale.help": "Decimal scale ( 0 int, 2 dec )",
    "prpDefault.help": "Default value",
    
    "fieldLabel.help": "Field label (in form)",
    "format.help": "input mask (automatic for date, time and numbers) (future use)",
    "fsLayout": "1col",
    "fsLayout.choices": ["fluid", "1col", "2col", "3col" ],
    "fsLayout.help": "Automatic layout distribution",

    "header.help" : "Column header (grid)  default for fieldLabel" ,

    "height.type": "number",
    "height.help": "The height value in pixels",
    "helpPath.help": "/help/xxxx.html  real: /static/help",
    
    "hidden.help": "Hiden field (future use)",
    "hidden.type": "boolean",

    "hideLabel.help": "Hide label? (ex: firstName, lastName)",
    "hideSheet.help" : "Hide sheet?", 
    
    "hideRowNumbers.help" : "Hide row numbers?", 
    "hideRowNumbers.type"  : "boolean",
    
    "hideCheckSelect.type"  : "boolean",
    "hideCheckSelect.help" : "Hide check select?", 

    "filterSetABC.help" : "Auto alphabetic filter", 

    "labelAlign": "left",
    "labelAlign.choices": ["left", "top"],
    "labelAlign.help": "Label align (left, top)",

    "labelWidth.help": "Label width",

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
    "flex.help": "Flex width eqivalence", 

    "readOnly": false,
    "readOnly.help": "ReadOnly field?",
    "title.help": "Title",
    "tooltip.help": "Microhelp",
 
    "sortable.help": "Sortable?",
    "sortable.type": "boolean",

    "searchable.help": "Searchable?",
    "searchable.type": "boolean",

    "type.help" : "Field type", 
    "type.choices" : [ "", "string", "text", "bool", "int", "decimal", "combo", "date",  "datetime", "time", "autofield", "html", "foreignid",  "foreigntext"  ],             

    "vType.help" : "Validation type", 
    "vType.choices" : [ "", "email", "ip4", "ip6", "tel", "postalCodeCA", "postalCodeUSA"  ],             
    
    "width.help": "The width value in pixels",
    
    "wordWrap.type": "boolean",
    "wordWrap.help": "Auto wordWrap (more than one line)", 

    "sheetType.help" : "Sheet type (showPrint, Grid, Report)", 
    "sheetType.choices" : [ "showPrint", "printerOnly", "gridOnly"], 
    
    "detailName.help" : "Detail name (used in MD definition)",              

    "actionType.help" : "Action type (backend function)", 
    // Solo las acciones de tipo "user" son presentadas  en el menu
    // los triggers pueden ser escritos directamente en el modelo y no pasar por protoExt 
    "actionType.choices" : [ "user", "insTrigger", "updTrigger", "delTrigger", "wflow"], 
    "refreshOnComplete.type": "boolean",
    
    "paramType.help" : "Parameter type", 
    "paramType.choices" : [ "", "string", "bool", "number"], 

    "executeJS.help" : "js plugin?",  
    "executeJS.type" : "boolean",  

    "jsCode.help" : "executing code", 
//  "jsCode.type" : "", 


    "cpFromField.help" : "Derived by copy",  
    "cpFromZoom.help" : "Derived form zoom (fk property)? ", 
    
    "crudType.help" : "Crud type", 
    // editable      : es un campo estandar de la Db ( default )  
    // screenOnly    : ninguna iteraccion con la db, funciones calculadas en el frontEnd, o campos de procesamiento intermedio para generar otros campos     
    // storeOnly     : leido de la Db,  no se despliega en el frontEnd, se usa como resultado de campos calculados, usado para manejar subSets ( implica definir baseFilter, vrDefault  )
    // insertOnly    : campos invariables ( ej: nro documento, )      
    // updateOnly    : nulo al inicio, requerido en modificacion       
        
    // linked        : no es editable, no se guarda en la Db, requiere cpFromField,  cpFromZoom* ( *para prototipos, o zooms no relacionales )  
    // copied        : toma el vr por defecto de cpFromField o cpFromZoom ( similar a linked + editable )      
    "crudType.choices" : [ "", "editable", "screenOnly", "storeOnly", "insertOnly", "updateOnly", "linked", "copied" ], 
    
    "selectionMode.help" : "Grid selection mode for actions",
    // none : Envia la accion sin QSet 
    // single : Exige un unico reg 
    // multiple : Exige al menos un reg       
    // details : Envia la seleccion de detalles 
    "selectionMode.choices" : [ "none", "single", "multiple", "details" ], 

    "addDetailForm.help" : "Shortcut to the add form", 
    "addDetailForm.type" : "boolean"

};






_SM._versionMeta = '14.0201';
_SM._MetaObjects = {

    "pcl" : {
        "description" : "Meta definition",
        "properties" : [
                "viewCode", "viewEntity", "viewIcon", "description", "shortTitle", 
                "localSort", "pageSize", 
                "sheetSelector", "pciStyle", "helpPath", "idProperty", 
                "jsonField", "returnField", "updateTime", 
                "metaVersion", "userVersion", "protoEntity", "protoEntityId", "pciType"
                ],
        "objects" : ["gridConfig", "gridSets", "formConfig", "usrDefProps", "custom", "businessRules"],
        "lists" : ["fields", "fieldsBase", "fieldsAdm", "actions", "detailsConfig", "sheetConfig"],
        "roProperties" : ["viewEntity", "idProperty", "updateTime", "metaVersion", "protoEntity", "protoEntityId"]
    },

    "fields" : {
        "description" : "Store fields definition",
        "listOf" : "field"
    },

    "fieldsBase" : {
        "description" : "Base store fields definition",
        "listOf" : "field"
    },

    "fieldsAdm" : {
        "description" : "Admin store fields definition",
        "listOf" : "field"
    },

    "field" : {
        "description" : "A store field element",
        "properties" : ["name", "required", "prpLength", "prpScale", "prpDefault", "fieldLabel", "format", "header", "sortable", "searchable", "flex",
        // "height","maxHeight","minHeight",
        // "width", "maxWidth","minWidth",
        // "hideLabel",
        // "labelAlign","labelWidth",

        "tooltip",
        // "cellToolTip",
        // "qbeHelp",
        "cellLink", "wordWrap",

        // manejo
        "primary", "crudType", "readOnly", "hidden",

        // Para el combo
        "choices",

        // Para el zoom
        "fkId", "fkField", "cellLink", "zoomModel", "zoomFilter", "zoomMultiple",

        // Definien como heredar datos de otro campo ( ya se a de un zoom o del mismo rset )
        "cpFromField", "cpFromZoom",

        // Para los N2N
        // "conceptDetail",
        // "relatedN2N",
        // "detailField",
        // "masterField",
        "physicalName", "type", "xtype", "vType"],
        "roProperties" : []
    },

    "formField" : {
        "description" : "A field element",
        "properties" : ["name", "tooltip", "fieldLabel", "labelWidth", "labelAlign", "hideLabel", "required", "readOnly", "hidden", "prpDefault",
        // "height","maxHeight","minHeight",
        // "width", "maxWidth","minWidth",

        "format", "prpLength",

        // Para los campos del htmlSet
        "collapsed",

        // Para el combo
        "choices",

        // Para el zoom
        "fkId", "fkField", "zoomModel", "zoomFilter", "zoomMultiple", "cellLink",

        // Para los N2N
        // "conceptDetail",
        // "relatedN2N",
        // "detailField",
        // "masterField",

        // tipos
        "type", "xtype", "vType"],
        "roProperties" : ["type "]

    },

    "gridConfig" : {
        "description" : "Grid configuration properties",
        "properties" : [
            'hideRowNumbers',
            // 'hideCheckSelect',
            'gridSelectionMode', "exportCsv", 'hideSheet', 'denyAutoPrint', 'filterSetABC', 
            'groupCol'
        ],

        "lists" : ["listDisplay", "baseFilter", "initialFilter", "initialSort",

        // TODO: Eliminar de aqui y pasar a obj  colShortcuts
        "searchFields", // TODO: Cambiar por sercheable
        "sortFields", // TODO: Cambiar por sortable
        "hiddenFields", "readOnlyFields"],
        "objects" : [
        // "colShortcuts"
        ]

    },

    // TODO: Caundo se agrega aqui, al guardar actualiza fieldDefinition,
    // el agregar o borrar prevalece sobre la condicion del campo.
    "colShortcuts" : {
        "description" : "Column configuration shortcuts",
        "lists" : ["searchFields", // TODO: Cambiar por sercheable
        "sortFields", // TODO: Cambiar por sortable
        "hiddenFields", "readOnlyFields"

        // qbeAllowFields
        // textSearchFields
        ]
    },

    // Estos son actualizados por el staf ( admin de grupo )
    "gridSets" : {
        "description" : "Additional settings ( filters, sorters, userViews )",
        "lists" : ["listDisplaySet", "filtersSet", "sortersSet"]
    },

    // Estos son actualizados por los usuarios de base
    "custom" : {
        "description" : "custom user configurations",
        "lists" : ["listDisplay", "listDisplaySet", "filtersSet", "sortersSet"]
    },

    "baseFilter" : {
        "description" : "Default defined filter. No user-modifiable, e.g. { \"status__exact\":\"0\" } ",
        "listOf" : "filterDef",
        "allowAdd" : true
    },

    "customFilter" : {
        "description" : "Predefined filter ",
        "listOf" : "filterDef",
        "allowAdd" : true
    },

    "initialFilter" : {
        "description" : "Initial filter  Ej: { \"status__exact\":\"0\" } ",
        "listOf" : "filterDef",
        "allowAdd" : true
    },

    "initialSort" : {
        "description" : "Default ordering  Ej: [{\"direction\":\"ASC\",\"property\":\"code\"}, ... ] ",
        "listOf" : "sorterDef",
        "allowAdd" : true
    },

    "sorterDef" : {
        "description" : "Sort definition",
        "addPrompt" : "Please enter the name of the property for your sorter:",
        "allowDel" : true,
        "nodeName" : "property",
        "properties" : ["property", "direction"]
    },

    "sortersSet" : {
        "description" : "Sorter set",
        "listOf" : "sortersSetDef",
        "allowAdd" : true
    },

    "sortersSetDef" : {
        "description" : "Sorter set definition",
        "addPrompt" : "Please enter the name of the sorter:",
        "allowDel" : true,
        "properties" : ["name", "description"],
        "lists" : ["customSort"]
    },

    "customSort" : {
        "description" : "User ordering",
        "listOf" : "sorterDef",
        "allowAdd" : true
    },

    "filterDef" : {
        "description" : "Predefined filter definition",
        "addPrompt" : "Please enter the name of the property for your filter:",
        "allowDel" : true,
        "nodeName" : "property",
        "properties" : ["property", "filterStmt"]
    },

    "filtersSet" : {
        "description" : "Predefined filter set ( *x*, ><=, !=,  aa:bb ) ",
        "listOf" : "filtersSetDef",
        "allowAdd" : true
    },

    "filtersSetDef" : {
        "description" : "Filter set definition",
        "addPrompt" : "Please enter the name of the filterSet:",
        "allowDel" : true,
        "properties" : ["name", "menuText"],
        "lists" : ["customFilter"]
    },

    "listDisplaySet" : {
        "description" : "Alternative configuration for the grid ( it appears under the icon 'ViewCols' of the main bar )",
        "listOf" : "listDisplayDef",
        "allowAdd" : true
    },

    // El esquema no soporta una lista de listas, tiene q ser un objeto para poder nombralo
    "listDisplayDef" : {
        "description" : "Predefined column set (view)",
        "addPrompt" : "Please enter the name of the columnSet:",
        "allowDel" : true,
        "properties" : ["name", 'hideRowNumbers', "description"],
        "lists" : ["listDisplay"]

    },

    "hiddenFields" : {
        "description" : "List of hidden fields",
        "__ptStyle" : "colList"
    },

    "listDisplay" : {
        "description" : "List of fields to display in the grid",
        // "prpDefault" : ["__str__"],
        "addPrompt" : "Please enter the name for your alternative listDisplay:",
        "__ptStyle" : "colList"
    },

    "readOnlyFields" : {
        "description" : "List of fields to marked as ReadOnly ( the property ReadOnly can also be used )",
        "__ptStyle" : "colList"
    },

    "searchFields" : {
        "description" : "Search-enabled fields",
        "__ptStyle" : "colList"
    },

    "sortFields" : {
        "description" : "Order-enabled fields",
        "__ptStyle" : "colList"
    },

    "detailsConfig" : {
        "description" : "Details definition (Master-Detail relationship)",
        "listOf" : "detailDef",
        "allowAdd" : true
    },

    "detailDef" : {
        "description" : "Master-Detail relationship definition",
        "properties" : ["menuText", "conceptDetail", "masterField", "detailField", "detailName", "detailTitleLbl", "masterTitleField", "detailTitleField"],
        "addPrompt" : "Please enter the name for your detail:",
        "allowDel" : true
    },

    "usrDefProps" : {
        "description" : "User defined properties ( Fields created by the user, they do not participe in search and sort)",
        "properties" : ["udpTable", "propertyRef", "keyField", "propertyPrefix", "propertyName", "propertyValue"]
    },

    "sheetConfig" : {
        "description" : "Information templates in HTML that are fed by data from the database",
        "listOf" : "sheetDef",
        "allowAdd" : true
    },

    "sheetDef" : {
        "description" : "Templates definition ( the name is the selector )",
        "properties" : ["name", "template", "title", "viewIcon", "sheetType", "templateFp", "templateBb", "templateEr", "templateAb", "templateLp"],
        "lists" : ["sheetDetails"],
        "addPrompt" : "Please enter the name for your sheet:",
        "allowDel" : true
    },

    "sheetDetails" : {
        "description" : "Lista de detalles por hoja ( sheet )",
        "listOf" : "sheetDetail",
        "allowAdd" : true
    },

    "sheetDetail" : {
        "description" : "Sheet detail configuration",
        "properties" : ["name", "detailName", "detailSort", "templateBb", "templateEr", "templateAb"],
        "lists" : ["sheetDetails"],
        "addPrompt" : "Please enter the detailName:",
        "allowDel" : true
    },

    "formConfig" : {
        "hideItems" : true,
        "description" : "Form definition",
        "properties" : ["title", "tooltip", "height", "maxHeight", "minHeight", "width", "maxWidth", "minWidth", "viewIcon", "helpPath"]
    },

    "fieldset" : {
        "hideItems" : true,
        "description" : "A Fieldset, containing field elements",
        "properties" : ["title", "fsLayout", "autoscroll", "border", "collapsible", "collapsed", "labelWidth", "labelAlign", "hideLabel", "height", "maxHeight", "minHeight"
        // "width", "maxWidth","minWidth"
        ]
    },

    "htmlset" : {
        "hideItems" : true,
        "description" : "A Fieldset, containing HtmlField elements",
        "properties" : ["title", "collapsible", "collapsed", "flex", "height", "maxHeight", "minHeight"
        // "width", "maxWidth","minWidth"
        ]
    },

    "protoGrid" : {
        "description" : "A detail grid",
        "properties" : ["viewCode", "menuText", "height", "maxHeight", "minHeight", "minWidth"
        // ,"width", "maxWidth"
        ]
    },

    "detailButton" : {
        "description" : "A button link to detail",
        "properties" : [ "viewCode", "text", "addDetailForm" ]
    },


    "panel" : {
        "hideItems" : true,
        "description" : "A simple panel with fit layout",
        "properties" : ["title", "height", "maxHeight", "minHeight"
        // ,"width", "maxWidth","minWidth"
        ]
    },

    "tabpanel" : {
        "hideItems" : true,
        "description" : "A Tab Container with many tabs",
        "properties" : ["layout", "activeItem", "height", "maxHeight", "minHeight"
        // ,"width", "maxWidth","minWidth"
        ]
    },

    "actions" : {
        "description" : "Actions list (Actions menu)",
        "listOf" : "actionDef",
        "allowAdd" : true
    },

    "actionDef" : {
        "description" : "Actions definition (backend)",
        "properties" : [
            "name", 
            "title", "actionType", "selectionMode", 
            "refreshOnComplete",
            "executeJS", 
            "jsCode"
         ],
        "lists" : ["actionParams"],

        "addPrompt" : "Please enter the name for your action:",
        "allowDel" : true

    },

    "actionParams" : {
        "description" : "Actions definition parameters",
        "listOf" : "actionParam",
        "allowAdd" : true
    },

    "actionParam" : {
        "properties" : ["name", "tooltip", "fieldLabel", "prpDefault", "required", "readOnly", "format",

        // Para el combo
        "choices",

        // Para el zoom
        "fkId", "fkField", "zoomModel", "zoomFilter", "cellLink",

        // tipos
        "type", "xtype", "vType"],
        "addPrompt" : "Action parameter",
        "allowDel" : true
    },

    "businessRules" : {
        "properties" : ["dblClick", "afterCellUpdate", "afterRowDelete", "afterSave", "beforeCellEdit", "beforeCellUpdate", "beforeRowDelete", "beforeRowInsert", "beforeOpSave", "beforeValidate", "zoomConfigure", "zoomReturn", "issRowLoad", "reposition", "getLinkFilter", "validationComplete"]
    },

    "businessRule" : {
        "properties" : ["name", "handler", "src", "type", "field"],
        "addPrompt" : "Action parameters",
        "allowDel" : true
    },

    "businessRulesText" : {
        "description" : "Business rules",
        "properties" : ["afterCellUpdate", "afterRowDelete", "BeforeCellEdit", "BeforeCellUpdate", "BeforeRowDelete", "BeforeRowInsert", "dblClick", "issZoomConfigure", "issBeforeVslidateVr", "issHelpReturn", "issRowLoad", "reposition", "getLinkFilter", "afterOpSave", "beforeOpSave", "issValidationComplete"]
    }

};

