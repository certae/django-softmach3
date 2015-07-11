# -*- coding: utf-8 -*-

META_OBJECTS = {
    
    "versionMeta" : '14.0201', 

    "pcl" : {
        "description" : "Meta definition",
        "properties" : [
            "viewCode", "viewEntity", "viewIcon", "description", "shortTitle", 
            "localSort", "pageSize", 
            "sheetSelector", "pciStyle", "helpPath", "idProperty", 
            "jsonField", "returnField", "updateTime", 
            "metaVersion", "userVersion", "protoEntity", "protoEntityId", "pciType"
            ],
        "objects" : ["gridConfig", "gridSets", "formConfig", "custom", "businessRules"],
        "lists" : ["fields", "fieldsBase", "fieldsAdm", "actions", "detailsConfig", "sheetConfig", "defaultTo" ],
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
        "properties" : [
                "name", "required", "header", "fieldLabel", "tooltip", 
                "prpLength", "prpScale", 
                "prpDefault",  "format", "flex", "wordWrap",
                "sortable", "searchable", 
        
                # manejo
                "primary", "crudType", "readOnly", "hidden",
        
                # Para el combo
                "choices",
        
                # Para el zoom
                "fkId", "fkField", "cellLink", "zoomModel", "zoomFilter", "zoomMultiple",
        
                # Definien como heredar datos de otro campo ( ya se a de un zoom o del mismo rset )
                "cpFromField", "cpFromZoom",
        
                # Para los N2N
                # "conceptDetail", "relatedN2N", "detailField", "masterField",

                #  form formating 
                # "height","maxHeight","minHeight",
                # "width", "maxWidth","minWidth",
                # "hideLabel", "labelAlign","labelWidth",
        
                # "cellToolTip", "qbeHelp",

                "physicalName", "type", "xtype", "vType"
        ],

        "roProperties" : [] 

    },

    "formField" : {
        "description" : "A field element",
        "properties" : [
            "name", "tooltip", "fieldLabel", "labelWidth", "labelAlign", "hideLabel", 
            "required", "readOnly", "hidden", "prpDefault",
            "format", "prpLength",
            # "height","maxHeight","minHeight",
            # "width", "maxWidth","minWidth",


            # Para los campos del htmlSet
            "collapsed",

            # Para el combo
            "choices",

            # Para el zoom
            "fkId", "fkField", "zoomModel", "zoomFilter", "zoomMultiple", "cellLink",

            # Para los N2N
            # "conceptDetail", "relatedN2N", "detailField", "masterField",

            # tipos
            "type", "xtype", "vType"],
            "roProperties" : ["type "]

    },

    "gridConfig" : {
        "description" : "Grid configuration properties",
        "properties" : [
            'hideRowNumbers',
            # 'hideCheckSelect',
            'gridSelectionMode', "exportCsv", 'hideSheet', 'denyAutoPrint', 'filterSetABC', 
            'groupCol'
            ],

        "lists" : ["listDisplay", "baseFilter", "initialFilter", "initialSort",

            # TODO: Eliminar de aqui y pasar a obj  colShortcuts
            "searchFields", # TODO: Cambiar por sercheable
            "sortFields", # TODO: Cambiar por sortable
            "hiddenFields", "readOnlyFields"
            ],
        "objects" : [
            # "colShortcuts"
            ]

    },

    # TODO: Caundo se agrega aqui, al guardar actualiza fieldDefinition,
    # el agregar o borrar prevalece sobre la condicion del campo.
    "colShortcuts" : {
        "description" : "Column configuration shortcuts",
        "lists" : [
            "searchFields", # TODO: Cambiar por sercheable
            "sortFields", # TODO: Cambiar por sortable
            "hiddenFields", "readOnlyFields"
            # qbeAllowFields, textSearchFields
        ]
    },

    # Estos son actualizados por el staf ( admin de grupo )
    "gridSets" : {
        "description" : "Additional settings ( filters, sorters, userViews )",
        "lists" : ["listDisplaySet", "filtersSet", "sortersSet"]
    },

    # Estos son actualizados por los usuarios de base
    "custom" : {
        "description" : "custom user configurations",
        "lists" : ["listDisplay", "listDisplaySet", "filtersSet", "sortersSet"]
    },

    "baseFilter" : {
        "description" : "Default defined filter. No user-modifiable, e.g. { \"status__exact\":\"0\" } ",
        "listOf" : "filterDef",
        "allowAdd" : True
    },

    "customFilter" : {
        "description" : "Predefined filter ",
        "listOf" : "filterDef",
        "allowAdd" : True
    },

    "initialFilter" : {
        "description" : "Initial filter  Ej: { \"status__exact\":\"0\" } ",
        "listOf" : "filterDef",
        "allowAdd" : True
    },

    "initialSort" : {
        "description" : "Default ordering  Ej: [{\"direction\":\"ASC\",\"property\":\"code\"}, ... ] ",
        "listOf" : "sorterDef",
        "allowAdd" : True
    },

    "sorterDef" : {
        "description" : "Sort definition",
        "addPrompt" : "Please enter the name of the property for your sorter:",
        "allowDel" : True,
        "nodeName" : "property",
        "properties" : ["property", "direction"]
    },

    "sortersSet" : {
        "description" : "Sorter set",
        "listOf" : "sortersSetDef",
        "allowAdd" : True
    },

    "sortersSetDef" : {
        "description" : "Sorter set definition",
        "addPrompt" : "Please enter the name of the sorter:",
        "allowDel" : True,
        "properties" : ["name", "description"],
        "lists" : ["customSort"]
    },

    "customSort" : {
        "description" : "User ordering",
        "listOf" : "sorterDef",
        "allowAdd" : True
    },

    "filterDef" : {
        "description" : "Predefined filter definition",
        "addPrompt" : "Please enter the name of the property for your filter:",
        "allowDel" : True,
        "nodeName" : "property",
        "properties" : ["property", "filterStmt"]
    },

    "filtersSet" : {
        "description" : "Predefined filter set ( *x*, ><=, !=,  aa:bb ) ",
        "listOf" : "filtersSetDef",
        "allowAdd" : True
    },

    "filtersSetDef" : {
        "description" : "Filter set definition",
        "addPrompt" : "Please enter the name of the filterSet:",
        "allowDel" : True,
        "properties" : ["name", "menuText"],
        "lists" : ["customFilter"]
    },

    "listDisplaySet" : {
        "description" : "Alternative configuration for the grid ( it appears under the icon 'ViewCols' of the main bar )",
        "listOf" : "listDisplayDef",
        "allowAdd" : True
    },

    # El esquema no soporta una lista de listas, tiene q ser un objeto para poder nombralo
    "listDisplayDef" : {
        "description" : "Predefined column set (view)",
        "addPrompt" : "Please enter the name of the columnSet:",
        "allowDel" : True,
        "properties" : ["name", 'hideRowNumbers', "description"],
        "lists" : ["listDisplay"]

    },

    "hiddenFields" : {
        "description" : "List of hidden fields",
        "__ptStyle" : "colList"
    },

    "listDisplay" : {
        "description" : "List of fields to display in the grid",
        # "listDefault" : ["__str__"],
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
        "allowAdd" : True
    },

    "defaultTo" : {
        "description" : "Context : Set default to [ model, field ] ",
        "listOf" : "defaultToDef",
        "allowAdd" : True
    },

    "detailDef" : {
        "description" : "Master-Detail relationship definition",
        "properties" : ["menuText", "conceptDetail", "masterField", "detailField", "detailName", "detailTitleLbl", "masterTitleField", "detailTitleField"],
        "addPrompt" : "Please enter the name for your detail:",
        "allowDel" : True
    },

    "defaultToDef" : {
        "description" : "Context, set default definition",
        "properties" : ["deftModel", "deftField"],
        "addPrompt" : "Please enter the name for model to set defaults:",
        "allowDel" : True
    },


    "sheetConfig" : {
        "description" : "Information templates in HTML that are fed by data from the database",
        "listOf" : "sheetDef",
        "allowAdd" : True
    },

    "sheetDef" : {
        "description" : "Templates definition ( the name is the selector )",
        "properties" : ["name", "template", "title", "description", "viewIcon", "sheetType", "nameSpace", "pageExpr" ],
        "lists" : ["sheetDetails"],
        "addPrompt" : "Please enter the name for report:",
        "allowDel" : True
    },

    "sheetDetails" : {
        "description" : "Child reports",
        "listOf" : "sheetDetail",
        "allowAdd" : True
    },

    "sheetDetail" : {
        "description" : "Sheet detail configuration",
        "properties" : ["name", "description", "detailName", "template", "nameSpace", "pageExpr" ],
        "lists" : ["sheetDetails"],
        "addPrompt" : "Please enter the detailName:",
        "allowDel" : True
    },

    "formConfig" : {
        "hideItems" : True,
        "description" : "Form definition",
        "properties" : ["title", "tooltip", "height", "maxHeight", "minHeight", "width", "maxWidth", "minWidth", "viewIcon", "helpPath"]
    },

    "fieldset" : {
        "hideItems" : True,
        "description" : "A Fieldset, containing field elements",
        "properties" : ["title", "fsLayout", "autoscroll", "border", "collapsible", "collapsed", "labelWidth", "labelAlign", "hideLabel", "height", "maxHeight", "minHeight"
        # "width", "maxWidth","minWidth"
        ]
    },

    "htmlset" : {
        "hideItems" : True,
        "description" : "A Fieldset, containing HtmlField elements",
        "properties" : ["title", "collapsible", "collapsed", "flex", "height", "maxHeight", "minHeight"
        # "width", "maxWidth","minWidth"
        ]
    },

    "protoGrid" : {
        "description" : "A detail grid",
        "properties" : ["viewCode", "menuText", "height", "maxHeight", "minHeight", "minWidth"
        # ,"width", "maxWidth"
        ]
    },

    "detailButton" : {
        "description" : "A button link to detail",
        "properties" : [ "viewCode", "text", "addDetailForm" ]
    },


    "panel" : {
        "hideItems" : True,
        "description" : "A simple panel with fit layout",
        "properties" : ["title", "height", "maxHeight", "minHeight"
        # ,"width", "maxWidth","minWidth"
        ]
    },

    "tabpanel" : {
        "hideItems" : True,
        "description" : "A Tab Container with many tabs",
        "properties" : ["layout", "activeItem", "height", "maxHeight", "minHeight"
        # ,"width", "maxWidth","minWidth"
        ]
    },

    "actions" : {
        "description" : "Actions list (Actions menu)",
        "listOf" : "actionDef",
        "allowAdd" : True
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
        "allowDel" : True

    },

    "actionParams" : {
        "description" : "Actions definition parameters",
        "listOf" : "actionParam",
        "allowAdd" : True
    },

    "actionParam" : {
        "properties" : ["name", "tooltip", "fieldLabel", "prpDefault", "required", "readOnly", "format",

        # Para el combo
        "choices",

        # Para el zoom
        "fkId", "fkField", "zoomModel", "zoomFilter", "cellLink",

        # tipos
        "type", "xtype", "vType"],
        "addPrompt" : "Action parameter",
        "allowDel" : True
    },

    "businessRules" : {
        "properties" : ["dblClick", "afterCellUpdate", "afterRowDelete", "afterSave", "beforeCellEdit", "beforeCellUpdate", "beforeRowDelete", "beforeRowInsert", "beforeOpSave", "beforeValidate", "zoomConfigure", "zoomReturn", "issRowLoad", "reposition", "getLinkFilter", "validationComplete"]
    },

    "businessRule" : {
        "properties" : ["name", "handler", "src", "type", "field"],
        "addPrompt" : "Action parameters",
        "allowDel" : True
    },

    "businessRulesText" : {
        "description" : "Business rules",
        "properties" : ["afterCellUpdate", "afterRowDelete", "BeforeCellEdit", "BeforeCellUpdate", "BeforeRowDelete", "BeforeRowInsert", "dblClick", "issZoomConfigure", "issBeforeVslidateVr", "issHelpReturn", "issRowLoad", "reposition", "getLinkFilter", "afterOpSave", "beforeOpSave", "issValidationComplete"]
    }

}
