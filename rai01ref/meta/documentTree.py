
DocumentTreeDefition =  {

    # "viewCode": "rai01ref.Capacity.tree",
    # "viewEntity": "rai01ref.Capacity",
    "description": "Capacity",
    "shortTitle": "Capacity Tree",
    "jsonField": "info",

    # Tree ref 
    "pciStyle": "tree",
    "treeRefField": "refCapacity",

    # Form selector 
    "formSelector": "docType_id",

    "fields": [{
        "name": "code",
        "type": "string",
        "searchable": True,
        "required": True,
        "sortable": True
    }, {
        "name": "description",
        "type": "string",
        "searchable": True,
        "sortable": True

    }, {
        "name": "id",
        "type": "autofield",
        "hidden": True,
        "readOnly": True
    }, {
        "name": "__str__",
        "type": "string",
        "zoomModel": "rai01ref.Capacity",
        "flex": 1,
        "fkId": "id",
        "cellLink": True,
        "readOnly": True

    # Static field in model ( docType ) 
    }, {
        "name": "iconCls", 
        "type": "string",
        "crudType": "readOnly",

    # Hierarchy ( Parent : treeRefField )
    }, {
        "name": "refCapacity",
        "header": "Parent",
        "type": "foreigntext",
        "zoomModel": "rai01ref.Capacity",
        "fkId": "refCapacity_id",
        "cellLink": True
    }, {
        "name": "refCapacity_id",
        "type": "foreignid",
        "fkField": "refCapacity",
        "readOnly": True


    # Dynamic path hierarchy ( Parent : treeRefField )
    }, {
        "name": "fullPath", 
        "type": "string",
        "crudType": "readOnly",

    # Document Type 
    }, {
        "name": "docType",
        "type": "foreigntext",
        "fkId": "docType_id",
        "zoomFilter": "document, =CAPACITY",
        "zoomModel": "rai01ref.DocType",
        "required": True,
        "cellLink": True
    }, {
        "name": "docType_id",
        "type": "foreignid",
        "fkField": "docType",
        "hidden": True,
        "readOnly": True, 

    # Copy trace 
    }, {
        "name": "copyFrom",
        "type": "foreigntext",
        "zoomModel": "rai01ref.Capacity",
        "fkId": "copyFrom_id",
        "cellLink": True,
        "readOnly": True
    }, {
        "name": "copyFrom_id",
        "type": "foreignid",
        "fkField": "copyFrom",
        "hidden": True,
        "readOnly": True


    }],

    #  load all dynamic fields in tree definition for formSelector -- need reload after execute 
    "actions": [{
        "name": "doUpdateMeta",
        "menuText": "doUpdateMeta",
        "selectionMode": "none",
        "refreshOnComplete": True
    }],


    "detailsConfig": [{
        "detailName": "artefactcapacity", 
        "menuText": "Artefacts",
        "masterField": "pk",
        "detailField": "capacity__pk",
        "conceptDetail": "rai01ref.ArtefactCapacity",
    }, {
        "detailName": "projectcapacity", 
        "menuText": "Projects",
        "masterField": "pk",
        "detailField": "capacity__pk",
        "conceptDetail": "rai01ref.ProjectCapacity",
    }, {
        "detailName": "copyto", 
        "menuText": "Copies",
        "masterField": "pk",
        "detailField": "copyFrom_id",
        "conceptDetail": "rai01ref.Capacity",
    }]
}


    #  info field is not necesary  
    # }, {
    #     "name": "info",
    #     "type": "text",
    #     "crudType": "storeOnly"


DocServices = {
  "shortTitle": "Services",
  "description": "capacity: services",
  "jsonField": "info",
  "viewEntity": "rai01ref.Capacity",
  "viewCode": "rai01ref.Capacity.61",
  "viewIcon": "icon-1",
  "fields": [
    {
      "fkId": "docType_id",
      "searchable": False,
      "hidden": True,
      "type": "foreigntext",
      "name": "docType",
      "zoomModel": "rai01ref.DocType",
      "prpDefault": "Services",
      "header": "docType",
      "sortable": True,
      "cellLink": True,
      "readOnly": True
    },
    {
      "searchable": True,
      "required": True,
      "type": "string",
      "name": "smUUID",
      "sortable": True,
      "readOnly": True
    },
    {
      "searchable": True,
      "required": True,
      "type": "text",
      "crudType": "storeOnly",
      "name": "info",
      "header": "info",
      "sortable": True,
      "readOnly": True
    },
    {
      "fkId": "refCapacity_id",
      "searchable": False,
      "type": "foreigntext",
      "name": "refCapacity",
      "zoomModel": "rai01ref.Capacity",
      "header": "refCapacity",
      "sortable": True,
      "cellLink": True
    },
    {
      "searchable": True,
      "type": "foreigntext",
      "name": "smOwningTeam",
      "header": "smOwningTeam",
      "sortable": True,
      "cellLink": True,
      "readOnly": True
    },
    {
      "searchable": True,
      "required": True,
      "type": "string",
      "name": "code",
      "header": "code",
      "sortable": True
    },
    {
      "searchable": False,
      "required": False,
      "type": "autofield",
      "name": "id",
      "header": "ID",
      "sortable": False,
      "hidden": True,
      "readOnly": True
    },
    {
      "searchable": True,
      "type": "foreigntext",
      "name": "smOwningUser",
      "header": "smOwningUser",
      "sortable": True,
      "cellLink": True,
      "readOnly": True
    },
    {
      "hidden": True,
      "type": "foreignid",
      "name": "copyFrom_id",
      "header": "copyFrom_id",
      "fkField": "copyFrom",
      "readOnly": True
    },
    {
      "prpDefault": "61",
      "hidden": True,
      "type": "foreignid",
      "name": "docType_id",
      "header": "docType_id",
      "fkField": "docType",
      "readOnly": True
    },
    {
      "searchable": True,
      "type": "string",
      "name": "description",
      "header": "description",
      "sortable": True,
      "vType": "plainText"
    },
    {
      "searchable": True,
      "type": "foreigntext",
      "name": "smCreatedBy",
      "header": "smCreatedBy",
      "sortable": True,
      "cellLink": True,
      "readOnly": True
    },
    {
      "searchable": True,
      "type": "string",
      "name": "smNaturalCode",
      "header": "smNaturalCode",
      "sortable": True,
      "readOnly": True
    },
    {
      "fkId": "id",
      "type": "string",
      "name": "__str__",
      "zoomModel": "rai01ref.Capacity.61",
      "header": "Capacity",
      "sortable": True,
      "flex": 1,
      "cellLink": True,
      "readOnly": True
    },
    {
      "header": "fullPath",
      "type": "string",
      "crudType": "readOnly",
      "name": "fullPath",
      "readOnly": True
    },
    {
      "searchable": True,
      "type": "string",
      "name": "smRegStatus",
      "header": "smRegStatus",
      "sortable": True,
      "readOnly": True
    },
    {
      "searchable": True,
      "type": "string",
      "name": "smWflowStatus",
      "header": "smWflowStatus",
      "sortable": True,
      "readOnly": True
    },
    {
      "searchable": True,
      "type": "datetime",
      "name": "smModifiedOn",
      "header": "smModifiedOn",
      "sortable": True,
      "readOnly": True
    },
    {
      "required": False,
      "prpScale": 0,
      "prpLength": 0,
      "name": "info__responsable",
      "tooltip": "",
      "choices": "",
      "vType": "",
      "prpDefault": "",
      "type": "string",
      "header": "Responsable",
      "crudType": "",
      "readOnly": False
    },
    {
      "searchable": True,
      "type": "foreigntext",
      "name": "smModifiedBy",
      "header": "smModifiedBy",
      "sortable": True,
      "cellLink": True,
      "readOnly": True
    },
    {
      "fkId": "copyFrom_id",
      "searchable": False,
      "type": "foreigntext",
      "name": "copyFrom",
      "zoomModel": "rai01ref.Capacity",
      "header": "copyFrom",
      "sortable": True,
      "cellLink": True
    },
    {
      "required": True,
      "prpScale": 0,
      "prpLength": 0,
      "name": "info__catergory",
      "tooltip": "",
      "choices": "",
      "vType": "",
      "prpDefault": "",
      "type": "string",
      "header": "Catergory",
      "crudType": "",
      "readOnly": False
    },
    {
      "hidden": True,
      "type": "foreignid",
      "name": "refCapacity_id",
      "header": "refCapacity_id",
      "fkField": "refCapacity",
      "readOnly": True
    },
    {
      "searchable": True,
      "type": "datetime",
      "name": "smCreatedOn",
      "header": "smCreatedOn",
      "sortable": True,
      "readOnly": True
    }
  ],
  "actions": [
    {
      "selectionMode": "none",
      "name": "doUpdateMeta",
      "menuText": "doUpdateMeta"
    }
  ],
  "detailsConfig": [
    {
      "conceptDetail": "rai01ref.Artefact",
      "detailName": "artefact.capacity",
      "detailField": "capacity__pk",
      "menuText": "Artefact.capacity",
      "masterField": "pk"
    },
    {
      "conceptDetail": "rai01ref.ArtefactCapacity",
      "detailName": "artefactcapacity.capacity",
      "detailField": "capacity__pk",
      "menuText": "Artefactcapacity.capacity",
      "masterField": "pk"
    },
    {
      "conceptDetail": "rai01ref.ProjectCapacity",
      "detailName": "projectcapacity.capacity",
      "detailField": "capacity__pk",
      "menuText": "Projectcapacity.capacity",
      "masterField": "pk"
    }
  ],
  "gridConfig": {
    "baseFilter": [
      {
        "property": "docType",
        "filterStmt": "=61"
      }
    ],
    "searchFields": [
      "smNaturalCode",
      "smRegStatus",
      "smWflowStatus",
      "code",
      "description",
      "info"
    ],
    "listDisplay": [
      "code",
      "description"
    ]
  },
  "formConfig": {
   "items": [
      {
       "items": [
          {"name": "code"},
          {"name": "docType", "fieldLabel": "DocType", }, 
          {"name": "description", "prpLength": "1", }, 
          {"name": "refCapacity"},
          {"name": "copyFrom"}
        ],
        "fsLayout": "2col"
      },
      {
       "items": [
        ],
        "fsLayout": "2col",
        "title": "Document Config"
      },
      {
        "collapsible": True,
        "items": [
          {
            "name": "smOwningTeam"
          },
          {
            "name": "smOwningUser"
          },
          {
            "name": "smCreatedBy"
          },
          {
            "name": "smModifiedOn"
          },
          {
            "name": "smModifiedBy"
          },
          {
            "name": "smCreatedOn"
          }
        ],
        "collapsed": True,
        "title": "Admin",
       "fsLayout": "2col"
      }
    ]
  }
}

Artefact = {
    "detailsConfig": [{
        "menuText": "Artefactcomposition.containerArt",
        "detailField": "containerArt__pk",
        "conceptDetail": "rai01ref.ArtefactComposition",
        "masterField": "pk",
        "detailName": "artefactcomposition.containerArt",
        "__ptType": "detailDef"
    }, {
        "menuText": "Artefactrequirement.artefact",
        "detailField": "artefact__pk",
        "conceptDetail": "rai01ref.ArtefactRequirement",
        "masterField": "pk",
        "detailName": "artefactrequirement.artefact",
        "__ptType": "detailDef"
    }, {
        "menuText": "Artefactcapacity.artefact",
        "detailField": "artefact__pk",
        "conceptDetail": "rai01ref.ArtefactCapacity",
        "masterField": "pk",
        "detailName": "artefactcapacity.artefact",
        "__ptType": "detailDef"
    }, {
        "menuText": "Projectartefact.artefact",
        "detailField": "artefact__pk",
        "conceptDetail": "rai01ref.ProjectArtefact",
        "masterField": "pk",
        "detailName": "projectartefact.artefact",
        "__ptType": "detailDef"
    }, {
        "menuText": "Artefactsource.artefact",
        "detailField": "artefact__pk",
        "conceptDetail": "rai01ref.ArtefactSource",
        "masterField": "pk",
        "detailName": "artefactsource.artefact",
        "__ptType": "detailDef"
    }],
    "metaVersion": "150625",
    "viewIcon": "icon-1",
    "viewCode": "rai01ref.Artefact",
    "idProperty": "id",
    "description": "Artefact",
    "jsonField": "info",
    "gridConfig": {
        "searchFields": ["smNaturalCode", "smRegStatus", "smWflowStatus", "code", "description", "info"],
        "listDisplay": ["code", "description"],
        "baseFilter": [],
        "sortFields": ["smNaturalCode", "smRegStatus", "smWflowStatus", "code", "description", "info"],
        "initialFilter": [],
        "initialSort": [],
        "readOnlyFields": [],
        "hiddenFields": ["id"],
        "__ptType": "gridConfig"
    },
    "actions": [{
        "menuText": "doBPD",
        "__ptType": "actionDef",
        "name": "doBPD",
        "actionParams": [],
        "selectionMode": "sinlge"
    }],
    "formConfig": {
        "__ptType": "formConfig",
        "items": [{
            "fsLayout": "2col",
            "__ptType": "fieldset",
            "items": [{
                "name": "code",
                "__ptType": "formField"
            }]
        }, {
            "fsLayout": "2col",
            "__ptType": "fieldset",
            "items": [{
                "name": "copyFrom",
                "__ptType": "formField"
            }, {
                "name": "refArtefact",
                "__ptType": "formField"
            }, {
                "name": "docType",
                "__ptType": "formField"
            }]
        }, {
            "fsLayout": "1col",
            "__ptType": "fieldset",
            "items": [{
                "name": "description",
                "__ptType": "formField"
            }]
        }, {
            "collapsed": True,
            "fsLayout": "2col",
            "title": "Admin",
            "items": [{
                "name": "smOwningUser",
                "__ptType": "formField"
            }, {
                "name": "smCreatedOn",
                "__ptType": "formField"
            }, {
                "name": "smRegStatus",
                "__ptType": "formField"
            }, {
                "name": "smNaturalCode",
                "__ptType": "formField"
            }, {
                "name": "smModifiedBy",
                "__ptType": "formField"
            }, {
                "name": "smWflowStatus",
                "__ptType": "formField"
            }, {
                "name": "smOwningTeam",
                "__ptType": "formField"
            }, {
                "name": "smModifiedOn",
                "__ptType": "formField"
            }, {
                "name": "smUUID",
                "__ptType": "formField"
            }, {
                "name": "smCreatedBy",
                "__ptType": "formField"
            }],
            "collapsible": True,
            "__ptType": "fieldset"
        }]
    },
    "gridSets": {
        "listDisplaySet": [],
        "filtersSet": [],
        "sortersSet": [],
        "__ptType": "gridSets"
    },
    "fields": [{
        "type": "string",
        "zoomModel": "rai01ref.Artefact",
        "name": "__str__",
        "__ptType": "field",
        "cellLink": True,
        "fkId": "id",
        "sortable": True,
        "header": "Artefact",
        "flex": 1,
        "readOnly": True
    }, {
        "type": "string",
        "required": True,
        "name": "code",
        "sortable": True,
        "header": "code",
        "searchable": True,
        "__ptType": "field"
    }, {
        "type": "foreigntext",
        "zoomModel": "rai01ref.Artefact",
        "name": "copyFrom",
        "fkId": "copyFrom_id",
        "sortable": True,
        "header": "copyFrom",
        "__ptType": "field"
    }, {
        "type": "text",
        "vType": "plainText",
        "name": "description",
        "sortable": True,
        "header": "description",
        "searchable": True,
        "__ptType": "field"
    }, {
        "type": "foreigntext",
        "zoomModel": "rai01ref.DocType",
        "name": "docType",
        "fkId": "docType_id",
        "sortable": True,
        "header": "docType",
        "__ptType": "field"
    }, {
        "type": "foreigntext",
        "zoomModel": "rai01ref.Artefact",
        "name": "refArtefact",
        "fkId": "refArtefact_id",
        "sortable": True,
        "header": "refArtefact",
        "__ptType": "field"
    }, {
        "type": "foreignid",
        "hidden": True,
        "name": "copyFrom_id",
        "fkField": "copyFrom",
        "readOnly": True,
        "__ptType": "field"
    }, {
        "type": "foreignid",
        "hidden": True,
        "name": "docType_id",
        "fkField": "docType",
        "readOnly": True,
        "__ptType": "field"
    }, {
        "type": "autofield",
        "hidden": True,
        "name": "id",
        "readOnly": True,
        "header": "ID",
        "__ptType": "field"
    }, {
        "type": "text",
        "required": True,
        "name": "info",
        "__ptType": "field",
        "sortable": True,
        "header": "info",
        "crudType": "storeOnly",
        "searchable": True,
        "readOnly": True
    }, {
        "type": "foreignid",
        "hidden": True,
        "name": "refArtefact_id",
        "fkField": "refArtefact",
        "readOnly": True,
        "__ptType": "field"
    }, {
        "type": "foreigntext",
        "name": "smCreatedBy",
        "sortable": True,
        "readOnly": True,
        "header": "smCreatedBy",
        "searchable": True,
        "__ptType": "field"
    }, {
        "type": "datetime",
        "name": "smCreatedOn",
        "sortable": True,
        "readOnly": True,
        "header": "smCreatedOn",
        "searchable": True,
        "__ptType": "field"
    }, {
        "type": "foreigntext",
        "name": "smModifiedBy",
        "sortable": True,
        "readOnly": True,
        "header": "smModifiedBy",
        "searchable": True,
        "__ptType": "field"
    }, {
        "type": "datetime",
        "name": "smModifiedOn",
        "sortable": True,
        "readOnly": True,
        "header": "smModifiedOn",
        "searchable": True,
        "__ptType": "field"
    }, {
        "type": "string",
        "name": "smNaturalCode",
        "sortable": True,
        "readOnly": True,
        "header": "smNaturalCode",
        "searchable": True,
        "__ptType": "field"
    }, {
        "type": "foreigntext",
        "name": "smOwningTeam",
        "sortable": True,
        "readOnly": True,
        "header": "smOwningTeam",
        "searchable": True,
        "__ptType": "field"
    }, {
        "type": "foreigntext",
        "name": "smOwningUser",
        "sortable": True,
        "readOnly": True,
        "header": "smOwningUser",
        "searchable": True,
        "__ptType": "field"
    }, {
        "type": "string",
        "name": "smRegStatus",
        "sortable": True,
        "readOnly": True,
        "header": "smRegStatus",
        "searchable": True,
        "__ptType": "field"
    }, {
        "type": "string",
        "required": True,
        "name": "smUUID",
        "__ptType": "field",
        "sortable": True,
        "header": "smUUID",
        "searchable": True,
        "readOnly": True
    }, {
        "type": "string",
        "name": "smWflowStatus",
        "sortable": True,
        "readOnly": True,
        "header": "smWflowStatus",
        "searchable": True,
        "__ptType": "field"
    }],
    "usrDefProps": {
        "__ptType": "usrDefProps"
    },
    "shortTitle": "Artefact",
    "updateTime": "2016-05-09 20:03:20",
    "__ptType": "pcl",
    "businessRules": {
        "__ptType": "businessRules"
    },
    "sheetConfig": [],
    "viewEntity": "rai01ref.Artefact"
}